##############################

# N = int(input("N 입력: "))

# for i in range(1, N + 1):
#     print(i, end=" ")
# print()

# for i in range(2, N + 1, 2):
#     print(i, end=" ")
# print()

# for i in range(N, 0, -1):
#     print(i, end=" ")
    
##############################

# N = int(input("N 입력: "))

# total = 0

# for i in range(1, N + 1):
#     total += i

# print("합:", total)

##############################

# for dan in range(2, 10):
#     print(f"[{dan}단]")

#     for num in range(1, 10):
#         print(f"{dan} x {num} = {dan * num}")

#     print("-" * 15)
    
##############################

count = 0

n = int(input("측정 횟수 입력: "))

for i in range(n):
    value = int(input(f"{i+1}번째 값 입력: "))

    if value > 80:
        count += 1

print("초과 개수:", count)

