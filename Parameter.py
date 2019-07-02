import numpy as np
import pandas as pd
import itertools
import sys

import Constant


class Parameter:

    USER_NUM = 800
    SERVER_NUM = 8
    DELAY_MAX = 30
    DELAY_SERVER = 1
    CAPACITY_MAX = 400

    def __init__(self, seed):
        np.random.seed(seed)
        self.create_input()

    def create_input(self):
        # inputs
        e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        d_us = np.random.randint(0, self.DELAY_MAX, (self.USER_NUM, self.SERVER_NUM))
        v_s = list(range(0, self.SERVER_NUM))
        m_s = np.random.randint(0, self.CAPACITY_MAX, self.SERVER_NUM)

        # dataframe for E_U
        df_e_u = pd.DataFrame([(i, j) for i, j in e_u], columns=['user', 'server'])
        df_e_u['delay'] = d_us.flatten()
        self.df_e_u = df_e_u

        # dataframe for E_S
        df_e_s = pd.DataFrame([(i, j) for i, j in e_s], columns=['server_1', 'server_2'])
        df_e_s['delay'] = self.DELAY_SERVER
        self.df_e_s = df_e_s

        # dataframe for V_S
        df_v_s = pd.DataFrame(v_s, columns=['server'])
        df_v_s['capacity'] = m_s
        self.df_v_s = df_v_s
