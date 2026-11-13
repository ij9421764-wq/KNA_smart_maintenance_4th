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

# print(qc["검사결과"].value_counts())

# temp_stats = qc.groupby("검사결과")["온도"].agg(
#     ["mean", "std", "max"]
# ).round(2)

# print(temp_stats)


# result = qc.groupby("검사결과").agg(
#     평균온도=("온도", "mean"),
#     평균냉각효율=("냉각효율", "mean"),
#     측정수=("온도", "count")
# ).round(2)

# print(tabulate(
#     result.reset_index(),
#     headers="keys",
#     tablefmt="pretty",
#     showindex=False,
#     floatfmt=".2f"
# ))

##################################################################

# marked = df.copy()

# marked["그룹평균"] = (
#     marked.groupby("냉각기상태")["온도"]
#     .transform("mean")
# )

# marked["편차"] = marked["온도"] - marked["그룹평균"]

# print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))

# print()
# max_idx = marked["편차"].abs().idxmax()

# print(marked.loc[max_idx,["냉각기상태", "온도", "그룹평균", "편차"]])

# print()

# temp_table = pd.pivot_table(
#     df,
#     index="밸브상태",
#     columns="운전부하",
#     values="온도",
#     aggfunc="mean",
#     margins=True,
#     margins_name="전체"
# )

# print(temp_table.round(2))

##################################################################

# corr_temp_vib = df["온도"].corr(df["진동"])
# print(round(corr_temp_vib, 3))


# corr_temp_press = df["온도"].corr(df["압력"])
# print(round(corr_temp_press, 3))


# corr_temp_eff = df["온도"].corr(df["냉각효율"])
# print(round(corr_temp_eff, 3))


# sensor_cols = ["온도", "진동", "압력", "냉각효율"]
# corr_matrix = df[sensor_cols].corr()
# print(corr_matrix.round(3))

##################################################################

# sensor_cols = qc.select_dtypes(include="number").columns.tolist()

# print(f"{sensor_cols} \n 수치형 지표 개수: {len(sensor_cols)}\n")

# corr_matrix = qc[sensor_cols].corr()
# print(f"{corr_matrix.round(2)}\n")

# rows = []
# for i in range(len(sensor_cols)):
#     for j in range(i + 1, len(sensor_cols)):

#         a = sensor_cols[i]
#         b = sensor_cols[j]

#         rows.append({"지표1": a, "지표2": b, "상관계수": corr_matrix.loc[a, b]})

# pair_table = pd.DataFrame(rows)

# pair_table["절댓값"] = pair_table["상관계수"].abs()

# print("중복 제외 pair_pable 행 확인 :", len(pair_table))

# print(f"\n상관계수 절댓값 0.4 이상 개수 : {len(pair_table[pair_table['절댓값'] >= 0.4])}\n")
# print(f"상관계수 절댓값 0.95 이상 개수 : {len(pair_table[pair_table['절댓값'] >= 0.95])}\n")


# print(f"0.95 이상 상위 5쌍 : \n {pair_table.sort_values(by='절댓값',ascending=False).head(5).round(2).to_string(index=False)}")

##################################################################

print()
print("냉각기 상태 중복 개수:",h_std["냉각기상태"].duplicated().sum())

merged = df.merge(h_std, on="냉각기상태",how="left")
print(f"\n병합 전: {df.shape} -> 병합 후: {merged.shape}\n")

merged["온도구간"] = pd.cut(merged["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"])

diagnosis = merged.groupby("냉각기상태").agg(
    측정수=("온도", "count"),
    평균온도=("온도", "mean"),
    온도표준편차=("온도", "std"),
    평균냉각효율=("냉각효율", "mean"),
    위험도=("위험도", "first"),
    점검주기=("권장점검주기", "first")
)

print(tabulate(diagnosis.round(2), headers="keys", tablefmt="grid"))

cross_table = pd.crosstab(merged["냉각기상태"],merged["온도구간"])
print(tabulate(cross_table, headers="keys", tablefmt="grid"))

corr_1 = merged["온도"].corr(merged["냉각효율"])
corr_2 = merged["온도"].corr(merged["진동"])

print(f"\n온도 - 냉각효율 : {round(corr_1, 3)}")
print(f"\n온도 - 진동 : {round(corr_2, 3)}")

diagnosis_sorted = diagnosis.sort_values(by=["위험도", "평균온도"],ascending=[False, False])
print(tabulate(diagnosis_sorted.round(2), headers="keys", tablefmt="grid"))