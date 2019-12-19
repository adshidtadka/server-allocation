
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
# df_user_server_10_capacity_5 = pd.read_csv("result/user_server_10_capacity_5.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_user_server_5_capacity_10 = pd.read_csv("result/user_server_5_capacity_10.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_user_server_20_capacity_5 = pd.read_csv("result/user_server_20_capacity_5.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_user_server_20_capacity_10 = pd.read_csv("result/user_server_20_capacity_10.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_user_server_10_capacity_10 = pd.read_csv("result/user_server_10_capacity_10.csv", names=(un, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_capacity_user_25_server_5 = pd.read_csv("result/capacity_user_25_server_5.csv", names=(cp, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_capacity_user_25_server_10 = pd.read_csv("result/capacity_user_25_server_10.csv", names=(cp, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_capacity_user_50_server_10 = pd.read_csv("result/capacity_user_50_server_10.csv", names=(cp, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_delay_user_d_us_200_d_st_100 = pd.read_csv("result/delay_user_d_us_200_d_st_100.csv", names=(un, tds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_delay_user_d_us_200_d_st_200 = pd.read_csv("result/delay_user_d_us_200_d_st_200.csv", names=(un, tds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_server_user_25_capacity_5 = pd.read_csv("result/server_user_25_capacity_5.csv", names=(sn, tds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_server_user_25_capacity_10 = pd.read_csv("result/server_user_25_capacity_10.csv", names=(sn, tds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
# df_server_user_50_capacity_10 = pd.read_csv("result/server_user_50_capacity_10.csv", names=(sn, tds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_kanto_user_server_8_capacity_5 = pd.read_csv("result/kanto_user_server_8_capacity_5.csv", names=(untds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)
df_kanto_user_server_8_capacity_10 = pd.read_csv("result/kanto_user_server_8_capacity_10.csv", names=(untds_min, tds_max, cts, tdes, ctes, ctg, ctsc, ctc)).replace(0.0, np.nan)

# %%
Graph.initialize_rcparams()

# %%
# plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_server_5_capacity_10[un], df_user_server_5_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_server_5_capacity_10.pdf')
# plt.show()
# plt.close()


# # %%

# plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_server_20_capacity_5[un], df_user_server_20_capacity_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_server_20_capacity_5.pdf')
# plt.show()
# plt.close()


# # %%

# # %%

# plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_server_20_capacity_10[un], df_user_server_20_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_server_20_capacity_10.pdf')
# plt.show()
# plt.close()


# # %%

# plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_server_10_capacity_10[un], df_user_server_10_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_server_10_capacity_10.pdf')
# plt.show()
# plt.close()


# # %%

# plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_user_server_10_capacity_5[un], df_user_server_10_capacity_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/user_server_10_capacity_5.pdf')
# plt.show()
# plt.close()


# # %%

# plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_capacity_user_25_server_5[cp], df_capacity_user_25_server_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(cp + ', ' + r'$M_s$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/capacity_user_25_server_5.pdf')
# plt.show()
# plt.close()


# # %%

# # 1点おかしいので排除
# df_capacity_user_25_server_10.at[1, ctg] = np.nan

# plt.plot(df_capacity_user_25_server_10[cp], df_capacity_user_25_server_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_capacity_user_25_server_10[cp], df_capacity_user_25_server_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_capacity_user_25_server_10[cp], df_capacity_user_25_server_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_capacity_user_25_server_10[cp], df_capacity_user_25_server_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(cp + ', ' + r'$M_s$')
# plt.ylabel(ct + ' [s]')

# plt.ylim(0, 2)

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/capacity_user_25_server_10.pdf')
# plt.show()
# plt.close()

# %%
# # %%

# # 1点おかしいので排除
# df_capacity_user_50_server_10.at[9, ctg] = np.nan

# plt.plot(df_capacity_user_50_server_10[cp], df_capacity_user_50_server_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_capacity_user_50_server_10[cp], df_capacity_user_50_server_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_capacity_user_50_server_10[cp], df_capacity_user_50_server_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_capacity_user_50_server_10[cp], df_capacity_user_50_server_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(cp + ', ' + r'$M_s$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper right")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/capacity_user_50_server_10.pdf')
# plt.show()
# plt.close()


# %%

plt.plot(df_delay_user_d_us_200_d_st_100[un], df_delay_user_d_us_200_d_st_100[tdes], label=('ESUM'), color='k', marker='x', linestyle='-')
plt.plot(df_delay_user_d_us_200_d_st_100[un], df_delay_user_d_us_200_d_st_100[tds_max], label=('SUM (upper-bound)'), color='k', marker='o', linestyle='--')
plt.plot(df_delay_user_d_us_200_d_st_100[un], df_delay_user_d_us_200_d_st_100[tds_min], label=('SUM (lower-bound)'), color='k', marker='^', linestyle='-.')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(td)

