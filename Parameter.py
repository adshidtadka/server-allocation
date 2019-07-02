import numpy as np
import pandas as pd
from itertools import product

import Constant


class Parameter:
    def __init__(self, seed):
        np.random.seed(seed)
        self.create_input()

    def create_input(self):
        # inputs
        e_u = list(product(range(Constant.USER_NUM), range(Constant.SERVER_NUM)))
        e_s = list(itertools.combinations(list(range(0, Constant.SERVER_NUM)), 2))
        d_us = np.random.randint(0, Constant.DELAY_MAX, (Constant.USER_NUM, Constant.SERVER_NUM))
        v_s = list(range(0, Constant.SERVER_NUM))
        m_s = np.random.randint(0, Constant.CAPACITY_MAX, Constant.SERVER_NUM)

        # dataframe for E_U
        df_e_u = pd.DataFrame([(i, j) for i, j in e_u], columns=['user', 'server'])
        df_e_u['delay'] = d_us.flatten()
        self.df_e_u = df_e_u

        # dataframe for E_S
        df_e_s = pd.DataFrame([(i, j) for i, j in e_s], columns=['server_1', 'server_2'])
        df_e_s['delay'] = Constant.DELAY_SERVER
        self.df_e_s = df_e_s

        # dataframe for V_S
        df_v_s = pd.DataFrame(v_s, columns=['server'])
        df_v_s['capacity'] = m_s
        self.df_v_s = df_v_s
