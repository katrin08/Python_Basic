def func(n, number):
    if n == number:
        return number
    print(n)
    return func(n+1, number)


num = int(input('Введите num: '))
start = 1
print(func(start, num))