# ilp approach
# transport optimization

# %%
import numpy as np
import pandas as pd
from itertools import product
from pulp import *

# %%
np.random.seed(1)


# %%
# given parameter
user_num = 800
server_num = 8
delay_max = 30
delay_serer = 1
capacity_max = 400

e_u = list(product(range(user_num), range(server_num)))
e_s = list(itertools.combinations(list(range(0, server_num)), 2))
d_us = np.random.randint(0, delay_max, (user_num, server_num))
v_s = list(range(0, server_num))
m_s = np.random.randint(0, capacity_max, server_num)
e_s

# %%
# dataframe for E_U
df_e_u = pd.DataFrame([(i, j) for i, j in e_u], columns=['user', 'server'])
df_e_u['delay'] = d_us.flatten()
df_e_u

# %%
# dataframe for E_S
df_e_s = pd.DataFrame([(i, j) for i, j in e_s],
                      columns=['server_1', 'server_2'])
df_e_s['delay'] = delay_serer
df_e_s

# %%
# dataframe for V_S
df_v_s = pd.DataFrame(v_s, columns=['server'])
df_v_s['capacity'] = m_s
df_v_s

# %%
# optimization problem
m = LpProblem()

# decision variables
df_e_u['variable'] = [LpVariable('x_us%d' % i, cat=LpBinary)
                      for i in df_e_u.index]
df_e_s['variable'] = [LpVariable('x_st%d' % i, cat=LpBinary)
                      for i in df_e_s.index]
df_v_s['variable'] = [LpVariable('y%d' % i, cat=LpBinary)
                      for i in df_v_s.index]
D_u = LpVariable('D_u', cat=LpInteger)
D_s = LpVariable('D_s', cat=LpInteger)

# %%
# objective function
m += 2 * D_u + D_s

# %%
# constraints
# (1b)
for k, v in df_e_u.groupby('user'):
    m += lpSum(v.variable) == 1


# (1c)
for k, v in df_e_u.groupby('server'):
    m += lpSum(v.variable) <= df_v_s['capacity'][k]

# (1d)
for k, v in df_e_u.iterrows():
    m += v.variable * v.delay <= D_u

# (1e)
for k, v in df_e_s.iterrows():
    m += v.variable * v.delay <= D_s

# (1f)
for k, v in df_e_u.groupby('user'):
    for l, w in df_v_s.iterrows():
        m += w.variable >= v.variable

# (1g)
for k, v in df_e_s.iterrows():
    m += df_v_s.iloc[v.server_1].variable + \
        df_v_s.iloc[v.server_2].variable - 1 <= v.variable

# (1h)
for k, v in df_e_s.iterrows():
    m += v.variable <= df_v_s.iloc[v.server_1].variable

# (1i)
for k, v in df_e_s.iterrows():
    m += v.variable <= df_v_s.iloc[v.server_2].variable

# %%
# solve
m.solve()


# %%
# result
df_e_u.variable = df_e_u.variable.apply(value)
df_e_u[df_e_u.variable >= 1]
# %%
