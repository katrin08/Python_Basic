def func_up(word):
    for letter in word:
        if letter.isupper():
            return True
    return False


def func_dig(word):
    count = 0
    for sym in word:
        if sym.isdigit():
            count += 1
    if count >= 3:
        return True
    return False


password = input('Придумайте пароль: ')

while True:
    if len(password) >= 8 and func_up(password) and func_dig(password):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        password = input()
