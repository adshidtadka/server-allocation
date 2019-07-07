import time
import csv
import os

import Constant
from Parameter import Parameter
from Mmd import Mmd


class Result:

    def __init__(self, sim_name):
        self.sim_name = sim_name
        self.sim_names = ['user', 'server', 'capacity']
        self.is_execute = self.is_execute()
        if self.is_execute:
            self.sim_range = Result.set_range(Constant.get_range(sim_name))
            self.fixed_params = self.set_fixed_param()

    def is_execute(self):
        print("Do you execute " + self.sim_name + " simulator? [y/N]", end=' > ')
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

    def set_fixed_param(self):
        self.sim_names.remove(self.sim_name)
        fixed_params = dict()
        for sim_name in self.sim_names:
            print("Please set " + sim_name + ".", end=' > ')
            try:
                fixed_params[sim_name] = int(input())
            except:
                f = Parameter.get_fixed_param(sim_name)
                print(str(f) + ' set.')
                fixed_params[sim_name] = f
        return fixed_params

    def get_result(self):
        result = []
        for i in self.sim_range:
            average_result = self.get_average(i)
            result.append([i, average_result])
            print(result)
        f = open('result/' + self.sim_name + '.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(result)
        f.close()

    def get_average(self, iterated_param):
        iterated_result = []
        for i in range(Constant.ITERATION_NUM):
            # create param
            param = Parameter(Constant.SEED + i)
            param.set_param(self.sim_name, iterated_param)
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
