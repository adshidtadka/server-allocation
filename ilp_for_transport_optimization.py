# ilp approach
# transport optimization

# %%
import numpy as np
import pandas as pd
from itertools import product
from pulp import *


# %%
np.random.seed(1)
nw, nf = 3, 4
pr = list(product(range(nw), range(nf)))
pr
# %%
supply = np.random.randint(30, 50, nw)
supply


# %%
demand = np.random.randint(20, 40, nf)
demand

# %%
cost = np.random.randint(10, 20, (nw, nf))
cost

# %%
# 表を作成
a = pd.DataFrame([(i, j) for i, j in pr], columns=['倉庫', '工場'])
a

# %%
a['cost'] = cost.flatten()
a

# %%
# 数理モデルの作成
m = LpProblem()
a['variable'] = [LpVariable('v%d' % i, lowBound=0) for i in a.index]
a

# %%
# 目的関数: 輸送コスト
m += lpDot(a.cost, a.variable)
# %%
for k, v in a.groupby('倉庫'):
    m += lpSum(v.variable) <= supply[k]
for k, v in a.groupby('工場'):
    m += lpSum(v.variable) >= demand[k]

# %%
m.solve()

# %%
a['value'] = a.variable.apply(value)
a[a.value > 0]

# %%
