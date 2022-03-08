
def func_summ(num):
    summa = 0
    while num != 0:
        ost = num % 10
        summa += ost
        num //= 10
    print('Сумма цифр:', summa)
    return summa


def func_count(numb):
    count = 0
    while numb != 0:
        count += 1
        numb //= 10
    print('Кол-во цифр в числе:', count)
    return count


number = int(input('Введите число: '))
total_summ = func_summ(number)
total_count = func_count(number)
print('Разность суммы цифр и кол-ва цифр:', total_summ - total_count)
