import time
import csv
import os

import Constant
from Parameter import Parameter
from Mmd import Mmd


class Result:
    def __init__(self, sim_name):
        self.sim_name = sim_name
        self.is_execute = self.check_execution()
        if self.is_execute:
            self.sim_range = Result.check_range(Constant.get_range(sim_name))

    def check_execution(self):
        print("Do you execute " + self.sim_name + " simulator? [y/N]", end=' > ')
        if input() == 'y':
            return True
        else:
            return False

    def check_range(sim_range):
        print("Please set range [start stop step]", end=' > ')
        try:
            x, y, z = map(int, input().split())
            print(str(range(x, y, z)) + ' set.')
            return range(x, y, z)
        except:
            print(str(sim_range) + ' set.')
            return sim_range

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

sim_user = Result('user')
sim_server = Result('server')
sim_capacity = Result('capacity')

if sim_user.is_execute:
    sim_user.get_result()

if sim_server.is_execute:
    sim_server.get_result()

if sim_capacity.is_execute:
    sim_capacity.get_result()
