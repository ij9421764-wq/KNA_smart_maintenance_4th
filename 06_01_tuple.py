################################

# sensor = ("모터온도", 78)


# print(sensor)
# print(sensor[0])
# print(sensor[1])

# name, value = sensor
# print(name, value)

################################

# sensors = [
#     ("모터온도", 78),
#     ("회전속도", 95),
#     ("펌프압력", 100)
# ]

# for name, value in sensors:
#     print(f"{name}: {value}")

    
#     if value > 90:
#         print(f"{name} 경고")

################################

sensors = [
    ("모터온도", 78, (3, 8)),
    ("회전속도", 95, (7, 2)),
    ("펌프압력", 88, (5, 5))
]

for name, value, (x, y) in sensors:
    print(f"{name} 위치: ({x}, {y})")

print("x <= 5 센서만 : ", end="")

for name, value, (x, y) in sensors:
    if x <= 5:
        print(f"{name}", end=", ")