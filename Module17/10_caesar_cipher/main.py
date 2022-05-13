def caesar(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    answer = [(alphabet[(alphabet.index(symbol) + shift) % 33] if symbol != ' ' else ' ') for symbol in text]
    new_str = ''
    for i_char in answer:
        new_str += i_char

    return new_str


text = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))

answer_str = caesar(text, step)
print('Зашифрованное сообщение:', answer_str)
