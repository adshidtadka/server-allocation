import numpy as np
import pandas as pd
import time

import Constant
from Parameter import Parameter


class Mmd:

    def __init__(self, param):
        self.set_input(param)

    def set_input(self, param):
        param.df_e_u['x'] = 0
        param.df_e_s['x'] = 0
        param.D_u = 0

        # for step 1 an step 2
        self.param_1 = param
        self.param_2 = param

    def start_algorithm(self):
        print('-------- t_0 --------')
        t_0 = time.process_time()

        L_1 = self.one_server_case(self.param_1)
        print(L_1)
        L_2 = self.multiple_server_case(self.param_2)

        t_1 = time.process_time()
        print('\n-------- t_1 --------')

        print('\nt_1 - t_0 is ', t_1 - t_0, '\n')

    def one_server_case(self, param):
        # step 1: consider one server case

        # allocate all user and get L_1
        dic_l = dict()
        for k, v in param.df_v_s.iterrows():
            if v['capacity'] >= param.USER_NUM:
                D_u = param.df_e_u[param.df_e_u.server == k]['delay'].max()
                dic_l[k] = D_u

        # search minimum D_u
        if bool(dic_l):
            s = min(dic_l, key=dic_l.get)
        else:
            return None

        # set x and D_u
        param.df_e_u.loc[param.df_e_u.server == s, 'x'] = 1
        param.D_u = dic_l[s]

        return dic_l[s]

    def multiple_server_case(self, param):
        # step 2: consider multiple server case

        # initialize the bipartite graph

        return None


def main():
    # set input to algorithm
    mmd = Mmd(Parameter(Constant.SEED))

    # start algorithm
    mmd.start_algorithm()


if __name__ == '__main__':
    main()
