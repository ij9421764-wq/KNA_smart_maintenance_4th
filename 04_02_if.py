#################

# age = int(input("나이를 입력하세요: "))

# if age >= 19:
#     print("성인입니다")
# else:
#     print("미성년자입니다")
    
#################

# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")

#################

# temperature = int(input("온도를 입력하세요: "))

# if temperature > 80:
#     print("위험")
# elif temperature > 60:
#     print("주의")
# else:
#     print("정상")
    
#################

# correct_id = "admin"
# correct_pw = "1234"

# user_id = input("아이디를 입력하세요: ")
# user_pw = input("비밀번호를 입력하세요: ")

# if user_id == correct_id and user_pw == correct_pw:
#     print("로그인 성공")
# else:
#     print("로그인 실패")
    
#################

temperature = int(input("온도: "))
vibration = float(input("진동: "))
electric = int(input("전류: "))

if temperature > 80 or vibration > 4.0:
    print("위험: 즉시 정지")
elif electric > 60 and temperature > 70:
    print("주의: 부하 점검")
elif vibration > 2.5:
    print("주의: 진동 관찰")
else:
    print("정상")