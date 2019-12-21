import numpy as np
import pandas as pd
import itertools
import sys
import math

import Constant


class Parameter:

    USER_NUM_CONST = 4
    SERVER_NUM_CONST = 8
    CAPACITY_CONST = 20
    DELAY_USER_MAX_CONST = 10
    DELAY_SERVER_MAX_CONST = 10

    def __init__(self, seed):
        np.random.seed(seed)
        self.USER_NUM = Parameter.USER_NUM_CONST
        self.SERVER_NUM = Parameter.SERVER_NUM_CONST
        self.CAPACITY = Parameter.CAPACITY_CONST
        self.DELAY_USER_MAX = Parameter.DELAY_USER_MAX_CONST
        self.DELAY_SERVER_MAX = Parameter.DELAY_SERVER_MAX_CONST

    def create_input(self, is_real):
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        self.m_s = np.full(self.SERVER_NUM, self.CAPACITY)

        if is_real == True:
            df_server = pd.read_csv("../../network/kanto.csv")
            self.d_st = self.get_d_st(df_server)
            self.d_us = self.get_d_us(df_server)
        else:
            self.d_us = np.random.randint(1, self.DELAY_USER_MAX, (self.USER_NUM, self.SERVER_NUM))
            self.d_st = np.random.randint(1, self.DELAY_SERVER_MAX, len(self.e_s))

    def get_d_st(self, df):
        d_st = []
        for link in self.e_s:
            city_1, city_2 = link[0], link[1]
            x_1, y_1 = df.iloc[city_1]["latitude"], df.iloc[city_1]["longitude"]
            x_2, y_2 = df.iloc[city_2]["latitude"], df.iloc[city_2]["longitude"]
            d_st.append(Parameter.get_distance(x_1, y_1, x_2, y_2))
        return np.array(d_st)

    def get_lower_and_upper(df, col):
        return df[col].min() - 0.3, df[col].max() + 0.3

    def get_d_us(self, df_server):
        # 範囲
        lati_lower, lati_upper = Parameter.get_lower_and_upper(df_server, "latitude")
        longi_lower, longi_upper = Parameter.get_lower_and_upper(df_server, "longitude")

        # userの座標情報の作成
        lati_array = (lati_upper - lati_lower) * np.random.rand(self.USER_NUM) + lati_lower
        longi_array = (longi_upper - longi_lower) * np.random.rand(self.USER_NUM) + longi_lower
        df_user = pd.DataFrame({"latitude": lati_array, "longitude": longi_array})

        d_us = []
        for i in range(self.USER_NUM):
            d_us_row = []
            for j in range(self.SERVER_NUM):
                x_1, y_1 = df_user.iloc[i]["latitude"], df_user.iloc[i]["longitude"]
                x_2, y_2 = df_server.iloc[j]["latitude"], df_server.iloc[j]["longitude"]
                d_us_row.append(Parameter.get_distance(x_1, y_1, x_2, y_2))
            d_us.append(d_us_row)
        return np.array(d_us)

    def set_param(self, var_name, consts, var, delay_params, is_real):
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

        if is_real == True:
            df_server = pd.read_csv("../../network/kanto.csv")
            self.SERVER_NUM = len(df_server)
            lati_lower, lati_upper = Parameter.get_lower_and_upper(df_server, "latitude")
            longi_lower, longi_upper = Parameter.get_lower_and_upper(df_server, "longitude")
            delay_max = Parameter.get_distance(lati_lower, longi_lower, lati_upper, longi_upper)
            self.DELAY_USER_MAX = delay_max
            self.DELAY_SERVER_MAX = delay_max
        else:
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

    def get_distance(x_1, y_1, x_2, y_2): return round(math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) * 10)


def main():
    param = Parameter(1)
    param.create_input(True)
    print(param.d_us)
    print(param.d_st)
    param.create_input(False)
    print(param.d_us)
    print(param.d_st)


if __name__ == '__main__':
    main()
