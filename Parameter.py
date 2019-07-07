import numpy as np
import pandas as pd
import itertools
import sys

import Constant


class Parameter:

    USER_NUM_FIXED = 500
    SERVER_NUM_FIXED = 10
    CAPACITY_FIXED = 50

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

    def set_param(self, sim_name, param):
        if sim_name == 'user':
            self.USER_NUM = param
        elif sim_name == 'server':
            self.SERVER_NUM = param
        elif sim_name == 'capacity':
            self.CAPACITY = param

    def get_fixed_param(sim_name):
        if sim_name == 'user':
            return Parameter.USER_NUM_FIXED
        elif sim_name == 'server':
            return Parameter.SERVER_NUM_FIXED
        elif sim_name == 'capacity':
            return Parameter.CAPACITY_FIXED
