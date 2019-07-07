import time
import csv
import os

import Constant
from Parameter import Parameter
from Mmd import Mmd


class Result:

    def __init__(self, var_name):
        self.var_name = var_name
        self.const_names = ['user', 'server', 'capacity']
        self.is_execute = self.is_execute()
        if self.is_execute:
            self.sim_range = Result.set_range(Constant.get_range(var_name))
            self.consts = self.set_consts()

    def is_execute(self):
        print("Do you execute " + self.var_name + " simulator? [y/N]", end=' > ')
        if input() == 'y':
            return True
        else:
            return False

    def set_range(sim_range):
        print("Please set range [start stop step]", end=' > ')
        try:
            x, y, z = map(int, input().split())
            return range(x, y, z)
        except:
            print(str(sim_range) + ' set.')
            return sim_range

    def set_consts(self):
        self.const_names.remove(self.var_name)
        consts = dict()
        for const_name in self.const_names:
            print("Please set " + const_name + ".", end=' > ')
            try:
                const_names[const_name] = int(input())
            except:
                f = Parameter.get_const(const_name)
                print(str(f) + ' set.')
                consts[const_name] = f
        return consts

    def get_result(self):
        result = []
        for i in self.sim_range:
            average_result = self.get_average(i)
            result.append([i, average_result])
            print(result)
        f = open('result/' + self.var_name + '.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(result)
        f.close()

    def get_average(self, iterated_param):
        iterated_result = []
        for i in range(Constant.ITERATION_NUM):
            # create param
            param = Parameter(Constant.SEED + i)
            param.set_param(self.var_name, iterated_param)
            param.create_input()

            # solve by algorithm
            mmd = Mmd(param)
            cpu_time_mmd = mmd.start_algorithm(param)
            iterated_result.append(cpu_time_mmd)
        return sum(iterated_result) / len(iterated_result)


if not os.path.exists('result'):
    os.mkdir('result')

result_user = Result('user')
result_server = Result('server')
result_capacity = Result('capacity')

if result_user.is_execute:
    result_user.get_result()

if result_server.is_execute:
    result_server.get_result()

if result_capacity.is_execute:
    result_capacity.get_result()
