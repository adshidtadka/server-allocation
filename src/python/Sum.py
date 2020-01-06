import numpy as np
import time
import itertools
import os
import subprocess

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp
from Method import Method


class Sum(Method):

    def __init__(self, param):
        self.set_edges_user(param)

    def set_edges_user(self, param):
        edges_user = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_us):
            for i, j in enumerate(v):
                edges_user = np.vstack((edges_user, np.array([k, i, j])))
        self.edges_user = np.delete(edges_user, 0, 0)

    def write_input(self, param):
        if not os.path.exists('../../tmp'):
            os.mkdir('../../tmp')
        path = "../../tmp/input.txt"
        with open(path, mode="w") as f:
            f.write(str(param.USER_NUM) + " " + str(param.SERVER_NUM) + " " + str(param.CAPACITY) + " " +
                    str(param.DELAY_USER_MAX) + " " + str(min(param.d_st)) + " " + str(max(param.d_st)) + "\n")
            f.write("\n")

            # write userDelays
            for delay in param.d_us:
                for i in delay:
                    f.write(str(i) + " ")
                f.write("\n")
            f.write("\n")

            # write serverDelays
            server_delays = np.zeros((param.SERVER_NUM, param.SERVER_NUM), dtype=np.int)
            for k, v in enumerate(param.e_s):
                server_delays[v[0]][v[1]] = param.d_st[k]
                server_delays[v[1]][v[0]] = param.d_st[k]
            for delay in server_delays:
                for i in delay:
                    f.write(str(i) + " ")
                f.write("\n")
            f.write("\n")

    def read_output(self):
        path = "../../tmp/output.txt"
        with open(path, mode="r") as f:
            output = f.read().split()
        self.cpu_time = float(output[0]) / 1000 / 1000
        self.L_min = int(output[1])
        self.L_max = int(output[2])

    def start_algo(self, param):
        self.write_input(param)
        command = "../cpp/run_sum.out"
        subprocess.call(command)
        self.status = True
        self.read_output()

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
            d_u = min(d_u_dict.values())
            server = min([key for key in d_u_dict if d_u_dict[key] == d_u])
            return {"d_u": d_u, "used_server": [server]}
        else:
            return {"d_u": Constant.INF, "used_server": None}

    def multiple_server(self, param):
        self.copy_servers(param)
        solution = self.search_matching(param)
        used_server = []
        if solution["d_u"] == Constant.INF:
            return {"d_u": Constant.INF, "used_server": used_server}
        else:
            for k, v in enumerate(solution["matching"]):
                if (v == 1) & (k < param.SERVER_NUM):
                    used_server.append(k)
            return {"d_u": solution["d_u"], "used_server": used_server}

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
    param.create_input(True)

    # set input to algorithm
    sum_obj = Sum(param)
    sum_obj.write_input(param)

    # start algorithm
    sum_obj.start_algo(param)

    # print result
    sum_obj.print_result()


if __name__ == '__main__':
    main()
