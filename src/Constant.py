import sys


class Constant:
    SEED = 1
    INF = 999999999
    ITERATION_NUM = 5

    def get_range(self, variable):
        if variable == 'user':
            return range(10, 100, 10)
        elif variable == 'server':
            return range(10, 20, 1)
        elif variable == 'capacity':
            return range(10, 20, 1)


sys.modules[__name__] = Constant()
