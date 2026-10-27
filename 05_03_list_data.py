# temperatures = [25, 32, 28, 35, 31]

# for temp in temperatures:
#     if temp >= 30:
#         print("고온:", temp)

################################################

# hours = [3, 8, 12, 6, 10, 15, 9]

# for hour in hours:
#     if hour >= 5 and hour <= 10:
#         print(hour)

################################################

# temperatures = [28, 32, 36, 25, 31, 29]

# total = 0
# count = 0

# for temp in temperatures:
#     if temp > 30:
#         total += temp
#         count += 1

# average = total / count

# print("고온 평균:", average)

################################################

# temperatures = [28, 32, 35, 25, 31, 29, 33]

# high_temps = []

# for temp in temperatures:
#     if temp > 30:
#         high_temps.append(temp)

# print(high_temps)
# print("개수:", len(high_temps))

################################################

# celsius = [25, 26, 24, 28, 27]

# fahrenheit = []

# for temp in celsius:
#     f = temp * 1.8 + 32
#     fahrenheit.append(f)

# print(fahrenheit)

################################################

temperatures = [25, 32, 35, 28, 31, 29, 34, 30, 35, 21]

total = 0

for temp in temperatures:
    total += temp

overall_avg = total / len(temperatures)

high_temps = []

for temp in temperatures:
    if temp > 30:
        high_temps.append(temp)

high_total = 0

for temp in high_temps:
    high_total += temp

high_avg = high_total / len(high_temps)

print("전체 평균:", overall_avg)
print("고온 개수:", len(high_temps))
print("고온 평균:", high_avg)