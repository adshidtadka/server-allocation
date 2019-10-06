import numpy as np
import time

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp


class Sum:

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
        D_u_1 = self.one_server(param)
        D_u_2 = self.multiple_server(param)
        D_u = min([D_u_1, D_u_2])

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

    def multiple_server(self, param):
        print("before copied edges_user = \n", self.edges_user)
        self.copy_servers(param)
        print("after copied edges_user = \n", self.edges_user)
        D_u = self.search_matching(param)
        print("D_u = ", D_u)
        return D_u

    def copy_servers(self, param):
        for edge in self.edges_user:
            for i in range(1, param.CAPACITY):
                new_edge = edge.copy()
                new_edge[1] += param.SERVER_NUM * i
                self.edges_user = np.vstack((self.edges_user, new_edge))
        param.COPY_SERVER_NUM = len(self.edges_user*param.CAPACITY)

    def search_matching(self, param):
        for i in range(1, param.DELAY_USER_MAX):
            hc = HopcroftKarp(param.USER_NUM, param.COPY_SERVER_NUM)
            for j in np.where(self.edges_user[:, -1] <= i)[0]:
                hc.add_edge(self.edges_user[j][0], self.edges_user[j][1])
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
    sum_obj = Sum(param)

    # start algorithm
    t_0 = time.perf_counter()
    sum_obj.start_algo(param)
    t_1 = time.perf_counter()
    sum_obj.cpu_time = t_1 - t_0

    # print result
    sum_obj.print_result()


if __name__ == '__main__':
    main()
