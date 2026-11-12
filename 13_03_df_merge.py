import pandas as pd
import numpy as np
from tabulate import tabulate

F_SHOT = 'data/13_diecasting_shot_24_261110_2.csv'
F_SMALL = 'data/13_diecasting_small_24_261110_3.csv'
F_MASTER = 'data/13_diecasting_master_24_261110_1.csv'

log = pd.read_csv(F_SHOT, encoding="utf-8")
master = pd.read_csv(F_MASTER, encoding="utf-8")

#######################################################

# print("log :", log.shape)
# print("master :", master.shape)

# print("\nlog columns :", log.columns)
# print("master columns :", master.columns)

# merged = log.merge(master, on="설비ID")

# print("\nmerged :", merged.shape)

# print(tabulate(merged.head(3), headers='keys', tablefmt='psql', showindex=False))

#######################################################

# inner_df = log.merge(master, on="설비ID", how="inner")
# left_df = log.merge(master, on="설비ID", how="left")
# outer_df = log.merge(master, on="설비ID", how="outer")

# print("inner :", inner_df.shape[0])
# print("left  :", left_df.shape[0])
# print("outer :", outer_df.shape[0])

# print("\n[master에 없는 설비]")
# print(left_df[left_df["라인"].isna()]["설비ID"].value_counts())

# print("\n[log에 없는 설비]")
# print(outer_df[outer_df["샷"].isna()][["설비ID"]])

#######################################################

# front = log.iloc[:100].reset_index(drop=True)
# back = log.iloc[100:].reset_index(drop=True)

# no_ignore = pd.concat([front, back])
# renumbered  = pd.concat([front, back], ignore_index=True)

# print(no_ignore.shape)
# print("번호 0 개수:", (no_ignore.index == 0).sum())

# print(renumbered.shape)
# print("마지막 인덱스:", renumbered.index[-1])

#######################################################

check = log.merge(master,on="설비ID",how="left")
check = check[check["라인"].notna()]

print("\n라인이 붙은 줄 :", len(check))

bad = check[check["품질등급"] != "양품"]
bad = bad.sort_values(by="비스킷두께",ascending=False)

print("\n양품이 아닌 행:", len(bad))

print(bad[["샷", "설비ID", "라인", "비스킷두께", "품질등급"]].head(5).to_string(index=False))