nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def func(nice_list):
    for elem in nice_list:
        if isinstance(elem, int):
            new_list.append(elem)
        else:
            func(elem)
    return


new_list = []

func(nice_list)
print(new_list)
