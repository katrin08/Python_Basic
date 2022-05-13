import random


def func_sort(number):
    if number == 0:
        return True
    return False


n = int(input('Количество чисел в списке: '))
list_number = [random.randint(0, 2) for _ in range(n)]
print('Список до сжатия:', list_number)
count_number = 0
for i in range(n):
    if func_sort(list_number[i]):
        list_number.append(0)
        list_number.remove(list_number[i])

list_number = [index for index in list_number if index != 0]
print('Список после сжатия: ', list_number)
