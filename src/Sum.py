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
        matching_1 = self.one_server(param)
        matching_2 = self.multiple_server(param)
        matching = min([matching_1, matching_2], key=lambda x: x["d_u"])

        if matching["d_u"] > param.DELAY_USER_MAX:
            self.status = False
        else:
            self.status = True
        t_1 = time.perf_counter()

        server_delays = []
        for server_key, is_used in enumerate(matching["matching"]):
            if is_used == 1:
                for edge_key, edge in enumerate(param.e_s):
                    if server_key in edge:
                        server_delays.append(param.d_st[edge_key])

        self.cpu_time = t_1 - t_0
        self.L_max = 2*matching["d_u"] + max(server_delays)
        self.L_min = 2*matching["d_u"] + min(server_delays)

    def one_server(self, param):
        # step 1: consider one server case

        # allocate all user and get L_1
        d_u_dict = dict()
        for k, v in enumerate(param.m_s):
            if v >= param.USER_NUM:
                d_u = param.d_us[:, k].max()
                d_u_dict[k] = d_u

        # search minimum d_u
        if bool(d_u_dict):
            d_u, server = min(d_u_dict.items(), key=lambda x: x[1])
            matching = [0 for i in range(param.SERVER_NUM)]
            matching[server] = 1
            return {"d_u": d_u, "matching": matching}
        else:
            return {"d_u": Constant.INF, "matching": None}

    def multiple_server(self, param):
        self.copy_servers(param)
        matching = self.search_matching(param)
        return {"d_u": matching["d_u"], "matching": matching["matching"]}

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
                return {"d_u": i, "matching": hc.matching()}
        return {"d_u": Constant.INF, "matching": None}

    def print_result(self):
        if self.status:
            print('L_max is ', str(self.L_max))
            print('L_min is ', str(self.L_min))
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
