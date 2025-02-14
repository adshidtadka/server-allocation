import sys


class Constant:
    SEED = 1
    INF = 999999999
    ITERATION_NUM = 50

    def get_range(self, variable):
        if variable == 'user':
            return range(10, 50, 5)
        elif variable == 'server':
            return range(5, 25, 2)
        elif variable == 'capacity':
            return range(5, 15, 1)


sys.modules[__name__] = Constant()
