def func(number):
    for num in range(2, number + 1):
        if number % num == 0:
            print('Наименьший делитель, отличный от единицы:', num)
            break


def menu():
    number = int(input('Введите число: '))
    if number > 1:
        func(number)
    else:
        print('Ошибка ввода')
        menu()


menu()
