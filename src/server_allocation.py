# ilp approach
# transport optimization

import numpy as np
import pandas as pd
import time
from itertools import product
from pulp import *


class Problem:

    # constants
    USER_NUM = 800
    SERVER_NUM = 8
    DELAY_MAX = 30
    DELAY_SERVER = 1
    CAPACITY_MAX = 400

    def __init__(self, seed):
        np.random.seed(seed)

        # inputs
        e_u = list(product(range(self.USER_NUM), range(self.SERVER_NUM)))
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

    def solve_by_ilp(self):
        # optimization problem
        m = LpProblem()

        # decision variables
        self.df_e_u['variable'] = [LpVariable('x_us%d' % i, cat=LpBinary) for i in self.df_e_u.index]
        self.df_e_s['variable'] = [LpVariable('x_st%d' % i, cat=LpBinary) for i in self.df_e_s.index]
        self.df_v_s['variable'] = [LpVariable('y%d' % i, cat=LpBinary) for i in self.df_v_s.index]
        self.D_u = LpVariable('D_u', cat=LpInteger)
        self.D_s = LpVariable('D_s', cat=LpInteger)

        # objective function
        m += 2 * self.D_u + self.D_s

        # constraints
        m = self.create_constraints(m)

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
            self.df_e_u.variable = self.df_e_u.variable.apply(value)
            # print(self.df_e_u[self.df_e_u.variable >= 1])
        else:
            print('status code is = ', m.status)

    def create_constraints(self, m):
        # constraints
        # (1b)
        for k, v in self.df_e_u.groupby('user'):
            m += lpSum(v.variable) == 1

        # (1c)
        for k, v in self.df_e_u.groupby('server'):
            m += lpSum(v.variable) <= self.df_v_s['capacity'][k]

        # (1d)
        for k, v in self.df_e_u.iterrows():
            m += v.variable * v.delay <= self.D_u

        # (1e)
        for k, v in self.df_e_s.iterrows():
            m += v.variable * v.delay <= self.D_s

        # (1f)
        for k, v in self.df_e_u.groupby('user'):
            for l, w in self.df_v_s.iterrows():
                m += w.variable >= v.variable

        # (1g)
        for k, v in self.df_e_s.iterrows():
            m += self.df_v_s.iloc[v.server_1].variable + \
                self.df_v_s.iloc[v.server_2].variable - 1 <= v.variable

        # (1h)
        for k, v in self.df_e_s.iterrows():
            m += v.variable <= self.df_v_s.iloc[v.server_1].variable

        # (1i)
        for k, v in self.df_e_s.iterrows():
            m += v.variable <= self.df_v_s.iloc[v.server_2].variable

        return m


def main():

    # create input
    problem = Problem(1)

    # solve by ilp
    problem .solve_by_ilp()


if __name__ == '__main__':
    main()
