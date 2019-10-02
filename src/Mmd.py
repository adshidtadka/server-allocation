import numpy as np
import time

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp
from BronKerbosch import BronKerbosch


class Mmd:

    def __init__(self, param):
        self.set_input(param)

    def set_input(self, param):
        # edges_user list
        edges_user = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_us):
            for i, j in enumerate(v):
                edges_user = np.vstack((edges_user, np.array([k, i, j])))
        edges_user = np.delete(edges_user, 0, 0)
        self.edges_user = edges_user

        # edges_server list
        edges_server = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_st):
            edges_server = np.vstack((edges_server, np.array([param.e_s[k][0], param.e_s[k][1], v])))
        edges_server = np.delete(edges_server, 0, 0)
        self.edges_server = edges_server

    def start_general(self, param):
        L_1 = self.one_server(param)
        L_2 = self.multiple_server_general(param)
        D_u = min([L_1, L_2])

        if D_u > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
            self.objective_function = D_u * 2 + param.DELAY_SERVER

    def start_special(self, param):
        L_1 = self.one_server(param)
        L_2 = self.multiple_server_special(param)
        D_u = min([L_1, L_2])

        if D_u > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
            self.objective_function = D_u * 2 + param.DELAY_SERVER

    def one_server(self, param):
        # step 1: consider one server case

        # allocate all user and get L_1
        dic_l = dict()
        for k, v in enumerate(param.m_s):
            if v >= param.USER_NUM:
                D_u = param.d_us[:, k].max()
                dic_l[k] = D_u

        # search minimum D_u
        if bool(dic_l):
            return min(dic_l.values())
        else:
            return Constant.INF

    def multiple_server_special(self, param):
        # step 2: consider multiple server case
        self.create_copy_servers(param)
        self.search_matching(param)

        return Constant.INF

    def create_copy_servers(self, param):
        added_server = param.SERVER_NUM
        for k, v in enumerate(param.m_s):
            for j in range(param.USER_NUM):
                delay = param.d_us[j][k]
                for i in range(added_server, added_server + v - 1):
                    self.edges_user = np.vstack((self.edges_user, np.array([j, i, delay])))
                added_server += v - 1
        param.COPY_SERVER_NUM = added_server

    def search_matching(self, param):
        for i in range(1, param.DELAY_USER_MAX):
            hc = HopcroftKarp(param.USER_NUM, param.COPY_SERVER_NUM)
            # fixme: hcのオブジェクトをいちいち初期化しなくてもいいかも
            for j in np.where(self.edges_user[:, -1] <= i)[0]:
                hc.add_edge(self.edges_user[j][0], self.edges_user[j][1])
            if hc.flow() == param.USER_NUM:
                return i

    def multiple_server_general(self, param):
        # step 2: consider multiple server case

        # search clique
        bk = BronKerbosch(param.SERVER_NUM)
        record = []
        for i in range(1, param.DELAY_SERVER_MAX):
            for j in np.where(self.edges_server[:, -1] == i)[0]:
                bk.add_edge(self.edges_server[j][0], self.edges_server[j][1])
            print(bk.find_cliques())
            for clique in bk.find_cliques():
                if clique in record:
                    continue
                else:
                    record.append(clique)
                if len(clique) < param.USER_NUM:
                    continue

    def print_result(self):
        if self.status:
            print('objective function is ', str(self.objective_function))
            print('cpu time is ' + str(self.cpu_time) + ' sec')
        else:
            print('Error')


def main():
    # create param
    param = Parameter(Constant.SEED)
    param.create_input()

    # set input to algorithm
    mmd = Mmd(param)

    # start algorithm
    t_0 = time.perf_counter()
    mmd.start_general(param)
    t_1 = time.perf_counter()
    mmd.cpu_time = t_1 - t_0

    # print result
    mmd.print_result()


if __name__ == '__main__':
    main()
