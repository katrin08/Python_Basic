def crypto(data):
    if isinstance(data, list) or isinstance(data, str) or isinstance(data, dict) or isinstance(data, tuple):
        return [i_val for i_keys, i_val in enumerate(data) if is_prime(i_keys) and i_keys > 1]


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
