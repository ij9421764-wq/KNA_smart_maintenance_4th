import csv
import numpy as np

# csv_rpm = []

# with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     header = next(reader)

#     for row in reader:
#         csv_rpm.append(int(row[4]))

# np_rpm = np.array(csv_rpm[0:10])

# print("\n맨 앞 값 : ", np_rpm[0])

# print("\n맨 뒤 값 : ", np_rpm[-1])

# print("\n두 번째~네 번째 : ", np_rpm[1:4])

# print("\n하나 걸러 하나 : ", np_rpm[::2])

#####################################################

# import csv
# import numpy as np

# result = []

# with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     header = next(reader)

#     for row in reader:
#         rpm = int(row[4])     
#         torque = int(row[5])

#         result.append([rpm, torque])

# sensor = np.array(result[0:4])
# print("세 번째 시점", sensor[2])
# print("\n회전수 열", sensor[:, 0])
# print("\n토크 열", sensor[:, 1])

#####################################################

# result = []

# with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)

#     # header = next(reader)

#     for row in reader:
#         result.append(int(row["회전수"]))

# rpm = np.array(result[:10])

# rpm_min = rpm.min()
# rpm_max = rpm.max()

# rpm_norm = (rpm - rpm_min) / (rpm_max - rpm_min)

# print(f"결과 : {np.round(rpm_norm, 2)}")

#####################################################

# rpm_list = []
# torque_list = []
# electric_current_list = []

# with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         rpm_list.append(int(row['회전수']))      
#         torque_list.append(int(row['토크']))   
#         electric_current_list.append(float(row['전류']))

# rpm = np.array(rpm_list)
# torque = np.array(torque_list)
# electric_current = np.array(electric_current_list)

# rpm_2000_under = rpm < 2000

# print("회전수 2000 미만 : ", rpm_2000_under)

# rpm_elec_torque_10_overi = (rpm < 2000) | (electric_current > 25)

# print("\n회전수 2000 미만 또는 전류 25 초과", rpm_elec_torque_10_overi)

# rpm_2000_under_count = np.sum(rpm_2000_under)
# rpm_elec_torque_10_overi_count = np.sum(rpm_elec_torque_10_overi)

# print("\n회전수 2000 미만 개수:", rpm_2000_under_count)
# print("회전수 2000 미만 또는 전류 25 초과 개수:", rpm_elec_torque_10_overi_count)

# rpm_2000_under_ratio1 = rpm_2000_under_count / len(rpm)
# rpm_elec_torque_10_overi_ratio2 = rpm_elec_torque_10_overi_count / len(rpm)

# print("\n회전수 2000 미만 비율:", round(rpm_2000_under_ratio1, 2))
# print("회전수 2000 미만 또는 전류 25 초과 비율:", round(rpm_elec_torque_10_overi_ratio2, 2))

#####################################################

# torque_list = []

# with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         torque_list.append(int(row['토크']))

# torque = np.array(torque_list[:10])

# torque_10_over = torque > 10

# print("조건 배열 : \n", torque_10_over)

# count = np.sum(torque_10_over)

# ratio = np.mean(torque_10_over)

# print("\n개수:", count)
# print("비율:", round(ratio, 2))

#####################################################

# result = []

# with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         rpm = int(row['회전수'])      
#         torque = int(row['토크'])   

#         result.append([rpm, torque])

# sensor = np.array(result)

# mean_value = sensor.mean(axis=0)
# std_value = sensor.std(axis=0)

# print("\n평균 : ", np.round(mean_value, 1))
# print("\n표준편차 : ", np.round(std_value, 1))

#####################################################

# rpm = np.loadtxt("data/10_mct_tool_18_261104.csv", delimiter=",",
#                 skiprows=1, usecols=4, encoding='utf-8')


# mean_value = rpm.mean()
# std_value = rpm.std()
# min_value = rpm.min()
# max_value = rpm.max()

# print("평균:", round(mean_value, 1))
# print("표준편차:", round(std_value, 1))
# print("최소값:", min_value)
# print("최대값:", max_value)

#####################################################

# torque = np.loadtxt("data/10_mct_tool_18_261104.csv", delimiter=",",
#                 skiprows=1, usecols=-1, encoding='utf-8')

# total_mean = torque.mean()

# selected_torque = torque[torque > 10]

# print("골라낸 값 : ", selected_torque)

# print("개수 : ", len(selected_torque))
# print("평균 : ", round(selected_torque.mean(), 1))

# print("전체 평균 : ", round(total_mean, 1))
# print("평균 차이 :", round(selected_torque.mean() - total_mean, 1))

#####################################################


data = torque = np.loadtxt("data/10_mct_tool_18_261104.csv", delimiter=",",
                skiprows=1, usecols=(-2, -1), encoding='utf-8')

print("shape:", data.shape)
print("dtype:", data.dtype)

rpm = data[:, 0]

under_rpm = rpm[rpm < 2000]

under_count = under_rpm.size
under_mean = under_rpm.mean()
total_mean = rpm.mean()

print("이상 시점 개수:", under_count)
print("이상 시점 평균:", round(under_mean, 1))
print("전체 평균:", round(total_mean, 1))
