import numpy as np
import time

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp
from Method import Method


class Sum(Method):

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

    def start_algo(self, param):
        t_0 = time.perf_counter()
        D_u_1 = self.one_server(param)
        D_u_2 = self.multiple_server(param)
        D_u = min([D_u_1, D_u_2])

        if D_u > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
        t_1 = time.perf_counter()
        self.cpu_time = t_1 - t_0
        self.D_u = D_u
        self.D_s_max = max(param.d_st)
        self.D_s_min = min(param.d_st)

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

    def multiple_server(self, param):
        self.copy_servers(param)
        D_u = self.search_matching(param)
        return D_u

    def copy_servers(self, param):
        for edge in self.edges_user:
            for i in range(1, param.CAPACITY):
                new_edge = edge.copy()
                new_edge[1] += param.SERVER_NUM * i
                self.edges_user = np.vstack((self.edges_user, new_edge))

    def search_matching(self, param):
        for i in range(1, param.DELAY_USER_MAX):
            hc = HopcroftKarp(param.USER_NUM, param.SERVER_NUM * param.CAPACITY)
            for j in np.where(self.edges_user[:, -1] <= i)[0]:
                hc.add_edge(self.edges_user[j][0], self.edges_user[j][1])
            if hc.flow() == param.USER_NUM:
                return i
        return Constant.INF

    def print_result(self):
        if self.status:
            print('D_u is ', str(self.D_u))
            print('D_s_max is ', str(self.D_s_max))
            print('D_s_min is ', str(self.D_s_min))
            print('cpu time is ' + str(self.cpu_time) + ' sec')
        else:
            print('Error')


def main():
    # create param
    param = Parameter(Constant.SEED)
    param.create_input()

    # set input to algorithm
    sum_obj = Sum(param)

    # start algorithm
    sum_obj.start_algo(param)

    # print result
    sum_obj.print_result()


if __name__ == '__main__':
    main()
