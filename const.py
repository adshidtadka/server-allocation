import sys


class _const:
    user_num = 800
    server_num = 8
    delay_max = 30
    delay_serer = 1
    capacity_max = 400


sys.modules[__name__] = _const()
