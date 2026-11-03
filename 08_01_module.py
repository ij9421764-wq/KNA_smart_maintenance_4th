# 모듈 / 패키지/ 라이브러리
# 모듈 : 기능을 모아둔 .py 파일 하나
# 패키지 : 모듈을 모아둔 폴더
# 라이브러리 : 위에 사항들을 통칭


###############################

# import math
# print(math.sqrt(16))

# from math import sqrt
# print(sqrt(16))

# import math as m
# print(m.sqrt(16))

###############################

# import random
# import math

# sensor = random.randint(1, 100)

# print("센서값:", sensor)
# print("제곱근:", math.sqrt(sensor))

###############################

# import os

# print("현재 경로:", os.getcwd())

# print("========================")

# files = os.listdir()

# print("전체 파일 목록")
# for f in files:
#     print(f)

# if os.path.exists("data"):
#     files = os.listdir("data")
    
#     print("========================")

#     print("CSV 파일")
    
#     for f in files:
#         if f.endswith(".csv"):
#             print(f)

###############################

# import os

# folder = "data"
# filename = "08_press_13_261029_3.csv"

# path = os.path.join(folder, filename)

# print("경로:", path)
# print("존재 여부:", os.path.exists(path))

# if os.path.exists(path):
#     print("파일 있음")
# else:
#     print("파일 없음")

###############################

# import os
# from datetime import datetime

# files = os.listdir()
# file_count = len(files)

# check_time = datetime.now()

# print(f"파일 {file_count}개, 점검 시각 {check_time}")

###############################

import os

files = os.listdir('data')

csv_files = []

for file in files:
    if file.endswith(".csv"):
        csv_files.append(
            os.path.join(os.getcwd(), 'data', file)
        )

print("[CSV 목록]")

for csv_file in csv_files:
    print(csv_file)