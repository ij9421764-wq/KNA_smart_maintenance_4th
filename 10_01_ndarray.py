import numpy as np

# celsius = np.array([10, 15, 20, 25, 30, 35])

# print("섭씨 온도:")
# print(celsius)

# fahrenheit = celsius * 1.8 + 32

# print("\n화씨 온도:")
# print(fahrenheit)

############################################################

# start = 0
# end = 70

# electric_current = np.linspace(start, end, 8)

# print(f"전류 값: {electric_current}\n")

# print(f"마지막 값: {end in electric_current}")

############################################################

# start = 0
# end = 40

# measurement_no = np.arange(start, end, 5)

# print(f"측정 순번: {measurement_no}")
# print(f"40 포함 여부: {end in measurement_no}")

############################################################

# sensor_data = np.array([
#     [20, 5],
#     [22, 10],
#     [24, 15],
#     [26, 20]
# ])

# print(f"센서 데이터: \n {sensor_data}")

# print("차원(ndim):", sensor_data.ndim)

# print("형태(shape):", sensor_data.shape)

# print("개수(size):", sensor_data.size)

# rows, cols = sensor_data.shape
# print(f"줄 수 × 칸 수 = 전체 개수 : {rows * cols == sensor_data.size}")

############################################################

# electric_current = np.array([18.69, 25.42, 31.87, 40.95])

# print("원본 dtype:", electric_current.dtype)

# electric_current_int = electric_current.astype(int)

# print("변환 후 :", electric_current_int)

############################################################

# cycle_time = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

# cycle_table = cycle_time.reshape(3, 4)

# print("\n원본 배열")
# print(cycle_time)

# print("\n3행 4열 표")
# print(cycle_table)

# print("\n원본 개수:", cycle_time.size)
# print("변경 후 개수:", cycle_table.size)

############################################################

sensor_data = np.array([
    20.1, 5.5, 1000,
    22.2, 7.6, 1050,
    24.3, 9.7, 1100,
    26.4, 11.8, 1150
])

sensor_table = sensor_data.reshape(4, 3)

print("\n4행 3열 표")
print(sensor_table)

flat_data = sensor_table.flatten()

print("\n다시 펼친 배열")
print(flat_data)

print("\n원본 배열:")
print(sensor_data)