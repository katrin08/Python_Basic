import math


def func(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    if r < distance:
        print('Монетки в области нет')
    else:
        print('Монетка где-то рядом')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
func(x, y)
