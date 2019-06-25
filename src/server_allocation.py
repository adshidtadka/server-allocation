# ilp approach
# transport optimization

import numpy as np
import pandas as pd
import time
from itertools import product
from pulp import *


class Input:

    user_num = 800
    server_num = 8
    delay_max = 30
    delay_serer = 1
    capacity_max = 400

    def __init__(self, seed):
        np.random.seed(seed)
        e_u = list(
            product(range(self.user_num), range(self.server_num)))
        e_s = list(itertools.combinations(
            list(range(0, self.server_num)), 2))
        d_us = np.random.randint(
            0, self.delay_max, (self.user_num, self.server_num))
        v_s = list(range(0, self.server_num))
        m_s = np.random.randint(0, self.capacity_max, self.server_num)

        # dataframe for E_U
        df_e_u = pd.DataFrame([(i, j) for i, j in e_u],
                              columns=['user', 'server'])
        df_e_u['delay'] = d_us.flatten()
        self.df_e_u = df_e_u

        # dataframe for E_S
        df_e_s = pd.DataFrame([(i, j) for i, j in e_s],
                              columns=['server_1', 'server_2'])
        df_e_s['delay'] = self.delay_serer
        self.df_e_s = df_e_s

        # dataframe for V_S
        df_v_s = pd.DataFrame(v_s, columns=['server'])
        df_v_s['capacity'] = m_s
        self.df_v_s = df_v_s


def solveByIlp(input):
    # optimization problem
    m = LpProblem()

    # decision variables
    input.df_e_u['variable'] = [LpVariable('x_us%d' % i, cat=LpBinary)
                                for i in input.df_e_u.index]
    input.df_e_s['variable'] = [LpVariable('x_st%d' % i, cat=LpBinary)
                                for i in input.df_e_s.index]
    input.df_v_s['variable'] = [LpVariable('y%d' % i, cat=LpBinary)
                                for i in input.df_v_s.index]
    D_u = LpVariable('D_u', cat=LpInteger)
    D_s = LpVariable('D_s', cat=LpInteger)

    # objective function
    m += 2 * D_u + D_s

    # constraints
    # (1b)
    for k, v in input.df_e_u.groupby('user'):
        m += lpSum(v.variable) == 1

    # (1c)
    for k, v in input.df_e_u.groupby('server'):
        m += lpSum(v.variable) <= input.df_v_s['capacity'][k]

    # (1d)
    for k, v in input.df_e_u.iterrows():
        m += v.variable * v.delay <= D_u

    # (1e)
    for k, v in input.df_e_s.iterrows():
        m += v.variable * v.delay <= D_s

    # (1f)
    for k, v in input.df_e_u.groupby('user'):
        for l, w in input.df_v_s.iterrows():
            m += w.variable >= v.variable

    # (1g)
    for k, v in input.df_e_s.iterrows():
        m += input.df_v_s.iloc[v.server_1].variable + \
            input.df_v_s.iloc[v.server_2].variable - 1 <= v.variable

    # (1h)
    for k, v in input.df_e_s.iterrows():
        m += v.variable <= input.df_v_s.iloc[v.server_1].variable

    # (1i)
    for k, v in input.df_e_s.iterrows():
        m += v.variable <= input.df_v_s.iloc[v.server_2].variable

    # solve
    try:
        print('-------- t_0 --------')
        t_0 = time.process_time()
        m.solve(CPLEX_CMD(msg=1))
        t_1 = time.process_time()
        print('\n-------- t_1 --------')

        print('\nt_1 - t_0 is ', t_1 - t_0, '\n')
    except PulpSolverError:
        print(CPLEX_CMD().path, 'is not installed')

    # result
    if m.status == 1:
        print('objective function is = ', value(m.objective))
        input.df_e_u.variable = input.df_e_u.variable.apply(value)
        # print(input.df_e_u[input.df_e_u.variable >= 1])
    else:
        print('status code is = ', m.status)


def main():

    # create input
    input = Input(1)

    # solve by ilp
    solveByIlp(input)


if __name__ == '__main__':
    main()
