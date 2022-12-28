def summ(*args, total_sum = 0):
    for elem in args:
        if isinstance(elem, int):
            total_sum += elem
        else:
            for i_elem in elem:
                total_sum += summ(i_elem)
    return total_sum


print('Ответ в консоли:', summ(1, 2, 3, 4, 5))
print('Ответ в консоли:', summ([[1, 2, [3]], [1], 3]))
