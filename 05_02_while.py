############################

# target = 7
# num = 0

# while num != target:
#     num = int(input("숫자를 입력하세요: "))

# print("정답입니다!")

############################

found = False

count = int(input("측정값 개수 입력: "))

for i in range(count):
    value = int(input("측정값 입력: "))

    if value > 80:
        found = True
        break

if found:
    print("발견")
else:
    print("없음")