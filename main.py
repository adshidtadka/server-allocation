import time
import csv

import Constant
from Parameter import Parameter
from HopcroftKarp import HopcroftKarp
from Ilp import Ilp
from Mmd import Mmd

result_user_num = []
for i in range(100, 500, 50):
    # create param
    param = Parameter(Constant.SEED)
    param.set_user_num(i)
    param.create_input()

    # solve by ilp
    ilp = Ilp(param)
    cpu_time_ilp = ilp.solve_by_ilp()

    # solve by algorithm
    mmd = Mmd(param)
    cpu_time_mmd = mmd.start_algorithm(param)

    result_user_num.append([cpu_time_ilp, cpu_time_mmd])
    print(result_user_num)
f = open('result_user_num.csv', 'w')
writer = csv.writter(f, lineterminator='\n')
writer.writerows(result_user_num)
f.close()

result_server_num = []
for i in range(10, 100, 10):
    param = Parameter(Constant.SEED)
    param.set_server_num(i)
    param.create_input()

    # solve by ilp
    ilp = Ilp(param)
    cpu_time_ilp = ilp.solve_by_ilp()

    # solve by algorithm
    mmd = Mmd(param)
    cpu_time_mmd = mmd.start_algorithm(param)

    result_server_num.append([cpu_time_ilp, cpu_time_mmd])
    print(result_server_num)
f = open('result_server_num.csv', 'w')
writer = csv.writter(f, lineterminator='\n')
writer.writerows(result_server_num)
f.close()

result_capacity = []
for i in range(50, 100, 5):
    param = Parameter(Constant.SEED)
    param.set_capacity(i)
    param.create_input()

    # solve by ilp
    ilp = Ilp(param)
    cpu_time_ilp = ilp.solve_by_ilp()

    # solve by algorithm
    mmd = Mmd(param)
    cpu_time_mmd = mmd.start_algorithm(param)

    result_capacity.append([cpu_time_ilp, cpu_time_mmd])
    print(result_capacity)
f = open('result_capacity.csv', 'w')
writer = csv.writter(f, lineterminator='\n')
writer.writerows(result_capacity)
f.close()
