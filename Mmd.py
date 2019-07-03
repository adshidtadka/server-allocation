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
        d_us_cp = param.d_us
        for k, v in enumerate(param.m_s):
            for i in range(v - 1):
                d_us_cp = np.hstack((d_us_cp, d_us_cp[:, k].reshape(len(d_us_cp[:, k]), 1)))

        # sort d_us_cp
        link_arr = np.empty(3, dtype=int)
        for k, v in enumerate(param.d_us):
            for i, j in enumerate(v):
                link_arr = np.vstack((link_arr, np.array([k, i, j])))
        link_arr = link_arr[np.argsort(link_arr[:, 2])]

        return None


def main():
    # set input to algorithm
    mmd = Mmd()

    # start algorithm
    mmd.start_algorithm(Parameter(Constant.SEED))


if __name__ == '__main__':
    main()
