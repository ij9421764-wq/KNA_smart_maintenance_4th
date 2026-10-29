# def check_score(score, limit=80):
#     if score < limit:
#         print("정상")
#     else:
#         print("경고")

# print(f"78 → ", end="")
# check_score(78)

# print(f"95 → ", end="")
# check_score(95)

# print(f"score = 50, limit = 40으로 변경 → ", end="")
# check_score(50, 40)

###############################################################

# def show_number():
#     x = 30
#     print("함수 안:", x)

# show_number()

# print(x)  # 오류 발생

###############################################################

# def calc_average(num1, num2):
#     return (num1 + num2) / 2

# def print_result(avg):
#     if avg >= 80:
#         print(f"평균 {avg} → 정상")
#     else:
#         print(f"평균 {avg} → 경고")

# result = calc_average(90, 80)
# print_result(result)

###############################################################

def calc_average(sensor_list):
    return sum(sensor_list) / len(sensor_list)

def check_status(avg, limit=90):
    if avg <= limit:
        return "정상"
    else:
        return "경고"

sensors = [90, 80, 85]

avg = calc_average(sensors)
status = check_status(avg)

print("평균:", avg)
print("상태:", status)