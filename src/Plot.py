
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
un = 'User number'
sn = 'Server number'
cp = 'Capacity'

# %%
# df_user_s_10 = pd.read_csv("result/user{'server': 10, 'capacity': 50}.csv", names=(un, ct))
# df_user_s_15 = pd.read_csv("result/user{'server': 15, 'capacity': 50}.csv", names=(un, ct))
# df_user_s_20 = pd.read_csv("result/user{'server': 20, 'capacity': 50}.csv", names=(un, ct))

# %%
# df_capacity_s_10 = pd.read_csv("result/capacity{'user': 300, 'server': 10}.csv", names=(cp, ct))
# df_capacity_s_15 = pd.read_csv("result/capacity{'user': 300, 'server': 15}.csv", names=(cp, ct))
# df_capacity_s_20 = pd.read_csv("result/capacity{'user': 300, 'server': 20}.csv", names=(cp, ct))

# %%
# df_user_s_10_cplex = pd.read_csv("result/user_server_10_capacity_50_cplex.csv", names=(un, ctc, ctes))
# df_user_s_10_glpk = pd.read_csv("result/user_server_10_capacity_50_glpk.csv", names=(un, ctg, ctes))

# %%
# df_user_scip = pd.read_csv("result/user_scip.csv", names=(un, ctsc, ctes))
# df_user_cplex = pd.read_csv("result/user_cplex.csv", names=(un, ctc, ctes))
# df_user_glpk = pd.read_csv("result/user_glpk.csv", names=(un, ctg, ctes))

# %%
df_capacity_scip = pd.read_csv("result/capacity_scip.csv", names=(cp, ctsc, ctes))
df_capacity_cplex = pd.read_csv("result/capacity_cplex.csv", names=(cp, ctc, ctes))
df_capacity_glpk = pd.read_csv("result/capacity_glpk.csv", names=(cp, ctg, ctes))

# %%
Graph.initialize_rcparams()

# %%
# plt.plot(df_user_s_10[un], df_user_s_10[ct], label=(r'$|{V_{\rm S}}| = 10$'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_s_15[un], df_user_s_15[ct], label=(r'$|{V_{\rm S}}| = 15$'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_s_20[un], df_user_s_20[ct], label=(r'$|{V_{\rm S}}| = 20$'), color='k', marker='.', linestyle=':')

# plt.xticks([0, 100, 200, 300, 400])
# plt.yticks([0, 50, 100, 150, 200])
# plt.xlim((0, 400))
# plt.ylim((0, 200))

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('graph/user.pdf')
# plt.show()
# plt.close()

# %%
# plt.plot(df_capacity_s_10[cp], df_capacity_s_10[ct], label=(r'$|{V_{\rm S}}| = 10$'), color='k', marker='x', linestyle='-')
# plt.plot(df_capacity_s_15[cp], df_capacity_s_15[ct], label=(r'$|{V_{\rm S}}| = 15$'), color='k', marker='^', linestyle='--')
# plt.plot(df_capacity_s_20[cp], df_capacity_s_20[ct], label=(r'$|{V_{\rm S}}| = 20$'), color='k', marker='.', linestyle=':')

# plt.xticks([30, 40, 50, 60, 70])
# plt.yticks([0, 50, 100, 150, 200])
# plt.xlim((30, 70))
# plt.ylim((0, 200))

# plt.xlabel(cp + ', ' + r'$M_s$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('graph/capacity.pdf')
# plt.show()
# plt.close()

# # %%
# plt.plot(df_user_scip[un], df_user_scip[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_glpk[un], df_user_glpk[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_user_scip[un], df_user_scip[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_cplex[un], df_user_cplex[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('graph/user_solver.pdf')
# plt.show()
# plt.close()

# %%
plt.plot(df_capacity_scip[cp], df_capacity_scip[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_capacity_glpk[cp], df_capacity_glpk[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_capacity_scip[cp], df_capacity_scip[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_capacity_cplex[cp], df_capacity_cplex[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(cp + ', ' + r'$M_s$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('graph/capacity_solver.pdf')
plt.show()
plt.close()


#%%
