def slicer(tup, sym):
    if sym in tup:
        sym_list = [index for index, elem in enumerate(tup) if elem == sym]
        if len(sym_list) > 1:
            new_tup = tup[sym_list[0]:sym_list[1]+1]
        else:
            new_tup = tup[sym_list[0]:]
    else:
        new_tup = ()

    return new_tup


symbol = int(input('Введите символ: '))
print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), symbol))
