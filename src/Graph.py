
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
        plt.rcParams['legend.fontsize'] = 20
        plt.rcParams['legend.borderaxespad'] = 0
        plt.rcParams['legend.frameon'] = False
        plt.rcParams['legend.numpoints'] = 1
        plt.rcParams['legend.labelspacing'] = 0.1
        plt.rcParams['savefig.bbox'] = 'tight'


# %%
ct = 'Cpu time'
un = 'User number'
sn = 'Server number'
cp = 'Capacity'

# %%
df_user = pd.read_csv("result/user{'server': 10, 'capacity': 50}.csv", names=(un, ct))
df_server = pd.read_csv("result/server{'user': 500, 'capacity': 50}.csv", names=(sn, ct))
df_capacity = pd.read_csv("result/capacity{'user': 500, 'server': 10}.csv", names=(cp, ct))

# %%
Graph.initialize_rcparams()

# %%
plt.plot(df_user[un], df_user[ct], color='k')
plt.xlabel(un)
plt.ylabel(ct + ' [s]')
plt.savefig('graph/user.pdf')
plt.show()
plt.close()

# %%
Graph.initialize_rcparams()

# %%
plt.plot(df_server[sn], df_server[ct], color='k')
plt.xlabel(sn)
plt.ylabel(ct + ' [s]')
plt.savefig('graph/server.pdf')
plt.show()
plt.close()


# %%
Graph.initialize_rcparams()

# %%
plt.plot(df_capacity[cp], df_capacity[ct], color='k')
plt.xlabel(cp)
plt.ylabel(ct + ' [s]')
plt.savefig('graph/capacity.pdf')
plt.show()
plt.close()


# %%
