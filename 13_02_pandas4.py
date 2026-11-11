import pandas as pd
import numpy as np
from tabulate import tabulate

F_SHOT = 'data/13_diecasting_shot_24_261110_2.csv'
F_SMALL = 'data/13_diecasting_small_24_261110_3.csv'
F_MASTER = 'data/13_diecasting_master_24_261110_1.csv'

df = pd.read_csv(F_SHOT, encoding="utf-8")

#######################################################

# print('전체 크기 :', df.shape)

# cond = df['비스킷두께'] >= 16

# print('\n조건 True 개수 :', cond.sum())

# result = df[cond]

# print('추출 행 개수 :', len(result))

# cond2 = df['비스킷두께'] < 16

# print('\n16 미만 개수 :', cond2.sum())

# print('\n전체 :', len(df))
# print('합계 :', cond.sum() + cond2.sum())

#######################################################

# result_and = df[(df['비스킷두께'] >= 16) & (df['사이클타임'] >= 25)]
# print('그리고 줄 수 :', len(result_and))

# result_or = df[(df['비스킷두께'] >= 16) | (df['사이클타임'] >= 25)]
# print('또는 줄 수 :', len(result_or))

# not_bad = df[~(df['품질등급'] == '불량')]
# print('불량이 아닌 행 :', len(not_bad))

#######################################################

# cond1 = df['품질등급'].isin(['주의', '불량'])
# print('주의/불량 개수 :', cond1.sum())

# cond2 = df['비스킷두께'].between(10, 16)
# print('10~16 개수 :', cond2.sum())

# cond3 = df['설비ID'].str.contains('A')
# print('A 포함 개수 :', cond3.sum())

# cond4 = df['설비ID'] == 'DIE-A-01'
# print('DIE-A-01 개수 :', cond4.sum())

#######################################################

# df1 = df.sort_values('비스킷두께', ascending=False)
# print('[두께 상위 5개]')
# print(tabulate(df1[['샷', '비스킷두께']].head(), headers='keys', tablefmt='psql', showindex=False))

# df2 = df.sort_values(['품질등급', '사이클타임'],ascending=[True, False])
# print('\n[다중 정렬 결과]')
# print(tabulate(df2[['샷', '품질등급', '사이클타임']].head(), headers='keys', tablefmt='psql', showindex=False))

# print('\n원본 첫 5행')
# print(tabulate(df.head(), headers='keys', tablefmt='psql', showindex=False))

#######################################################

report = df[(df['품질등급'] != '양품') & (df['비스킷두께'] >= 16)]

print('조건 통과 샷 수 :', len(report))

report = report.sort_values('비스킷두께', ascending=False)

report = report[['샷', '비스킷두께', '품질등급']]

print('\n상위 5개')
print(tabulate(report.head(),headers='keys',tablefmt='psql',showindex=False))

x = df[(df["품질등급"] != "양품") & df["비스킷두께"].isna()]
print(len(x)) 