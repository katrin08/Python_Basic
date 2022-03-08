def func_contrast(number):
    sum_contrast = 0
    while number != 0:
        ost = number % 10
        sum_contrast = sum_contrast * 10 + ost
        number //= 10
    return sum_contrast


def func(number):
    whole_part = ''
    fractional_part = ''
    count = 0
    flag = True
    for num in number:
        if num == '.':
            flag = False
        elif flag:
            whole_part += num
        else:
            fractional_part += num
            count += 1
    whole_part = func_contrast(int(whole_part))
    fractional_part = func_contrast(int(fractional_part))
    contrast_summ = whole_part + (fractional_part * 10 ** (-count))
    return contrast_summ


number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
contrast_number_1 = func(number_1)
print('\nПервое число наоборот:', contrast_number_1)
contrast_number_2 = func(number_2)
print('Второе число наоборот:', contrast_number_2)
print('Сумма:', contrast_number_1 + contrast_number_2)
