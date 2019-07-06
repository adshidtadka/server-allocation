import sys


class Constant:
    SEED = 1
    INF = 999999999
    USER_RANGE = range(100, 500, 50)
    SERVER_RANGE = range(10, 20, 1)
    CAPACITY_RANGE = range(50, 100, 10)


sys.modules[__name__] = Constant()
