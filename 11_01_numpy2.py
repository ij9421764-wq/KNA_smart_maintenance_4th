import numpy as np

##########################################################################################

# F = 'data/11_diecasting_series_20_261105_1.csv'

# def col(c) :
#     return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

# # 1차원 리스트 형태로 넘어옴 -> 실수 형태로 넘어옴(나머지 실수이기 때문)
# shot = col(0)

# ct = col(1)

# idx = np.argmax(ct)

# shot_no = int(shot[idx])
# max_ct = ct[idx]

# print(f"{shot_no}번 샷에서 사이클타임 {max_ct:.1f}초", end="")
# print(f"(배열 인덱스는 {idx})")

##########################################################################################

F = 'data/11_diecasting_series_20_261105_1.csv'

def col(c) :
    return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

shot = col(0)
ct = col(1)

diff_ct = np.diff(ct)
abs_diff = np.abs(diff_ct)

idx = np.argmax(abs_diff)

shot1 = int(shot[idx])
shot2 = int(shot[idx + 1])

change = abs_diff[idx]

print(f"{shot1}번과 {shot2}번 사이에서 {change:.1f}초만큼 변함")