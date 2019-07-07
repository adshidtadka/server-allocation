import time
import csv
import os
import slackweb

import Constant
from Parameter import Parameter
from Mmd import Mmd


class Result:

    def __init__(self, var_name):
        self.var_name = var_name
        self.const_names = ['user', 'server', 'capacity']
        self.is_execute = self.is_execute()
        if self.is_execute:
            self.var_range = Result.set_range(Constant.get_range(var_name))
            self.consts = self.set_consts()

    def is_execute(self):
        print("Do you execute " + self.var_name + " simulator? [y/N]", end=' > ')
        if input() == 'y':
            return True
        else:
            return False

    def set_range(var_range_def):
        print("Please set range [start stop step]", end=' > ')
        try:
            x, y, z = map(int, input().split())
            return range(x, y, z)
        except:
            print(str(var_range_def) + ' set.')
            return var_range_def

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
        message = '\nGet result of ' + self.var_name + ' with ' + str(self.consts)
        Result.post_to_slack(message)

        results = []
        for i in self.var_range:
            average_result = [i, self.get_average(i)]
            Result.post_to_slack(str(average_result))
            results.append(average_result)
        f = open('result/' + self.var_name + str(self.consts) + '.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(results)
        f.close()

    def get_average(self, var):
        iterated_result = []
        for i in range(Constant.ITERATION_NUM):
            # create param
            param = Parameter(Constant.SEED + i)
            param.set_param(self.var_name, self.consts, var)
            param.create_input()

            # solve by algorithm
            mmd = Mmd(param)
            cpu_time_mmd = mmd.start_algorithm(param)
            iterated_result.append(cpu_time_mmd)
        return sum(iterated_result) / len(iterated_result)

    def post_to_slack(text):
        print(text)
        slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
        slack.notify(text=text)


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
