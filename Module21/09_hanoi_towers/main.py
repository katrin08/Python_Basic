def tower(number, start, finish):
    if number <= 0:
        return
    support = 6 - start - finish
    tower(number - 1, start, support)
    print('Переложить диск', number, 'со стержня номер', start, 'на стержень номер', finish)
    tower(number - 1, support, finish)

count = int(input('Введите количество дисков: '))
tower(count, 1, 3)
