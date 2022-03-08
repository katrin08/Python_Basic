def func(number):
    numb_1 = number // 1000
    numb_2 = number // 100 % 10
    numb_3 = number % 100 // 10
    numb_4 = number % 10
    if numb_1 == numb_2 == numb_3 or numb_2 == numb_3 == numb_4 or numb_1 == numb_3 == numb_4:
        print(number)


start = int(input('Введите первый год: '))
finish = int(input('Введите второй год: '))
print('Года от', start, 'до', finish, 'с тремя одинаковыми цифрами:')
for numb in range(start, finish + 1):
    func(numb)
