def func_sum(number):
    if number in (1, 2):
        return 1
    else:
        return func_sum(number-1) + func_sum(number-2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))

answer = (func_sum(number))
print('Число:', answer)
