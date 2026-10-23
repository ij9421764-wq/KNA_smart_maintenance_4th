#################

# text = "설비 정상 가동"
# result = text.replace("정상", "점검")

# print(result)

#################

# text = "PUMP A 03"
# result = text.split()

# print(result)

#################

# text = "a,b,c,d"
# result = text.split(',')

# print(result)

#################

# text = "a,b,c,d"

# result = text.split(",", 1)

# print(result)

#################

# date_list = ['2025', '01', '15']

# result = '-'.join(date_list)

# print(result)

#################

# print(2025, 1, 15, sep='-')
# print(2025, 1, 15, sep=',')

#################

# date = '2025/01/15'

# result = '-'.join(date.split('/'))

# print(result)

#################

data = '1, NORMAL, 25.3'

choice_value = data.split(',')[1].strip().lower()

print(choice_value)