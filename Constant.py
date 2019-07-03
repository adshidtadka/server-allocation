import sys


class Constant:
    SEED = 1
    INF = 999999999


sys.modules[__name__] = Constant()
