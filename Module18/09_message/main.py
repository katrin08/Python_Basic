text = input('Сообщение: ')
answer = ''
revers = ''
word = ''

for symbol in text:
    if symbol.isalpha():
        word += symbol
    else:
        revers = word[::-1]
        answer += revers + symbol
        word = ''

print('Новое сообщение: ', answer)
