import numpy as np
import pandas as pd
import itertools
import sys

import Constant


class Parameter:

    USER_NUM = 30
    SERVER_NUM = 8
    DELAY_MAX = 30
    DELAY_SERVER = 1
    CAPACITY_MAX = 10

    def __init__(self, seed):
        np.random.seed(seed)
        self.create_input()

    def create_input(self):
        # inputs
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        self.d_us = np.random.randint(1, self.DELAY_MAX, (self.USER_NUM, self.SERVER_NUM))
        self.m_s = np.random.randint(1, self.CAPACITY_MAX, self.SERVER_NUM)
