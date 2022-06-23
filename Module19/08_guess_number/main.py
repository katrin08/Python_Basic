n = int(input('Введите максимальное число: '))
string = ''
new_numbers = {num for num in range(1, n+1)}

while True:
    string = input('Нужное число есть среди вот этих чисел: ').lower()
    if string != 'помогите!':
        numbers = set(string.split())
        answer = input('Ответ Артёма: ').lower()
        if answer == 'да':
            new_numbers = numbers
        elif answer == 'нет':
            new_numbers = new_numbers - numbers
    else:
        print('Артём мог загадать следующие числа:', end=' ')
        for i_num in sorted(new_numbers):
            print(i_num, end=' ')
        break



