# def check_device(device):
#     print(device, "점검 시작")

# check_device("압축기A")
# check_device("펌프1")

###############################

# def sensor(name, temp):
#     print(name, temp, "도")

# sensor("모터", 78)
# sensor("펌프", 92)

# print("### 인수 순서 변경 시 ###")
# sensor(92, "펌프")

###############################

# def sensor(name, temp):
#     print(f"{name} {temp}")

# sensor(name="모터", temp=78)
# sensor(temp=92, name="펌프")

# # 위치 인자와 키워드 인자 섞을 때 -> 에러 발생
# # 위치 인자가 먼저이기 때문
# sensor(92, name="펌프")

###############################

# def average(num1, num2):
#     return (num1 + num2) / 2

# result = average(78, 92)
# print(result)

# result2 = average(result, 95)
# print(result2)

###############################

# def sensor_value_calculate(values):
#     minimum = min(values)
#     maximum = max(values)
#     average = sum(values) / len(values)

#     return minimum, maximum, average

# min_v, max_v, avg_v = sensor_value_calculate([78, 92])

# print(min_v, max_v, avg_v)