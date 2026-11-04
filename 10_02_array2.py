# import csv
# import numpy as np

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

import csv
import numpy as np

result = []

with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)

    for row in reader:
        rpm = int(row[4])     
        torque = int(row[5])

        result.append([rpm, torque])

sensor = np.array(result[0:4])
print("세 번째 시점", sensor[2])
print("\n회전수 열", sensor[:, 0])
print("\n토크 열", sensor[:, 1])