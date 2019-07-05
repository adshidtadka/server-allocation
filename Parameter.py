import numpy as np
import pandas as pd
import itertools
import sys

import Constant


class Parameter:

    def __init__(self, seed):
        np.random.seed(seed)
        self.USER_NUM = 500
        self.SERVER_NUM = 10
        self.DELAY_MAX = 10
        self.DELAY_SERVER = 1
        self.CAPACITY = 50

    def create_input(self):
        # inputs
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        self.d_us = np.random.randint(1, self.DELAY_MAX, (self.USER_NUM, self.SERVER_NUM))
        self.m_s = np.full(self.SERVER_NUM, self.CAPACITY)

    def set_user_num(self, v):
        self.USER_NUM = v

    def set_server_num(self, v):
        self.SERVER_NUM = v

    def set_capacity(self, v):
        self.CAPACITY = v
