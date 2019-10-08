import time
import csv
import os
import slackweb
import configparser

import Constant
from Parameter import Parameter
from Sum import Sum
from Esum import Esum
from Ilp import Ilp


class Result:

    def __init__(self, var_name):
        print()
        self.var_name = var_name
        self.const_names = ['user', 'server', 'capacity']
        self.execute = self.is_execute()
        if self.execute:
            self.var_range = Result.get_range(Constant.get_range(var_name))
            self.consts = self.get_consts()
            self.iter_num = self.get_iteration_num()
            self.ilp = self.execute_ilp()
            if self.ilp:
                self.solver = self.select_solver()

    def is_execute(self):
        print("Do you execute " + self.var_name + " simulator? [y/N]", end=' > ')
        if input() == 'y':
            return True
        else:
            return False

    def select_solver(self):
        print("Which solver do you use? [1:GLPK, 2:SCIP, 3:CPLEX]", end=' > ')
        solver = input()
        if solver == '1':
            return 1
        elif solver == '2':
            return 2
        elif solver == '3':
            return 3
        else:
            return False

    def execute_ilp(self):
        print("Do you execute ilp? [y/N]", end=' > ')
        if input() == 'y':
            return True
        else:
            return False

    def get_range(var_range_def):
        print("Please set range [start stop step]", end=' > ')
        try:
            x, y, z = map(int, input().split())
            return range(x, y, z)
        except:
            print(str(var_range_def) + ' set.')
            return var_range_def

    def get_consts(self):
        self.const_names.remove(self.var_name)
        consts = dict()
        for const_name in self.const_names:
            print("Please set " + const_name + ".", end=' > ')
            try:
                consts[const_name] = int(input())
            except:
                f = Parameter.get_const(const_name)
                print(str(f) + ' set.')
                consts[const_name] = f
        return consts

    def get_iteration_num(self):
        print("Please set iteration number.", end=' > ')
        try:
            return int(input())
        except:
            print(str(Constant.ITERATION_NUM) + ' set.')
            return Constant.ITERATION_NUM

    def rotate_file_name(file_name):
        file_index = 1
        while os.path.exists(file_name + '_' + str(file_index) + '.csv'):
            file_index += 1
        return file_name + '_' + str(file_index) + '.csv'

    def get_result(self):
        message = '\nGet result for {' + self.var_name + ': ' + str(self.var_range) + '} with ' + str(self.consts)
        Result.post_to_slack(message)
        file_name = Result.rotate_file_name('../result/' + self.var_name + str(self.consts))

        for var in self.var_range:
            average_result_str = self.get_average(var)
            Result.post_to_slack(average_result_str + ' for {' + self.var_name + ': ' + str(var) + '} and ' + str(self.consts))
            f = open(file_name, 'a')
            f.write(str(var) + ',' + average_result_str + '\n')
            f.close()

    def get_average(self, var):
        iterated_result_ilp = []
        iterated_result_sum = []
        iterated_result_esum = []
        for i in range(self.iter_num):
            # create param
            param = Parameter(Constant.SEED + i)
            param.set_param(self.var_name, self.consts, var)
            param.create_input()

            # solve by ilp
            if self.ilp:
                ilp = Ilp(param)
                cpu_time_ilp = ilp.solve_by_ilp(self.solver)
                iterated_result_ilp.append(cpu_time_ilp)

            # solve by esum
            esum = Esum(param)
            cpu_time_esum = esum.start_algo(param)
            iterated_result_esum.append(cpu_time_esum)
        result = []
        if self.ilp:
            result.append(sum(iterated_result_ilp) / len(iterated_result_ilp))
        result.append(sum(iterated_result_esum) / len(iterated_result_esum))
        return ",".join(map(str, result))

    def post_to_slack(text):
        print(text)

        config = configparser.ConfigParser()
        config.read("../config.ini")
        slack = slackweb.Slack(url=config.get("general", "slack_webhook"))
        slack.notify(text=text)


if not os.path.exists('../result'):
    os.mkdir('../result')

# result_user = Result('user')
# result_server = Result('server')
result_capacity = Result('capacity')

# if result_user.execute:
#     result_user.get_result()

# if result_server.execute:
#     result_server.get_result()

if result_capacity.execute:
    result_capacity.get_result()
