import numpy as np
import pandas as pd
import itertools
import sys
import math

import Constant


class Parameter:

    USER_NUM_CONST = 25
    SERVER_NUM_CONST = 10
    CAPACITY_CONST = 5
    DELAY_USER_MAX_CONST = 10
    DELAY_SERVER_MAX_CONST = 10

    def __init__(self, seed):
        np.random.seed(seed)
        self.USER_NUM = Parameter.USER_NUM_CONST
        self.SERVER_NUM = Parameter.SERVER_NUM_CONST
        self.CAPACITY = Parameter.CAPACITY_CONST
        self.DELAY_USER_MAX = Parameter.DELAY_USER_MAX_CONST
        self.DELAY_SERVER_MAX = Parameter.DELAY_SERVER_MAX_CONST

    def create_input(self):
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        self.d_us = np.random.randint(1, self.DELAY_USER_MAX, (self.USER_NUM, self.SERVER_NUM))
        self.d_st = np.random.randint(1, self.DELAY_SERVER_MAX, len(self.e_s))
        self.m_s = np.full(self.SERVER_NUM, self.CAPACITY)

    def kanto_input(self):
        df_kanto = pd.read_csv("../network/kanto.csv")
        self.SERVER_NUM_KANTO = len(df_kanto)
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM_KANTO)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM_KANTO)), 2))
        self.m_s = np.full(self.SERVER_NUM_KANTO, self.CAPACITY)

        # 2点間の距離
        def get_distance(x_1, y_1, x_2, y_2): return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

        # d_stを作成
        d_st = []
        for link in self.e_s:
            city_1, city_2 = link[0], link[1]
            x_1, y_1 = df_kanto.iloc[city_1]["latitude"], df_kanto.iloc[city_1]["longitude"]
            x_2, y_2 = df_kanto.iloc[city_2]["latitude"], df_kanto.iloc[city_2]["longitude"]
            d_st.append(get_distance(x_1, y_1, x_2, y_2))
        self.d_st = np.array(d_st)
        print(self.d_st)

    def set_param(self, var_name, consts, var, delay_params):
        if var_name == 'user':
            self.USER_NUM = var
            self.SERVER_NUM = consts['server']
            self.CAPACITY = consts['capacity']
        elif var_name == 'server':
            self.USER_NUM = consts['user']
            self.SERVER_NUM = var
            self.CAPACITY = consts['capacity']
        elif var_name == 'capacity':
            self.USER_NUM = consts['user']
            self.SERVER_NUM = consts['server']
            self.CAPACITY = var
        else:
            sys.exit('invalid var_name = ' + str(var_name))

        self.DELAY_USER_MAX = delay_params["user_max"]
        self.DELAY_SERVER_MAX = delay_params["server_max"]

    def get_const(var_name):
        if var_name == 'user':
            return Parameter.USER_NUM_CONST
        elif var_name == 'server':
            return Parameter.SERVER_NUM_CONST
        elif var_name == 'capacity':
            return Parameter.CAPACITY_CONST
        else:
            sys.exit('invalid var_name = ' + str(var_name))


def main():
    param = Parameter(1)
    param.kanto_input()


if __name__ == '__main__':
    main()
