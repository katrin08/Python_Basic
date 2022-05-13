def func_sort(symbol):
    list_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    for i_list in list_letters:
        if i_list == symbol:
            return True
    return False


text = input('Введите текст: ')
answer_list = [text[i] for i in range(len(text)) if func_sort(text[i])]
print('Список гласных букв:', answer_list)
print('Длина списка:', len(answer_list))
