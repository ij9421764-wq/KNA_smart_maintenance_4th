# temp = [25, 26, 24, 27, 26]

# print(temp)
# print(len(temp))

# empty_list = []
# print(empty_list)
# print(len(empty_list))

#################

# temps = [22, 24, 27, 25, 26, 23]

# print(temps[0]) 
# print(temps[2]) 
# print(temps[-1])

#################

# production = [100, 105, 108, 110, 115, 122]

# first = production[0]
# last = production[-1]

# total = first + last
# middle = total / 2

# print(total)
# print(middle)

#################

# temps = [22, 24, 27, 25, 26, 28, 29, 30, 21, 23]

# front = temps[:3]
# back = temps[-3:]

# print(front)
# print(back)
# print(len(front))

#################

# numbers = [3, 4, 5, 6, 5, 4, 6, 7, 8, 7, 5, 3]

# first = numbers[:6]
# second = numbers[6:]

# print(first)
# print(second)
# print(len(first))
# print(len(second))

#################

# temps = [25, 26, 240, 28, 27]

# print(240 in temps)

# idx = temps.index(240)
# temps[idx] = 24

# print(temps)

# print(240 in temps)

#################

# temps = []

# temps.append(30)
# print(temps)

# temps.insert(0, 28)
# print(temps)

# temps.extend([31, 32])
# print(temps)

#################

# temps = [25, 26, 999, 24, 28, 26]

# temps.remove(999)
# print(temps)

# removed = temps.pop(1)
# print("꺼낸 값", removed)

# del temps[0]
# print(temps)

#################

temps = [27, 26, 30, 22, 24, 28, 24]

temps.sort()
print(temps)

temps.reverse()
print(temps)

temps = [27, 26, 30, 22, 24, 28, 24]

print(temps.count(24))

print(temps.index(24))