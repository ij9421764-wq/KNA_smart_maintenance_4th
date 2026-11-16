import pandas as pd
import numpy as np
from tabulate import tabulate

F_PROC = 'data/15_사출성형_공정_28_261113_1.csv'
F_LOG = 'data/15_사출성형_로그_28_261113_2.csv'

NA_RULES = {
    "배럴온도": [999],
    "스크루속도": [-999],
    "사출압력": [0]
}

df = pd.read_csv(F_PROC, encoding="utf-8")
qc = pd.read_csv(F_LOG, encoding="utf-8")
qc_na = pd.read_csv(F_LOG, encoding="utf-8", na_values=NA_RULES)

##########################################################################

# print("원본 데이터:", df.shape)

# rows_removed = df.dropna()
# cols_removed = df.dropna(axis=1)

# print(f"행 삭제 : {rows_removed.shape}")
# print(f"열 삭제 : {cols_removed.shape}")
# print("원본 데이터:", df.shape)

##########################################################################

# sensor_cols = df.select_dtypes(include="number").columns.tolist()
# result_all = df.dropna(how="all")

# print("how='all':", result_all.shape)
# print("thresh 20':", df.dropna(thresh=20).shape)

# print("불량여부 결측 수 : ", df["불량여부"].isna().sum())
# print("subset 불량여부 : ", df.dropna(subset=['불량여부']).shape)

##########################################################################

feature_cols = df.select_dtypes(include="number").columns.tolist()

missing_rate = df[feature_cols].isna().mean() * 100
drop_cols = missing_rate[missing_rate >= 40].index.tolist()
print("\n40% 이상인 열 :", drop_cols)

df_drop_cols = df.drop(columns=drop_cols)
print("\n열 제거 결과:", df_drop_cols.shape)

