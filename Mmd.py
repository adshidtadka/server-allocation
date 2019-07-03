import numpy as np
import time

import Constant
from Parameter import Parameter


class Mmd:
    def start_algorithm(self, param):
        print('-------- t_0 --------')
        t_0 = time.process_time()

        L_1 = self.one_server_case(param)
        print(L_1)
        L_2 = self.multiple_server_case(param)

        t_1 = time.process_time()
        print('\n-------- t_1 --------')

        print('\nt_1 - t_0 is ', t_1 - t_0, '\n')

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
            return None

    def multiple_server_case(self, param):
        # step 2: consider multiple server case

        # initialize the bipartite graph
        for k, v in enumerate(param.m_s):
            for i in range(v - 1):
                param.d_us = np.hstack((param.d_us, param.d_us[:, k].reshape(len(param.d_us[:, k]), 1)))

        return None


def main():
    # set input to algorithm
    mmd = Mmd()

    # start algorithm
    mmd.start_algorithm(Parameter(Constant.SEED))


if __name__ == '__main__':
    main()
