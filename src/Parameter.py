import numpy as np
import pandas as pd
import itertools
import sys

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
        # inputs
        self.e_u = list(itertools.product(range(self.USER_NUM), range(self.SERVER_NUM)))
        self.e_s = list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))
        self.d_us = np.random.randint(1, self.DELAY_USER_MAX, (self.USER_NUM, self.SERVER_NUM))
        self.d_st = np.random.randint(1, self.DELAY_SERVER_MAX, len(list(itertools.combinations(list(range(0, self.SERVER_NUM)), 2))))
        self.m_s = np.full(self.SERVER_NUM, self.CAPACITY)

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
