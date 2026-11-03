# with open("data/test.txt", "w", encoding="utf-8") as f:
#     f.write("첫 번째 줄\n")
#     f.write("두 번째 줄\n")

# with open("data/test.txt", "r", encoding="utf-8") as f:
#     print(f.read())

######################################

# with open("data/test.txt", "w", encoding="utf-8") as f:
#     f.write("세 번째 줄\n")

# with open("data/test.txt", "r", encoding="utf-8") as f:
#     print(f.read())

######################################

# import csv

# with open("data/08_press_13_261029_3.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)

######################################

# import csv

# with open("data/result.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)

#     writer.writerow(["시각", "설비"])
#     writer.writerow(["09:00", "pump-01"])
#     writer.writerow(["10:00", "pump-02"])

######################################

import csv

result = []

with open("data/08_press_13_261029_3.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)

    for row in reader:
        score = float(row[-2])

        # 전류 값으로 진행
        if score > 90:
            result.append(row)
            
with open("data/electric_result.csv", "w", encoding="utf-8", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(header)

    for row in result:
        writer.writerow(row)