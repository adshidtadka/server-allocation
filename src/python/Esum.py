import numpy as np
import time
import subprocess

import Constant
from Parameter import Parameter
from Sum import Sum
from BronKerbosch import BronKerbosch


class Esum(Sum):

    def __init__(self, param):
        self.set_edges_user(param)
        self.set_edges_server(param)

    def read_output(self):
        path = "../../tmp/output.txt"
        with open(path, mode="r") as f:
            output = f.read().split()
        self.cpu_time = float(output[0]) / 1000 / 1000
        self.L = int(output[1])

    def set_edges_server(self, param):
        edges_server = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_st):
            edges_server = np.vstack((edges_server, np.array([param.e_s[k][0], param.e_s[k][1], v])))
        self.edges_server = np.delete(edges_server, 0, 0)

    def start_algo(self, param):
        self.write_input(param)
        command = "../cpp/run_esum.out"
        subprocess.call(command)
        self.status = True
        self.read_output()

    def print_result(self):
        if self.status:
            print('objective function is ', str(self.L))
            print('cpu time is ' + str(self.cpu_time) + ' sec')
        else:
            print('Error')


def main():
    # create param
    param = Parameter(Constant.SEED)
    param.create_input()

    # set input to algorithm
    esum = Esum(param)

    # start algorithm
    esum.start_algo(param)

    # print result
    esum.print_result()


if __name__ == '__main__':
    main()
