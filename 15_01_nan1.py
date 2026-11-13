import pandas as pd
import numpy as np
from tabulate import tabulate

F_PROC = 'data/15_사출성형_공정_28_261113_1.csv'
F_LOG = 'data/15_사출성형_로그_28_261113_2.csv'


df = pd.read_csv(F_PROC, encoding="utf-8")
qc = pd.read_csv(F_LOG, encoding="utf-8")

##########################################################################

# print(qc.shape)
# print(f"NaN의 전체 개수 : {qc.isna().sum().sum()}")
# print(f"사출압력 - 0의 전체 개수 : {(qc['사출압력'] == 0).sum()}")
# print(f"스크루속도 - -999의 전체 개수 : {(qc['스크루속도'] == -999).sum()}")
# print(f"배럴온도 - 999의 전체 개수 : {(qc['배럴온도'] == 999).sum()}")

##########################################################################

print(df.shape)
print(df.head(3))

df.info()

result = df["최대사출속도"].describe()

##########################################################################
