import numpy as np
import pandas as pd
import itertools
import sys

import Constant


class Parameter:

    USER_NUM_CONST = 10
    SERVER_NUM_CONST = 3
    CAPACITY_CONST = 10

    def __init__(self, seed):
        np.random.seed(seed)
        self.USER_NUM = 10
        self.SERVER_NUM = 3
        self.DELAY_USER_MAX = 20
        self.DELAY_SERVER = 1
        self.DELAY_SERVER_MAX = 10
        self.CAPACITY = 10

    def create_input(self):
        # inputs
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        self.d_us = np.random.randint(1, self.DELAY_USER_MAX, (self.USER_NUM, self.SERVER_NUM))
        self.d_st = np.random.randint(1, self.DELAY_SERVER_MAX, len(list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))))
        self.m_s = np.full(self.SERVER_NUM, self.CAPACITY)

    def set_param(self, var_name, consts, var):
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

    def get_const(var_name):
        if var_name == 'user':
            return Parameter.USER_NUM_CONST
        elif var_name == 'server':
            return Parameter.SERVER_NUM_CONST
        elif var_name == 'capacity':
            return Parameter.CAPACITY_CONST
        else:
            sys.exit('invalid var_name = ' + str(var_name))
