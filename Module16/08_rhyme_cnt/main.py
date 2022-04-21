start = 1
count = 0
n = int(input('Кол-во человек: '))
list_number = list(range(1, n + 1))
k = int(input('Какое число в считалке? '))

while len(list_number) > 1:
    print('\nТекущий круг людей:', list_number)
    print('Начало счёта с номера', start)
    delete = (count + k - 1) % len(list_number)
    print('Выбывает человек под номером', list_number[delete])
    list_number.remove(list_number[delete])
    count = delete
    start = k % len(list_number)
    if delete == -1:
        count = 0
    else:
        count = delete

print('\nОстался человек под номером ', list_number[0])
