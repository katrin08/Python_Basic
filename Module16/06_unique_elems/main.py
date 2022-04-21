def func(n, list_n):
    list_number = []
    for i in range(n):
        number = int(input(f'Введите {i+1}-е число для {list_n} списка: '))
        list_number.append(number)
    return list_number


first_list = func(3, 'первого')
second_list = func(7, 'второго')
print('\nПервый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

ind = 0
while ind < len(first_list):
    x = first_list[ind]
    count_x = first_list.count(x)
    ind += 1
    for _ in range(count_x - 1):
        first_list.remove(x)
        ind -= 1

print('\nНовый первый список с уникальными элементами:', first_list)
