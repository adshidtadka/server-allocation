import sys


class Constant:
    SEED = 1


sys.modules[__name__] = Constant()
