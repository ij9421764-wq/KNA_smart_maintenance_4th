import numpy as np

F = 'data/11_hydraulic_cooler_20_261105_2.csv'

def col(c) :
    return np.genfromtxt(F,delimiter=',', skip_header=1, usecols=c, encoding = "utf-8")

######################################################################################################

# vib = col(2)

# missing = np.isnan(vib)

# missing_cnt = np.sum(missing)

# missing_ratio = np.mean(missing)

# mean_all = np.mean(vib)
# mean_no_nan = np.nanmean(vib)

# print(f"결측 {missing_cnt}건")
# print(f"비율 {missing_ratio:.2f}")
# print(f"결측 제외 평균 {mean_no_nan:.3f}")
# print(f"일반 평균 {mean_all}")

######################################################################################################

# temp = col(1)

# q1, q3 = np.percentile(temp, [25, 75])
# iqr = q3 - q1
# upper = q3 + 1.5 * iqr
# outlier = temp[temp > upper]

# print(f"상한 = {upper:.1f}")
# print("이상치:", outlier)
# print("개수:", len(outlier))

######################################################################################################

# cyc = col(0)
# temp = col(1)

# temp_avg = np.mean(temp)
# temp_std = np.std(temp)

# temp_z = (temp - temp_avg) / temp_std

# idx = np.where(np.abs(temp_z) > 2)


# print("이상 시점:", cyc[idx].astype(int))
# print(f"최대 z-score: {np.max(np.abs(temp_z)):.2f}" )

######################################################################################################


# cyc = col(0)
# temp = col(1)

# avg, std = np.mean(temp), np.std(temp)

# upper = avg + 3 * std

# idx = np.where(temp > upper)

# print(idx)

# print(f"상한 {upper:.2f}")
# print("걸리는 사이클:", cyc[idx].astype(int))

######################################################################################################

# temp = col(1)
# ce = col(3)

# corr = np.corrcoef(temp, ce)

# # print(corr)

# r = corr[0, 1]

# print(f"상관계수 : {r:.2f}")

######################################################################################################

# temp = col(1)
# vib = col(2)
# ce = col(3)
# cp = col(4)

# M = np.stack([temp, vib, ce, cp])

# avg = np.nanmean(M, axis=1)

# std = np.nanstd(M, axis=1)

# print("센서별 평균 :", np.round(avg, 1))
# print("흩어진 정도 :", np.round(std, 1))

######################################################################################################

# cyc = col(0)
# temp = col(1)

# cs = np.cumsum(temp - np.nanmean(temp))

# idx = np.argmin(cs)

# cyc_min = int(cyc[idx])

# print(f"{cyc_min}번 사이클 뒤({cyc_min}~{cyc_min+1}번 사이)가 경계 후보, {cyc_min+2}번은 경보 초과 시작")

######################################################################################################

cyc = col(0)
temp = col(1)
ce = col(3)
status = col(5)

z_temp = np.abs((temp - np.nanmean(temp))/ np.nanstd(temp))
z_ce = np.abs((ce - np.nanmean(ce))/ np.nanstd(ce))

score = z_temp + z_ce
idx = np.argmax(score)
top3 = np.argsort(score)[-3:][::-1]


print(f"최고 점수 {int(cyc[idx])}번 {score[idx]:.2f}")

print("상위 세 시점 :",cyc[top3].astype(int))

print("상태 라벨 :",cyc[status == 1].astype(int))