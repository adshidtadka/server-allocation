import numpy as np
import time

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp


class Mmd:
    def start_algorithm(self, param):
        t_0 = time.process_time()

        L_1 = self.one_server_case(param)
        L_2 = self.multiple_server_case(param)
        D_u = min([L_1, L_2])

        t_1 = time.process_time()

        self.cpu_time = t_1 - t_0
        self.objective_function = D_u*2 + param.DELAY_SERVER

    def one_server_case(self, param):
        # step 1: consider one server case

        # allocate all user and get L_1
        dic_l = dict()
        for k, v in enumerate(param.m_s):
            if v >= param.USER_NUM:
                D_u = param.d_us[:, k].max()
                dic_l[k] = D_u

        # search minimum D_u
        if bool(dic_l):
            return min(dic_l)
        else:
            return Constant.INF

    def multiple_server_case(self, param):
        # step 2: consider multiple server case

        # initialize the bipartite graph
        d_us_cp = param.d_us
        for k, v in enumerate(param.m_s):
            for i in range(v - 1):
                d_us_cp = np.hstack((d_us_cp, d_us_cp[:, k].reshape(len(d_us_cp[:, k]), 1)))
        param.COPY_SERVER_NUM = len(d_us_cp[0])

        # sort d_us_cp
        sorted_link = np.empty(3, dtype=int)
        for k, v in enumerate(d_us_cp):
            for i, j in enumerate(v):
                sorted_link = np.vstack((sorted_link, np.array([k, i, j])))
        # sorted_link = sorted_link[np.argsort(sorted_link[:, 2])]

        # search matching
        for i in range(1, param.DELAY_MAX):
            hc = HopcroftKarp(param.USER_NUM, param.COPY_SERVER_NUM)
            for j in np.where(sorted_link[:, -1] <= i)[0]:
                hc.add_edge(sorted_link[j][0], sorted_link[j][1])
            if hc.flow() == param.USER_NUM:
                return i

        return Constant.INF

    def print_result(self):
        print('objective function is ', str(self.objective_function))
        print('it takes ' + str(self.cpu_time) + ' sec')


def main():
    # set input to algorithm
    mmd = Mmd()

    # start algorithm
    mmd.start_algorithm(Parameter(Constant.SEED))

    # print result
    mmd.print_result()


if __name__ == '__main__':
    main()
