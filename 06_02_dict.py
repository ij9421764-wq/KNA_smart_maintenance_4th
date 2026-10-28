###################################

# sensors = {
#     "온도": 78,
#     "습도": 65,
#     "압력": 80
# }

# print(sensors["온도"])

# sensors["조도"] = 90
# sensors["온도"] = 100
# print("추가수정된 딕셔너리")
# print(sensors)

# print(sensors.get("풍속", 0))
# print("압력" in sensors)

###################################

# sensors = {
#     "온도": 75,
#     "습도": 65
# }

# new_data = {
#     "온도": 80,    
#     "압력": 90     
# }

# sensors.update(new_data)

# del sensors["습도"]

# print("갱신된 딕셔너리")
# print(sensors)

# print("센서 수:", len(sensors))

###################################

# sensors = {
#     "온도": 70,
#     "습도": 65,
#     "압력": 95
# }

# avg = sum(sensors.values()) / len(sensors)

# max_sensor = ""
# max_value = 0

# for name, value in sensors.items():
#     if value > max_value:
#         max_value = value
#         max_sensor = name

# print(f"평균: {avg:.1f}")
# print(f"최댓값 센서: {max_sensor} {max_value}")

###################################

# names = ["온도", "진동", "압력"]
# values = [78, 0.5, 95]

# sensors = dict(zip(names, values))

# print(sensors)

# for name, value in sensors.items():
#     print(name, value)

###################################

# sensors = {
#     "온도": 75,
#     "습도": 60,
#     "진동": 0.5
# }

# thresholds = {
#     "온도": 70,
#     "습도": 80,
#     "진동": 1.0
# }

# warning_sensors = []

# for name, value in sensors.items():
#     if value > thresholds[name]:
#         warning_sensors.append(name)

# print(f"경고 센서: {warning_sensors}")

###################################

# machines = {
#     "1번펌프": {
#         "압력": 80,
#         "상태": "정상"
#     },
#     "2번펌프": {
#         "압력": 95,
#         "상태": "경고"
#     }
# }

# print(machines["2번펌프"]["압력"])

# for name, info in machines.items():
#     if info["상태"] == "경고":
#         print(name, "점검 필요")

###################################

# rows = [
#     "온도,78",
#     "압력,95",
#     "진동,0.5"
# ]

# sensors = {}

# for row in rows:
    
#     # print(row.split(","))
#     name, value = row.split(",")

#     sensors[name] = float(value)

# print(sensors)

###################################

values = {
    "온도": 78,
    "압력": 113
}

limits = {
    "온도": 75,
    "압력": 100
}

avg = sum(values.values()) / len(values)
print("평균:", avg)

danger = set()

for name, value in values.items():
    if value > limits[name]:
        danger.add(name)

print("위험 센서:", sorted(danger))
