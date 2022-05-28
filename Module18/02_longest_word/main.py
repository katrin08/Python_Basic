text = input('Введите строку: ').split(' ')
max_sym = text[0]

for word in text:
    if len(word) > len(max_sym):
        max_sym = word

print('Самое длинное слово:', max_sym)
print('Длина этого слова:', len(max_sym))
