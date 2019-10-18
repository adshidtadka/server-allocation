import time
import csv
import os
import slackweb
import configparser
import collections

import Constant
from Parameter import Parameter
from Sum import Sum
from Esum import Esum
from Ilp import Ilp
from Method import Method


class Result:

    def __init__(self, var_name):
        print()
        self.var_name = var_name
        self.const_names = ['user', 'server', 'capacity']
        self.is_execute_simulator = self.is_execute_simulator()
        if self.is_execute_simulator:
            self.var_range = Result.get_range(Constant.get_range(var_name))
            self.consts = self.get_consts()
            self.delay_params = self.get_delay_params()
            self.iter_num = self.get_iteration_num()
            self.methods = self.is_execute_methods()

    def is_y(self, input_str):
        if input_str == 'y':
            return True
        else:
            return False

    def is_execute_simulator(self):
        print("Do you execute " + self.var_name + " simulator? [y/N]", end=' > ')
        return self.is_y(input())

    def is_execute_methods(self):
        methods = collections.OrderedDict()
        print("Do you execute SUM? [y/N]", end=' > ')
        methods["sum"] = {"is_execute": self.is_y(input()), "is_algo": True}
        print("Do you execute ESUM? [y/N]", end=' > ')
        methods["esum"] = {"is_execute": self.is_y(input()), "is_algo": True}
        print("Do you execute GLPK? [y/N]", end=' > ')
        methods["glpk"] = {"is_execute": self.is_y(input()), "is_algo": False}
        print("Do you execute SCIP? [y/N]", end=' > ')
        methods["scip"] = {"is_execute": self.is_y(input()), "is_algo": False}
        print("Do you execute CPLEX? [y/N]", end=' > ')
        methods["cplex"] = {"is_execute": self.is_y(input()), "is_algo": False}
        return methods

    def is_execute_sum(self):
        print("Do you execute sum? [y/N]", end=" > ")
        return self.is_y(input())

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
        consts = collections.OrderedDict()
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

    def get_delay_params(self):
        delay_params = dict()
        print("Please set maximum user delay", end=" > ")
        try:
            delay_params["user_max"] = int(input())
        except:
            print(str(Parameter.DELAY_USER_MAX_CONST) + ' set.')
            delay_params["user_max"] = Parameter.DELAY_USER_MAX_CONST
        print("Please set maximum server delay", end=" > ")
        try:
            delay_params["server_max"] = int(input())
        except:
            print(str(Parameter.DELAY_SERVER_MAX_CONST) + ' set.')
            delay_params["server_max"] = Parameter.DELAY_SERVER_MAX_CONST
        return delay_params

    def rotate_file_name(file_name):
        file_index = 1
        while os.path.exists(file_name + '_' + str(file_index) + '.csv'):
            file_index += 1
        return file_name + '_' + str(file_index) + '.csv'

    def get_result(self):
        message = '\nGet result for {' + self.var_name + ': ' + str(self.var_range) + '} with ' + str(self.consts)
        Result.post_to_slack(message)
        consts = ""
        for k, v in self.consts.items():
            consts += "_" + str(k) + "_" + str(v)
        file_name = Result.rotate_file_name('../result/' + self.var_name + consts)

        for var in self.var_range:
            average_result_str = self.get_average(var)
            Result.post_to_slack(average_result_str + ' for {' + self.var_name + ': ' + str(var) + '} and ' + str(self.consts))
            f = open(file_name, 'a')
            f.write(str(var) + ',' + average_result_str + '\n')
            f.close()

    def get_average(self, var):
        # create lists
        iter_result = collections.OrderedDict()
        for k, v in self.methods.items():
            iter_result[k] = collections.OrderedDict()
            iter_result[k]["cpu_time"] = []
            if k == "sum":
                iter_result[k]["l_min"] = []
                iter_result[k]["l_max"] = []
            elif k == "esum":
                iter_result[k]["l"] = []

        # append results
        for i in range(self.iter_num):
            # create param
            param = Parameter(Constant.SEED + i)
            param.set_param(self.var_name, self.consts, var, self.delay_params)
            param.create_input()

            # solve
            for k, v in self.methods.items():
                method = Method()
                if v["is_algo"] & v["is_execute"]:
                    if k == "sum":
                        method = Sum(param)
                        method.start_algo(param)
                    elif k == "esum":
                        method = Esum(param)
                        method.start_algo(param)
                elif v["is_execute"]:
                    method = Ilp(param)
                    method.solve_by_ilp(k)
                iter_result[k]["l_min"].append(method.L_min)
                iter_result[k]["l_max"].append(method.L_max)
                iter_result[k]["l"].append(method.L)
                iter_result[k]["cpu_time"].append(method.cpu_time)

        result = []
        for k, v in self.methods.items():
            if k == "sum":
                result.append(round(sum(iter_result[k]["l_min"]) / len(iter_result[k]["l_min"])))
                result.append(round(sum(iter_result[k]["l_max"]) / len(iter_result[k]["l_max"])))
            elif k == "esum":
                result.append(round(sum(iter_result[k]["l"]) / len(iter_result[k]["l"])))
            result.append(round(sum(iter_result[k]["cpu_time"]) / len(iter_result[k]["cpu_time"]), 4))
        return ",".join(map(str, result))

    def post_to_slack(text):
        print(text)

        config = configparser.ConfigParser()
        config.read("config.ini")
        slack = slackweb.Slack(url=config.get("general", "slack_webhook"))
        slack.notify(text=Constant.MESSAGE + text)


if not os.path.exists('../result'):
    os.mkdir('../result')

print("Put a message for this simulation.", end=" > ")
Constant.MESSAGE = "[" + input() + "] "

result_user = Result('user')
result_server = Result('server')
result_capacity = Result('capacity')

if result_user.is_execute_simulator:
    result_user.get_result()

if result_server.is_execute_simulator:
    result_server.get_result()

if result_capacity.is_execute_simulator:
    result_capacity.get_result()
