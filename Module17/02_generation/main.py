length = int(input('Введите длину списка: '))

answer = [1 if number % 2 == 0 else number % 5 for number in range(length)]

print('Результат:', answer)
