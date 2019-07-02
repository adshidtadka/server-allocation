import sys


class Constant:

    # constants
    USER_NUM = 800
    SERVER_NUM = 8
    DELAY_MAX = 30
    DELAY_SERVER = 1
    CAPACITY_MAX = 400
    SEED = 1


sys.modules[__name__] = Constant()
