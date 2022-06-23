def func(word):
    for i_keys, i_val in word_dict.items():
        if word.lower() == i_keys.lower():
            return i_val
        elif word.lower() == i_val.lower():
            return i_keys
    else:
        return False


count_word = int(input('Введите количество пар слов: '))
word_dict = dict()

for i_count in range(1, count_word+1):
     string = input(f'{i_count}-ая пара: ').split(' — ')
     word_dict[string[0]] = string[1]

while True:
    word = input('Введите слово: ')
    if func(word):
        print('Синоним:', func(word))
        break
    else:
        print('Такого слова в словаре нет.')
