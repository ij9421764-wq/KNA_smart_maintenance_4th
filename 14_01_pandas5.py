import pandas as pd
import numpy as np
from tabulate import tabulate

F = 'data/14_hydraulic_26_261112_1.csv'
F_QC = 'data/14_hydraulic_qc_26_261112_2.csv'
F_H_STD = 'data/14_hydraulic_std_26_261112_3.csv'

df = pd.read_csv(F, encoding="utf-8")
qc = pd.read_csv(F_QC, encoding="utf-8")
h_std = pd.read_csv(F_H_STD, encoding="utf-8")

##################################################################

# print(df.shape)

# valve_cnt = df["밸브상태"].value_counts()
# print(f"\n{valve_cnt}")

# valve_ratio = df["밸브상태"].value_counts(normalize=True)
# print(f"\n{round(valve_ratio, 3)}")

# load_cnt = df["운전부하"].value_counts()
# print(f"\n{load_cnt}")

# load_ratio = df["운전부하"].value_counts(normalize=True)
# print(f"\n{round(load_ratio, 3)}")

# print(f"\n최대 : {valve_cnt.idxmax()} {valve_cnt.max()}")
# print(f"최소 : {valve_cnt.idxmin()} {valve_cnt.min()}")
# print(f"\n최대 : {load_cnt.idxmax()} {load_cnt.max()}")
# print(f"최소 : {load_cnt.idxmin()} {load_cnt.min()}")

##################################################################

# print(qc.shape)

# cnt = qc["검사결과"].value_counts()
# ratio = qc["검사결과"].value_counts(normalize=True)

# print(f"\n{cnt}")
# print(f"\n{round(ratio, 3)}")

# print(f"\n불합격 비율 : {ratio['불합격'] * 100:.1f}%")

##################################################################

# print(f"진동 범위 : {df['진동'].min():.3f} ~ {df['진동'].max():.3f}")

# vib_range = pd.cut(
#     df["진동"],
#     bins=[0, 0.6, 0.7, 1.0],
#     labels=["약함", "보통", "강함"]
# )

# cnt = vib_range.value_counts()
# ratio = vib_range.value_counts(normalize=True)

# print(f"\n {cnt}")
# print(f"\n {ratio}")

# print(f"\n 구간 미지정 : {vib_range.isna().sum()}")

# print(f"\n 가장 많은 구간 : {cnt.idxmax()} {cnt.max()}")

# print(f"\n 가장 적은 구간 : {cnt.idxmin()} {cnt.min()}")

##################################################################

# counts = df.groupby("냉각기상태")["온도"].count()
# print(f"\n {counts}\n")

# means = df.groupby("냉각기상태")["온도"].mean()

# print(f"{round(means, 2)}\n")

# max_temp = df.groupby("냉각기상태")["온도"].max()
# print(f"{round(max_temp, 2)}\n")

# print(f"평균 차이 : {means.max() - means.min():.2f}")

##################################################################

total_cnt = df["밸브상태"].value_counts()

fault_cnt = df[df["result"] == "고장"]["밸브상태"].value_counts()

print(f"\n{total_cnt}\n")
print(f"{fault_cnt}\n")

ratio = round(fault_cnt / total_cnt, 3)

print(f"{ratio}\n")
print(f"가장 높은 상태 : {ratio.max()}\n")