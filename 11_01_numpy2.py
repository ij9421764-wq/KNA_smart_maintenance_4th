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

# F = 'data/11_diecasting_series_20_261105_1.csv'

# def col(c) :
#     return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

# shot = col(0)
# ct = col(1)

# diff_ct = np.diff(ct)
# abs_diff = np.abs(diff_ct)

# idx = np.argmax(abs_diff)

# shot1 = int(shot[idx])
# shot2 = int(shot[idx + 1])

# change = abs_diff[idx]

# print(f"{shot1}번과 {shot2}번 사이에서 {change:.1f}초만큼 변함")

##########################################################################################

# F = 'data/11_diecasting_series_20_261105_1.csv'

# def col(c) :
#     return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

# cyl = col(2)


# origin_mean = np.mean(cyl)

# cyl[0] = 9999

# error_mean = np.mean(cyl)

# fixed = np.clip(cyl, 100, 300)

# fixed_mean = np.mean(fixed)

# print(f"원래 평균 : {origin_mean:.1f}")
# print(f"보정 전 평균 : {error_mean:.1f}")
# print(f"보정 후 평균 : {fixed_mean:.1f}")

##########################################################################################

# F = 'data/11_diecasting_series_20_261105_1.csv'

# def col(c) :
#     return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

# ct = col(1)

# state = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))

# value, count = np.unique(state, return_counts=True)

# print("상태번호:", value)
# print("개수:", count)

# ratio = count / len(state)

# print(f"정상 {count[0]}, 경고 {count[1]}, 잼 {count[2]}")
# print(f"비율은 {ratio[0]:.2f}, {ratio[1]:.2f}, {ratio[2]:.2f}")

##########################################################################################

# F = 'data/11_diecasting_series_20_261105_1.csv'

# def col(c) :
#     return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

# ct = col(1)      
# cyl = col(2)     
# main = col(3)    
# force = col(4)   

# M = np.stack((ct, cyl, main, force))

# print("전체 행렬 크기 :", M.shape)

# recent = M[:, -10:]

# print("잘라낸 뒤 데이터 크기 :", recent.shape)

##########################################################################################

F = 'data/11_diecasting_series_20_261105_1.csv'

def col(c) :
    return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

cyc = col(0)
ct = col(1)
cyl = col(2)

idx_max = np.argmax(ct)

max_shot = int(cyc[idx_max])
max_ct = ct[idx_max]

diff_ct = np.abs(np.diff(ct))
idx_diff = np.argmax(diff_ct)

shot1 = int(cyc[idx_diff])
shot2 = int(cyc[idx_diff + 1])

warning = (ct >= 50) | (cyl < 150)
warning_ratio = np.mean(warning)

top3_idx = np.argsort(ct)[-3:][::-1]
top3_shot = cyc[top3_idx].astype(int)

print(f"최대 {max_shot}번 {max_ct:.1f}")
print(f"급변 {shot1}->{shot2}")
print(f"경고 비율 {warning_ratio:.2f}")
print(f"상위 세 시점 {top3_shot[0]}, {top3_shot[1]}, {top3_shot[2]}")