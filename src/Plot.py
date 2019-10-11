
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
ctes = 'Computation time with ESUM'
ctc = 'Computation time with CPLEX'
ctg = 'Computation time with GLPK'
ctsc = 'Computation time with SCIP'
un = 'Number of users'
sn = 'Number of servers'
cp = 'Capacity'

# %%
df_user_server_10_capacity_5 = pd.read_csv("result/user_server_10_capacity_5.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_user_server_5_capacity_10 = pd.read_csv("result/user_server_5_capacity_10.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_user_server_20_capacity_5 = pd.read_csv("result/user_server_20_capacity_5.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_user_server_20_capacity_10 = pd.read_csv("result/user_server_20_capacity_10.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_user_server_10_capacity_10 = pd.read_csv("result/user_server_10_capacity_10.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_capacity_user_25_server_5 = pd.read_csv("result/capacity_user_25_server_5.csv", names=(cp, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)

# %%
Graph.initialize_rcparams()

# %%
plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/user_server_5_capacity_10.pdf')
plt.show()
plt.close()


# %%

plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/user_server_20_capacity_5.pdf')
plt.show()
plt.close()


# %%

# %%

plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/user_server_20_capacity_10.pdf')
plt.show()
plt.close()


# %%

plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/user_server_10_capacity_10.pdf')
plt.show()
plt.close()


# %%

plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/user_server_10_capacity_5.pdf')
plt.show()
plt.close()


# %%

plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(cp + ', ' + r'$M_s$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/capacity_user_25_server_5.pdf')
plt.show()
plt.close()


# %%
