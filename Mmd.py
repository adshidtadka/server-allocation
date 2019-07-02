import numpy as np
import pandas as pd
import time

import Constant
import Parameter


class Mmd:

    def __init__(self, param):
        self.set_input(param)

    def set_input(self, param):
        self.param = param

    def start_algorithm(self):
        # step 1: Consider one server case
        for s in self.param.df_v_s:
            print(s)


def main():

    # set input to algorithm
    mmd = Mmd(Parameter(Constant.SEED))

    # start algorithm
    mmd.start_algorithm()


if __name__ == '__main__':
    main()
