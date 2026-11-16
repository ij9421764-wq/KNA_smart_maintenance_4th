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

# print(qc.shape)
# print(f"NaN의 전체 개수 : {qc.isna().sum().sum()}")
# print(f"사출압력 - 0의 전체 개수 : {(qc['사출압력'] == 0).sum()}")
# print(f"스크루속도 - -999의 전체 개수 : {(qc['스크루속도'] == -999).sum()}")
# print(f"배럴온도 - 999의 전체 개수 : {(qc['배럴온도'] == 999).sum()}")

##########################################################################

# print(df.shape)
# print(df.head(3))

# df.info()

# result = df["최대사출속도"].describe()

##########################################################################

# before = qc.isna().sum()
# after = qc_na.isna().sum()

# print(f"\nbefore : {before}\n")
# print(f"after : {after}")

##########################################################################

# count = df.isna().sum()

# #  Series가 됨
# print(type(count))
# # 각 열 별로 결측값의 합이 들어가 있음
# print(count)

# ratio_pct = count / len(df) * 100

# print(count[count > 0])
# print()
# print(ratio_pct[ratio_pct > 0].round(1))

##########################################################################

# count = df.isna().sum()
# ratio_pct = count / len(df) * 100

# missing_summary = pd.DataFrame({
#     "결측개수": count,
#     "결측비율(%)": ratio_pct.round(1)
# })

# missing_rank = missing_summary.sort_values(by="결측비율(%)",ascending=False)

# print(tabulate(missing_rank.head(3), headers="keys", tablefmt="grid"))

# row_missing = df.isna().sum(axis=1)

# complete_rows = (row_missing == 0).sum()
# missing_rows = (row_missing > 0).sum()

# many_missing_rows = (row_missing >= 5).sum()

# print(f"완전한 행 : {complete_rows}")
# print(f"결측 있는 행 : {missing_rows}")
# print(f"이상인 행 : {many_missing_rows.sum()}")

##########################################################################


target_cols = ["최대사출속도", "감압시간"]
missing_mask = df[target_cols].isna()
print(tabulate(missing_mask.head(10), headers="keys", tablefmt="grid"))

both_missing = missing_mask.all(axis=1)
only_one_missing = missing_mask.sum(axis=1) == 1
both_valid = missing_mask.sum(axis=1) == 0

print(f"동시 결측 행 수 : {both_missing.sum()}")
print(f"동시 결측 비율 : {both_missing.mean() * 100}")
print(f"한 열만 결측 : {only_one_missing.sum()}")
print(f"두 열 모두 관측 : {both_valid.sum()}")
print(tabulate(df.loc[both_missing, ['측정시각', '사출기']].head(), headers="keys", tablefmt="grid"))

##########################################################################

