import numpy as np

F = 'data/11_diecasting_series_20_261105_1.csv'

def col(c) :
    return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

# 1차원 리스트 형태로 넘어옴
shot = col(0)

ct = col(1)

# 2차원 리스트 형태로 넘어옴
test = col((0, 1))

idx = np.argmax(ct)

shot_no = int(shot[idx])
max_ct = ct[idx]

print(f"{shot_no}번 샷에서 사이클타임 {max_ct:.1f}초", end="")
print(f"(배열 인덱스는 {idx})")