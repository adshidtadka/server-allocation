# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_user = pd.read_csv("result/user{'server': 10, 'capacity': 50}.csv", names=('User num', 'Cpu time'))
df_user

# %%
plt.clf()
plt.style.use('default')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'light'
plt.rcParams['font.size'] = 22
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['legend.borderaxespad'] = 0
plt.rcParams['legend.frameon'] = False
plt.rcParams['legend.numpoints'] = 1
plt.rcParams['legend.labelspacing'] = 0.1
plt.rcParams['savefig.bbox'] = 'tight'

# %%
plt.plot(df_user['User num'], df_user['Cpu time'])
plt.legend(loc="upper left")
plt.savefig('graph/user.pdf')
plt.show()
plt.close()


# %%