plt.ylim(ymin=0)

plt.legend(loc="lower right")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/delay_d_us_200_d_st_100.pdf')
plt.show()
plt.close()


# # %%

# plt.plot(df_delay_user_d_us_200_d_st_100[un], df_delay_user_d_us_200_d_st_100[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_delay_user_d_us_200_d_st_100[un], df_delay_user_d_us_200_d_st_100[cts], label=('SUM'), color='k', marker='o', linestyle='--')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/time_d_us_200_d_st_100.pdf')
# plt.show()
# plt.close()


# # %%
# plt.plot(df_delay_user_d_us_200_d_st_200[un], df_delay_user_d_us_200_d_st_200[tdes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_delay_user_d_us_200_d_st_200[un], df_delay_user_d_us_200_d_st_200[tds_max], label=('SUM'), color='k', marker='o', linestyle='--')
# plt.plot(df_delay_user_d_us_200_d_st_200[un], df_delay_user_d_us_200_d_st_200[tds_min], color='k', marker='o', linestyle='--')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(td)

# plt.legend(["ESUM", "SUM"], loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/delay_d_us_200_d_st_200.pdf')
# plt.show()
# plt.close()


# # %%

# plt.plot(df_delay_user_d_us_200_d_st_200[un], df_delay_user_d_us_200_d_st_200[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_delay_user_d_us_200_d_st_200[un], df_delay_user_d_us_200_d_st_200[cts], label=('SUM'), color='k', marker='o', linestyle='--')

# plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/time_d_us_200_d_st_200.pdf')
# plt.show()
# plt.close()


# # %%

# df_server_user_25_capacity_5.at[2, ctg] = np.nan

# plt.plot(df_server_user_25_capacity_5[sn], df_server_user_25_capacity_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_server_user_25_capacity_5[sn], df_server_user_25_capacity_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_server_user_25_capacity_5[sn], df_server_user_25_capacity_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_server_user_25_capacity_5[sn], df_server_user_25_capacity_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(sn + ', ' + r'$|{V_{\rm S}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/server_user_25_capacity_5.pdf')
# plt.show()
# plt.close()

# #%%

# plt.plot(df_server_user_25_capacity_10[sn], df_server_user_25_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_server_user_25_capacity_10[sn], df_server_user_25_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_server_user_25_capacity_10[sn], df_server_user_25_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_server_user_25_capacity_10[sn], df_server_user_25_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(sn + ', ' + r'$|{V_{\rm S}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/server_user_25_capacity_10.pdf')
# plt.show()
# plt.close()


# #%%


# # %%

# plt.plot(df_server_user_50_capacity_10[sn], df_server_user_50_capacity_10[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_server_user_50_capacity_10[sn], df_server_user_50_capacity_10[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
# plt.plot(df_server_user_50_capacity_10[sn], df_server_user_50_capacity_10[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
# plt.plot(df_server_user_50_capacity_10[sn], df_server_user_50_capacity_10[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

# plt.xlabel(sn + ', ' + r'$|{V_{\rm S}}|$')
# plt.ylabel(ct + ' [s]')

# plt.legend(loc="upper left")

# plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/server_user_50_capacity_10.pdf')
# plt.show()
# plt.close()


# %%
plt.plot(df_kanto_user_server_8_capacity_5[un], df_kanto_user_server_8_capacity_5[ctes], label=('ESUM'), color='k', marker='x', linestyle='-')
# plt.plot(df_kanto_user_server_8_capacity_5[un], df_kanto_user_server_8_capacity_5[ctg], label=('GLPK'), color='k', marker='s', linestyle='-.')
plt.plot(df_kanto_user_server_8_capacity_5[un], df_kanto_user_server_8_capacity_5[ctsc], label=('SCIP'), color='k', marker='^', linestyle='--')
plt.plot(df_kanto_user_server_8_capacity_5[un], df_kanto_user_server_8_capacity_5[ctc], label=('CPLEX'), color='k', marker='o', linestyle=':')

plt.xlabel(un + ', ' + r'$|{V_{\rm U}}|$')
plt.ylabel(ct + ' [s]')

plt.legend(loc="upper left")

plt.savefig('/Users/takaaki/Dropbox/oki_lab/m2/paper/ieice_server/workspace/fig/kanto_user_server_5_capacity_10.pdf')
plt.show()
plt.close()


# %%
