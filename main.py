import time
import csv
import os

import Constant
from Parameter import Parameter
from Mmd import Mmd

if not os.path.exists('result'):
    os.mkdir('result')

# check whether execute 1: user, 2: server, 3: capacity
print("Do you execute 1: user simulator? [y/n]:", end=' ')
if input() == 'y':
    is_user = True
else:
    is_user = False

print("Do you execute 2: server simulator? [y/n]:", end=' ')
if input() == 'y':
    is_server = True
else:
    is_server = False

print("Do you execute 3: capacity simulator? [y/n]:", end=' ')
if input() == 'y':
    is_capacity = True
else:
    is_capacity = False


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
