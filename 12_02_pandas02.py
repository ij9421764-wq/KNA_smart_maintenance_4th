import pandas as pd
import numpy as np
from tabulate import tabulate

F = 'data/12_metro_compressor_22_261109_1.csv'
FS = 'data/12_metro_compressor_semicolon_22_261109_2.csv'
FD = 'data/12_metro_digital_22_261109_3.csv'
MS = 'data/12_metro_small_22_261109_4.csv'

df = pd.read_csv(MS, encoding="utf-8")

####################################################


# print(df.head())

# print(df.tail())

# print(df.head(3))

# print(df.tail(10))

# print("크기:", df.shape)

####################################################

# print('------------------------------')
# print(df.shape)
# print('------------------------------')
# print(df.columns.tolist())
# print('------------------------------')

# print(df.dtypes)
# print('------------------------------')

# print(df.head())
# print('------------------------------')

####################################################

# df.info()

####################################################


# print(tabulate(df.describe().round(2), headers = "keys", tablefmt = 'fancy_outline'))

# state = df["가동상태"].values
# cur = df["모터전류"].values

# print(f"모터전류 평균 : {round(float(np.mean(cur)), 2)}")
# print(f"모터전류 한가운데 값 : {round(float(np.median(cur)), 2)}")
# print(f"가동 : {round(float(np.mean(cur[state == '가동'])), 2)}")
# print(f"정지 : {round(float(np.mean(cur[state == '정지'])), 2)}")

####################################################

print(tabulate(df.head(), headers = "keys", tablefmt = 'fancy_outline'))

print('===============================')

print(df.shape)

print('===============================')

df.info()

print('===============================')


missing = df.isna().sum().sum()
    
print('===============================')

for col in df.columns:
    missing_count = len(df) - df[col].count()
    print(f"{col}: 결측치 {missing_count}개")
    
print('===============================')

desc = df.describe()

print(desc)

print('===============================')

motor_mean = df["모터전류"].mean()
motor_median =  df["모터전류"].median()

print("\n===== 리포트 =====")
print(f"크기 : {df.shape[0]}행 {df.shape[1]}열")
print(f"결측 : {missing}건")
print(f"모터전류 평균 : {motor_mean:.2f}")
print(f"모터전류 중앙값 : {motor_median:.2f}")