import numpy as np
import time

import Constant
from Parameter import Parameter
from Sum import Sum
from BronKerbosch import BronKerbosch


class Esum(Sum):

    def __init__(self, param):
        self.set_edges_user(param)
        self.set_edges_server(param)

    def set_edges_server(self, param):
        edges_server = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_st):
            edges_server = np.vstack((edges_server, np.array([param.e_s[k][0], param.e_s[k][1], v])))
        self.edges_server = np.delete(edges_server, 0, 0)

    def start_algo_with_cpp(self, param):
        self.write_input(param)
        # command = "../cpp/run_esum.out"
        # subprocess.call(command)
        # self.status = True
        # self.read_output()

    def start_algo(self, param):
        t_0 = time.process_time()
        L_1 = self.one_server(param)["d_u"]*2
        L_2 = self.multiple_server(param)
        L = min([L_1, L_2])

        if L > param.DELAY_USER_MAX*2 + param.DELAY_SERVER_MAX:
            self.status = False
        else:
            self.status = True
            self.L = L
        t_1 = time.process_time()
        self.cpu_time = t_1 - t_0

    def multiple_server(self, param):
        # step 2: consider multiple server case

        # search clique
        bk = BronKerbosch(param.SERVER_NUM)
        record = []
        L = Constant.INF
        for D_s in range(1, param.DELAY_SERVER_MAX):
            for j in np.where(self.edges_server[:, -1] == D_s)[0]:
                bk.add_edge(self.edges_server[j][0], self.edges_server[j][1])
            for clique in bk.find_cliques():
                if clique in record:
                    continue
                else:
                    record.append(clique)

                # set edges_user
                edges_user = np.empty(3, dtype=int)
                for node in clique:
                    edges_user = np.vstack((edges_user, self.edges_user[np.where((self.edges_user[:, 1] == node))]))
                self.edges_user = np.delete(edges_user, 0, 0)

                D_u = Sum.multiple_server(self, param)["d_u"]
                L = min(L, D_u * 2 + D_s)
        return L

    def print_result(self):
        if self.status:
            print('objective function is ', str(self.L))
            print('cpu time is ' + str(self.cpu_time) + ' sec')
        else:
            print('Error')


def main():
    # create param
    param = Parameter(Constant.SEED)
    param.create_input(True)

    # set input to algorithm
    esum = Esum(param)

    # start algorithm
    esum.start_algo_with_cpp(param)

    # print result
    # esum.print_result()


if __name__ == '__main__':
    main()
