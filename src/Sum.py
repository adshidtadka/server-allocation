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
        L_1 = Sum.one_server(param)
        L_2 = self.multiple_server(param)
        D_u = min([L_1, L_2])

        if D_u > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
            self.objective_function = D_u * 2 + param.DELAY_SERVER

    def one_server(param):
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
        return self.search_matching(param)

    def copy_servers(self, param):
        copy_server_num = param.SERVER_NUM
        for k, v in enumerate(param.m_s):
            for j in range(param.USER_NUM):
                delay = param.d_us[j][k]
                for i in range(copy_server_num, copy_server_num + v - 1):
                    self.edges_user = np.vstack((self.edges_user, np.array([j, i, delay])))
                copy_server_num += v - 1
        param.COPY_SERVER_NUM = copy_server_num

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
