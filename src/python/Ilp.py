import numpy as np
import pandas as pd
import time
from pulp import *

import Constant
from Parameter import Parameter
from Method import Method


class Ilp(Method):
    def __init__(self, param):
        self.create_dataframe(param)
        self.set_input()

    def set_input(self):
        # optimization problem
        problem = LpProblem()

        # decision variables
        self.df_e_u['variable'] = [LpVariable('x_us_%d' % i, cat=LpBinary) for i in self.df_e_u.index]
        self.df_e_s['variable'] = [LpVariable('x_st_%d' % i, cat=LpBinary) for i in self.df_e_s.index]
        self.df_v_s['variable'] = [LpVariable('y_%d' % i, cat=LpBinary) for i in self.df_v_s.index]
        self.D_u = LpVariable('D_u', cat=LpInteger)
        self.D_s = LpVariable('D_s', cat=LpInteger)

        # objective function
        problem += 2 * self.D_u + self.D_s

        self.problem = problem

    def create_dataframe(self, param):
        # dataframe for E_U
        df_e_u = pd.DataFrame([(i, j) for i, j in param.e_u], columns=['user', 'server'])
        df_e_u['delay'] = param.d_us.flatten()
        self.df_e_u = df_e_u

        # dataframe for E_S
        df_e_s = pd.DataFrame([(i, j) for i, j in param.e_s], columns=['server_1', 'server_2'])
        df_e_s['delay'] = param.d_st
        self.df_e_s = df_e_s

        # dataframe for V_S
        df_v_s = pd.DataFrame(list(range(0, param.SERVER_NUM)), columns=['server'])
        df_v_s['capacity'] = param.m_s
        self.df_v_s = df_v_s

    def solve_by_ilp(self, solver=None):
        t_0 = time.process_time()
        # solve
        try:
            # constraints
            self.problem = self.create_constraints(self.problem)
            if solver == "scip":
                self.problem.solve(pulp.SCIP(msg=0))
            elif solver == "cplex":
                self.problem.solve(pulp.CPLEX_CMD(msg=0))
            else:
                self.problem.solve(pulp.GLPK_CMD(msg=0))

        except PulpSolverError:
            print('Solver is not installed or there is no feasible solution.')
            return 0

        t_1 = time.process_time()
        self.cpu_time = t_1 - t_0

    def print_result(self):
        if self.problem.status == 1:
            print('objective function is ', value(self.problem.objective))
            print('cpu time is ' + str(self.cpu_time) + ' sec')
        else:
            print('status code is ', self.problem.status)

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
        for k, v in self.df_e_u.iterrows():
            m += self.df_v_s.at[v.server, "variable"] >= v.variable

        # (1g)
        for k, v in self.df_e_s.iterrows():
            m += self.df_v_s.iloc[v.server_1].variable + self.df_v_s.iloc[v.server_2].variable - 1 <= v.variable

        # (1h)
        for k, v in self.df_e_s.iterrows():
            m += v.variable <= self.df_v_s.iloc[v.server_1].variable

        # (1i)
        for k, v in self.df_e_s.iterrows():
            m += v.variable <= self.df_v_s.iloc[v.server_2].variable

        return m


def main():
    # create param
    param = Parameter(Constant.SEED)
    param.create_input()

    # set input to problem
    ilp = Ilp(param)

    # solve by ilp
    ilp.solve_by_ilp("cplex")

    # print result
    ilp.print_result()


if __name__ == '__main__':
    main()
