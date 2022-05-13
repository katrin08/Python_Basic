import random

count_number = int(input('Количество палок: '))
cast = int(input('Количество бросков: '))
answer = ''
list_sticks = ['I' for _ in range(count_number)]

for i_cast in range(cast):
    left_i = random.randint(0, count_number - 1)
    right_i = random.randint(left_i, count_number - 1)
    print('Бросок', str(i_cast + 1) + '. Сбиты палки с номера', left_i + 1, 'по номер', str(right_i + 1) + '.')
    for i_stics in range(left_i, right_i + 1):
        list_sticks[i_stics] = '.'

for i_answ in list_sticks:
    answer += i_answ

print(answer)
