def transl_1(text_1):
    translated_1 = ''
    step = 1
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for sym in text_1:
        if sym in letters:
            number = letters.find(sym)
            translated_1 += letters[number - step]
        else:
            translated_1 += sym
    return translated_1


def transl_2(text_2):
    translated_2 = ''
    shift = 3
    text_list = text_2.split()
    for word in text_list:
        new_word = ''
        for i_word in range(len(word)):
            new_word += (word[i_word - shift % len(word)])
            if new_word.endswith('/'):
                shift += 1

        translated_2 += new_word + ' '

    return translated_2


text = input('Введите текст: ')

transl_1 = transl_1(text)
answer = transl_2(transl_1)


print(answer.replace('/', '\n'))
