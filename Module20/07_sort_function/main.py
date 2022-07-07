def tpl_sort(tup):
    if func_verivication(tup):
        return sorted(tup)
    else:
        return tup


def func_verivication(tup):
    for elem in tup:
        if elem != int(elem):
            return False
    return True


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
