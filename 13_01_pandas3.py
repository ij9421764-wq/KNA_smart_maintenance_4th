import pandas as pd
import numpy as np
from tabulate import tabulate

F_SHOT = 'data/13_diecasting_shot_24_261110_2.csv'
F_SMALL = 'data/13_diecasting_small_24_261110_3.csv'
F_MASTER = 'data/13_diecasting_master_24_261110_1.csv'

df = pd.read_csv(F_SHOT, encoding="utf-8")

#############################################################

# print(df.columns)

# col1 = df['형체력']

# print(type(col1))
# print(col1.head(3))
# print("크기 :", col1.shape)

# col2 = df[['형체력', '실린더압력']]

# print(type(col2))
# print(col2.head(3))
# print("크기 :", col2.shape)

# col3 = df[['형체력']]

# print(type(col3))
# print(col3.head(3))
# print("크기 :", col3.shape)

#############################################################

# print("\n[원본 데이터]")

# print("\nloc[0]의 샷번호 :", df.loc[0, '샷'])
# print("iloc[0]의 샷번호 :", df.iloc[0]['샷'])

# df2 = df.sort_values('형체력', ascending=False)

# print("\n[정렬 후]")

# print("\nloc[0]의 샷번호 :", df2.loc[0, '샷'])
# print("iloc[0]의 샷번호 :", df2.iloc[0]['샷'])

#############################################################

# print('=====================================')

# print(f"컬럼 목록 : {df.columns}")

# result_loc = df.loc[0:4, ['실린더압력', '형체력']]

# print('=====================================')

# print(f"loc 결과 : {result_loc}")
# print(f"loc 크기 : {result_loc.shape}")

# print('=====================================')

# result_iloc = df.iloc[0:5, [2, 6]]

# print(f"iloc 결과 : {result_iloc}")
# print(f"iloc 크기 : {result_iloc.shape}")

# print('=====================================')

#############################################################

print('전체 크기 :', df.shape)

print(f"컬럼 목록 : {df.columns}")

result = df.loc[:9, ['설비ID', '비스킷두께', '품질등급']]

print('\n[앞 10줄 필요한 컬럼]')
print(tabulate(result, headers='keys', tablefmt='psql', showindex=False))

tail5 = df.tail(5)

print('\n[맨 뒤 5줄]')
print(tabulate(tail5, headers='keys', tablefmt='psql', showindex=False))