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


if not os.path.exists('result'):
    os.mkdir('result')

sim_user = Result('user')
sim_server = Result('server')
sim_capacity = Result('capacity')

if sim_user.is_execute:
    result_user = []
    for i in range(100, 500, 50):
        # create param
        param = Parameter(Constant.SEED)
        param.set_user_num(i)
        param.create_input()

        # solve by algorithm
        mmd = Mmd(param)
        cpu_time_mmd = mmd.start_algorithm(param)

        result_user.append([param.USER_NUM, param.SERVER_NUM, param.CAPACITY, cpu_time_mmd])
        print(result_user)
    f = open('result/user.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(result_user)
    f.close()

if sim_server.is_execute:
    result_server = []
    for i in range(10, 20, 1):
        param = Parameter(Constant.SEED)
        param.set_server_num(i)
        param.create_input()

        # solve by algorithm
        mmd = Mmd(param)
        cpu_time_mmd = mmd.start_algorithm(param)

        result_user.append([param.USER_NUM, param.SERVER_NUM, param.CAPACITY, cpu_time_mmd])
        print(result_server)
    f = open('result/server.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(result_server)
    f.close()

if sim_capacity.is_execute:
    result_capacity = []
    for i in range(50, 100, 10):
        param = Parameter(Constant.SEED)
        param.set_capacity(i)
        param.create_input()

        # solve by algorithm
        mmd = Mmd(param)
        cpu_time_mmd = mmd.start_algorithm(param)

        result_user.append([param.USER_NUM, param.SERVER_NUM, param.CAPACITY, cpu_time_mmd])
        print(result_capacity)
    f = open('result/capacity.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(result_capacity)
    f.close()
