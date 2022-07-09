def tpl_sort(tup):
    if func_verivication(tup):
        return tuple(sorted(tup))
    else:
        return tup


def func_verivication(tup):
    for elem in tup:
        if not isinstance(elem, int):
            return False
    return True


print(tpl_sort((6, 3, -1, 8, [4, 10], -5, 4)))
