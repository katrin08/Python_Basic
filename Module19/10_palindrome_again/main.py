def func_poll(string):
    sym_dict = dict()
    for i_sym in string:
        sym_dict[i_sym] = sym_dict.get(i_sym, 0) + 1

    sym_count = 0
    for i_val in sym_dict.values():
        if i_val % 2 != 0:
            sym_count += 1

    return sym_count <= 1

string = input('Введите строку: ')
if func_poll(string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')