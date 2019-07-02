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
        # for step 1
        self.param_1 = param
        # for step 2
        self.param_2 = param

    def start_algorithm(self):
        # step 1: Consider one server case
        dic_l = dict()
        for k, v in self.param_1.df_v_s.iterrows():
            # if v['capacity'] >= self.param.USER_NUM:
            # get L'
            D_u = self.param_1.df_e_u[self.param_1.df_e_u.server == k]['delay'].max()
            dic_l[k] = D_u

        s = min(dic_l, key=dic_l.get)
        self.param_1.df_e_u.loc[self.param_1.df_e_u.server == s, 'x'] = 1
        self.param_1.D_u = dic_l[s]


def main():
    # set input to algorithm
    mmd = Mmd(Parameter(Constant.SEED))

    # start algorithm
    mmd.start_algorithm()


if __name__ == '__main__':
    main()
