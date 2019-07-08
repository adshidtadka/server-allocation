
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%


class Graph:
    def initialize_rcparams():
        plt.clf()
        plt.style.use('default')
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.gca().yaxis.set_ticks_position('left')
        plt.gca().xaxis.set_ticks_position('bottom')
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['font.weight'] = 'light'
        plt.rcParams['font.size'] = 18
        plt.rcParams['axes.linewidth'] = 0.8
        plt.rcParams['lines.linewidth'] = 3
        plt.rcParams['lines.marker'] = '.'
        plt.rcParams['lines.markersize'] = 8
        plt.rcParams['legend.borderaxespad'] = 0
        plt.rcParams['legend.frameon'] = False
        plt.rcParams['legend.numpoints'] = 1
        plt.rcParams['legend.labelspacing'] = 0.1
        plt.rcParams['savefig.bbox'] = 'tight'
        plt.rc('text', usetex=True)


# %%
ct = 'Computation time'
un = 'User number'
sn = 'Server number'
cp = 'Capacity'

# %%
df_user_s_10 = pd.read_csv("result/user{'server': 10, 'capacity': 50}.csv", names=(un, ct))
df_user_s_15 = pd.read_csv("result/user{'server': 15, 'capacity': 50}.csv", names=(un, ct))
df_user_s_20 = pd.read_csv("result/user{'server': 20, 'capacity': 50}.csv", names=(un, ct))

# %%
Graph.initialize_rcparams()

# %%
plt.plot(df_user_s_10[un], df_user_s_10[ct], label=(r'${\rm V_{\rm S}} = 10$'), color='k', marker='x', linestyle='-')
plt.plot(df_user_s_15[un], df_user_s_15[ct], label=(r'${\rm V_{\rm S}} = 15$'), color='k', marker='^', linestyle='--')
plt.plot(df_user_s_20[un], df_user_s_20[ct], label=(r'${\rm V_{\rm S}} = 20$'), color='k', marker='.', linestyle=':')

plt.xticks([0, 100, 200, 300, 400, 500])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70])
plt.xlim((0, 500))
plt.ylim((0, 70))

plt.xlabel(un)
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/user.pdf')
plt.show()
plt.close()


# %%
