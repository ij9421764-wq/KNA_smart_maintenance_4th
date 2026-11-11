import pandas as pd
import numpy as np
from tabulate import tabulate

F = 'data/12_metro_compressor_22_261109_1.csv'
FS = 'data/12_metro_compressor_semicolon_22_261109_2.csv'

df = pd.read_csv(F, encoding="utf-8")

# print("데이터 크기:", df.shape)

# print("\n[앞 5행]")

# print(tabulate(df.head(), headers = "keys", tablefmt = 'fancy_outline'))

############################################################################

# df = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"], encoding="utf-8")
# print(df.shape)


# df = pd.read_csv(F, nrows=20, encoding="utf-8")
# print(df.shape)

############################################################################

# df = pd.read_csv("data/12_metro_compressor_semicolon_22_261109_2.csv", encoding="utf-8")

# print(df.shape)

# df = pd.read_csv("data/12_metro_compressor_semicolon_22_261109_2.csv", sep=";", encoding="utf-8")

# print(df.shape)

############################################################################

df = pd.read_csv(
    FS,
    sep=";",
    encoding="utf-8",
    usecols=["측정시각", "오일온도", "모터전류"],
    nrows=50
)

print(df.shape)
print(tabulate(df.head(), headers = "keys", tablefmt = 'fancy_outline'))