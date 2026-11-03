
# try:
#     f = open("data/09_ict_inspection_15_261102_1.csv", "r")
#     print(f.read())

#     10 / 0

# except Exception as e:
#     print("오류 발생:", e)

# finally:
#     if f:
#         f.close()
#     print("파일 닫기 완료")

#####################################

# try:
#     with open("data/09_ict_inspection_dirty_15_261102_2.csv", encoding="utf-8") as f:
#         rows = f.readlines()[1:]
# except FileNotFoundError:
#     rows = []

# total = 0.0
# skipped = 0

# for line in rows:
#     try:
#         total += float(line.split(",")[2])
#     except (ValueError, IndexError):
        
#         pass
#         # skipped += 1
#         continue

# print("합계:", round(total, 1), "/건너뜀:", skipped)

#####################################


# files = ["data/09_ict_inspection_15_261102_1.csv", "data/non_test.csv", "data/09_ict_inspection_dirty_15_261102_2.csv"]

# done = 0

# for file in files:
#     try:
#         with open(file, encoding="utf-8") as f:
#             rows = f.readlines()[1:]

#         print(f"{file} : {len(rows)}행\n")
#         done += 1

#     except FileNotFoundError:
#         print(f"[파일 없음] {file}\n")
#         continue

# print("처리한 파일:", done)

#####################################

def check_value(text, lo=0.0, hi=5000.0):
    v = float(text)

    if v < lo or v > hi:
        raise ValueError(f"범위 밖 값 -> {v}")

    return v


for t in ["128.5", "결측", "-999"]:
    try:
        print("통과:", check_value(t))
    except ValueError as e:
        print("제외:", e)