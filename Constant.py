import sys


class Constant:
    SEED = 1
    INF = 999999999
    ITERATION_NUM = 50

    def get_range(self, variable):
        if variable == 'user':
            return range(100, 500, 50)
        elif variable == 'server':
            return range(10, 20, 1)
        elif variable == 'capacity':
            return range(50, 100, 10)


sys.modules[__name__] = Constant()
