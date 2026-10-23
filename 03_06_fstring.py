####################

# equipment = 'PUMP_A'
# temp = 87

# print(f'설비 {equipment}, 온도 {temp}도')

####################

# score1 = 80
# score2 = 90
# score3 = 91

# print(f'평균 {(score1 + score2 + score3) / 3}')

####################

# value = 87.456

# print(f'{value:.1f}')
# print(f'{value:.2f}')

####################

log = ' 5, sensor_2, WARNING, 0.78912 '

parts = log.split(',')

sensor = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())

print(f'[센서 {sensor}] 상태 {status}, 측정값 {value:.2f}')

####################
