
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
cts = 'Computation time with SUM'
ctes = 'Computation time with ESUM'
ctc = 'Computation time with CPLEX'
ctg = 'Computation time with GLPK'
ctsc = 'Computation time with SCIP'
td = 'Total delay'
tds_max = 'Total maximum delay with SUM'
tds_min = 'Total minimum delay with SUM'
tdes = 'Total delay with SUM'
un = 'Number of users'
sn = 'Number of servers'
cp = 'Capacity'

# %%

df_user_50_cap_10 = pd.read_csv("../result/user_50_cap_10.csv", names=(un, tds_min, tds_max, cts, tdes, ctes, ctc)).replace(0.0, np.nan)
df_user_100_cap_15 = pd.read_csv("../result/user_100_cap_15.csv", names=(un, tds_min, tds_max, cts, tdes, ctes, ctc)).replace(0.0, np.nan)
df_cap_20_user_20 = pd.read_csv("../result/cap_20_user_20.csv", names=(cp, tds_min, tds_max, cts, tdes, ctes, ctc)).replace(0.0, np.nan)
df_cap_40_user_40 = pd.read_csv("../result/cap_40_user_40.csv", names=(cp, tds_min, tds_max, cts, tdes, ctes, ctc)).replace(0.0, np.nan)
df_user_10_cap_5 = pd.read_csv("../result/user_10_cap_5.csv", names=(un, tds_min, tds_max, cts, tdes, ctes, ctc)).replace(0.0, np.nan)

# %%
rate_seriese = pd.concat([df_user_50_cap_10[ctes] / df_user_50_cap_10[ctc], df_user_100_cap_15[ctes] / df_user_100_cap_15[ctc]])
rate_seriese.mean()

# %%
Graph.initialize_rcparams()

# %%

plt.plot(df_user_10_cap_5[un], df_user_10_cap_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_10_cap_5[un], df_user_10_cap_5[cts], label=('SUM'), color='k', marker='o', linestyle='--')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.ylim([-0.02, 0.2])

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_10_cap_5.pdf')
plt.show()
plt.close()

# %%

plt.plot(df_user_10_cap_5[un], df_user_10_cap_5[tdes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_10_cap_5[un], df_user_10_cap_5[tds_max], label=('SUM (upper-bound)'), color='k', marker='o', linestyle='--')
plt.plot(df_user_10_cap_5[un], df_user_10_cap_5[tds_min], label=('SUM (lower-bound)'), color='k', marker='^', linestyle='-.')


plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(td)

plt.ylim([50, 250])

plt.legend(loc="lower right")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/delay_user_10_cap_5.pdf')
plt.show()
plt.close()

# %%

plt.plot(df_user_50_cap_10[un], df_user_50_cap_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_50_cap_10[un], df_user_50_cap_10[ctc], label=('ILP'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.ylim([0, 0.12])

plt.legend(loc="upper left")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_50_cap_10.pdf')
plt.show()
plt.close()


# %%

plt.plot(df_user_100_cap_15[un], df_user_100_cap_15[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_user_100_cap_15[un], df_user_100_cap_15[ctc], label=('ILP'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.ylim([0, 0.2])

plt.legend(loc="upper left")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_100_cap_15.pdf')
plt.show()
plt.close()

# %%

plt.plot(df_cap_20_user_20[cp], df_cap_20_user_20[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_cap_20_user_20[cp], df_cap_20_user_20[ctc], label=('ILP'), color='k', marker='o', linestyle=':')

plt.xlabel(cp + ', ' + r'$M_s$')
plt.ylabel(ct + ' [s]')

plt.ylim([0, 0.1])

plt.legend(loc="upper left")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/cap_20_user_20.pdf')
plt.show()
plt.close()


# %%

plt.plot(df_cap_40_user_40[cp], df_cap_40_user_40[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_cap_40_user_40[cp], df_cap_40_user_40[ctc], label=('ILP'), color='k', marker='o', linestyle=':')

plt.xlabel(cp + ', ' + r'$M_s$')
plt.ylabel(ct + ' [s]')

plt.ylim([0, 0.175])

plt.legend(loc="upper left")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/cap_40_user_40.pdf')
plt.show()
plt.close()


# %%
