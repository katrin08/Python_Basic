def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def invert_dict(hist, i):
    sym_list.clear()
    new_dict.clear()
    for i_keys, i_val in hist.items():
        if i_val == i:
            sym_list.append(i_keys)
    new_dict[i+1] = sym_list
    for i_keys_new, i_val_new in new_dict.items():
        print(i_keys_new, ':', i_val_new)


text = input('Введите текст: ').lower()
hist = histogram(text)
new_dict = dict()
sym_list = list()

print('\nОригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, '-', hist[i_sym])

maximum = max(hist.values())
print('\nИнвертированный словарь частот:')
for i in range(maximum):
    invert_dict(hist, i+1)
