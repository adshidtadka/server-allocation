import sys


class Constant:
    SEED = 1
    INF = 999999999

    def get_range(self, sim_name):
        if sim_name == 'user':
            return range(100, 500, 50)
        elif sim_name == 'server':
            return range(10, 20, 1)
        elif sim_name == 'capacity':
            return range(50, 100, 10)


sys.modules[__name__] = Constant()
