import numpy as np
import pandas as pd
import time
from pulp import *

import Constant
from Parameter import Parameter


class Ilp:
    def __init__(self, param):
        self.set_input(param)

    def set_input(self, param):
        # optimization problem
        problem = LpProblem()

        # decision variables
        param.df_e_u['variable'] = [LpVariable('x_us%d' % i, cat=LpBinary) for i in param.df_e_u.index]
        param.df_e_s['variable'] = [LpVariable('x_st%d' % i, cat=LpBinary) for i in param.df_e_s.index]
        param.df_v_s['variable'] = [LpVariable('y%d' % i, cat=LpBinary) for i in param.df_v_s.index]
        param.D_u = LpVariable('D_u', cat=LpInteger)
        param.D_s = LpVariable('D_s', cat=LpInteger)

        # objective function
        problem += 2 * param.D_u + param.D_s

        # constraints
        problem = Ilp.create_constraints(param, problem)

        self.problem = problem

    def solve_by_ilp(self):
        # solve
        try:
            print('-------- t_0 --------')
            t_0 = time.process_time()
            self.problem.solve(CPLEX_CMD(msg=1))
            t_1 = time.process_time()
            print('\n-------- t_1 --------')

            print('\nt_1 - t_0 is ', t_1 - t_0, '\n')
        except PulpSolverError:
            print(CPLEX_CMD().path, 'is not installed')

    def print_result(self):
        if self.problem.status == 1:
            print('objective function is ', value(self.problem.objective))
        else:
            print('status code is ', self.problem.status)

    def create_constraints(param, m):
        # constraints
        # (1b)
        for k, v in param.df_e_u.groupby('user'):
            m += lpSum(v.variable) == 1

        # (1c)
        for k, v in param.df_e_u.groupby('server'):
            m += lpSum(v.variable) <= param.df_v_s['capacity'][k]

        # (1d)
        for k, v in param.df_e_u.iterrows():
            m += v.variable * v.delay <= param.D_u

        # (1e)
        for k, v in param.df_e_s.iterrows():
            m += v.variable * v.delay <= param.D_s

        # (1f)
        for k, v in param.df_e_u.groupby('user'):
            for l, w in param.df_v_s.iterrows():
                m += w.variable >= v.variable

        # (1g)
        for k, v in param.df_e_s.iterrows():
            m += param.df_v_s.iloc[v.server_1].variable + \
                param.df_v_s.iloc[v.server_2].variable - 1 <= v.variable

        # (1h)
        for k, v in param.df_e_s.iterrows():
            m += v.variable <= param.df_v_s.iloc[v.server_1].variable

        # (1i)
        for k, v in param.df_e_s.iterrows():
            m += v.variable <= param.df_v_s.iloc[v.server_2].variable

        return m


def main():

    param = Parameter(Constant.SEED)

    # set input to problem
    ilp = Ilp(param)

    # solve by ilp
    ilp.solve_by_ilp()

    # print result
    ilp.print_result()


if __name__ == '__main__':
    main()
