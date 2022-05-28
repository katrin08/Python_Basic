def func(first, second):
    new_string = ''
    for i in range(1, len(first) + 1):
        if first != new_string:
            new_string = second[-i:] + second[:-i]
        else:
            print('\nПервая строка получается из второй со сдвигом', i-1)
            return True


first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')


if not func(first_string, second_string):
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
