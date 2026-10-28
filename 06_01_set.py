
# sensor_ids = ["S01", "S02", "S01", "S03", "S02"]

# unique_sensors = set(sensor_ids)

# print(sorted(unique_sensors))

# print("종류 수:", len(unique_sensors))

##########################################################

# line_a = {"S01", "S02", "S03", "S05"}
# line_b = {"S03", "S04", "S05"}

# all_sensors = line_a.union(line_b)

# common = line_a.intersection(line_b)

# only_a = line_a.difference(line_b)
# only_b = line_b.difference(line_a)

# print("공통:", common)
# print("전체:", all_sensors)
# print("A만:", only_a)
# print("B만:", only_b)

##########################################################

yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}

new_events = today.difference(yesterday)

ongoing_events = today.intersection(yesterday)

print("신규 이상:", new_events)
print("지속 이상:", ongoing_events)