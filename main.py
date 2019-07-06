import time
import csv
import os

import Constant
from Parameter import Parameter
from Mmd import Mmd

if not os.path.exists('result'):
    os.mkdir('result')


class GetResult:
    def check_execution(sim_name):
        print("Do you execute " + sim_name + " simulator? [y/N]", end=' > ')
        if input() == 'y':
            return True
        else:
            return False

    def check_range(sim_range):
        print("Please set range [start stop step]", end=' > ')
        try:
            x, y, z = map(int, input().split())
            return range(x, y, z)
        except:
            print(str(sim_range) + ' set.')
            return sim_range


# check execution and range
is_user = GetResult.check_execution("user")
if is_user:
    user_range = GetResult.check_range(Constant.USER_RANGE)

is_server = GetResult.check_execution("server")
if is_server:
    server_range = GetResult.check_range(Constant.SERVER_RANGE)

is_capacity = GetResult.check_execution("capacity")
if is_capacity:
    capacity_range = GetResult.check_range(Constant.CAPACITY_RANGE)

if is_user:
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

if is_server:
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

if is_capacity:
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
