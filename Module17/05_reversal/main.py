def func_sort(string):
    for i in range(len(string)):
        if string[i] == 'h':
            return i


text = input('Введите строку: ')
finish = func_sort(text[::-1])
start = func_sort(text)

if finish == 0:
    finish = -2

print('Развёрнутая последовательность между первым и последним h:', text[finish:start:-1])
