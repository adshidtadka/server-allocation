import numpy as np
import time

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp


class Mmd:

    def __init__(self, param):
        self.set_input(param)

    def set_input(self, param):
        # edges list
        edges = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_us):
            for i, j in enumerate(v):
                edges = np.vstack((edges, np.array([k, i, j])))
        self.edges = edges

    def start_general(self, param):
        L_1 = self.one_server_case(param)
        L_2 = self.multiple_server_case(param)
        D_u = min([L_1, L_2])

        if D_u > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
            self.objective_function = D_u * 2 + param.DELAY_SERVER

    def start_special(self, param):
        L_1 = self.one_server_case(param)
        L_2 = self.multiple_server_case(param)
        D_u = min([L_1, L_2])

        if D_u > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
            self.objective_function = D_u * 2 + param.DELAY_SERVER

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
            return min(dic_l.values())
        else:
            return Constant.INF

    def multiple_server_case(self, param):
        # step 2: consider multiple server case

        # initialize the bipartite graph
        added_server = param.SERVER_NUM
        for k, v in enumerate(param.m_s):
            for j in range(param.USER_NUM):
                delay = param.d_us[j][k]
                for i in range(added_server, added_server + v - 1):
                    self.edges = np.vstack((self.edges, np.array([j, i, delay])))
                added_server += v - 1
        param.COPY_SERVER_NUM = added_server

        # search matching
        for i in range(1, param.DELAY_USER_MAX):
            hc = HopcroftKarp(param.USER_NUM, param.COPY_SERVER_NUM)
            for j in np.where(self.edges[:, -1] <= i)[0]:
                hc.add_edge(self.edges[j][0], self.edges[j][1])
            if hc.flow() == param.USER_NUM:
                return i

        return Constant.INF

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
    mmd.start_special(param)
    t_1 = time.perf_counter()
    mmd.cpu_time = t_1 - t_0

    # print result
    mmd.print_result()


if __name__ == '__main__':
    main()
