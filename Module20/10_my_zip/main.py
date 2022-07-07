def min_len(str, tup):
    return min(len(str), len(tup))


def verification(data):
    if isinstance(data, list) or isinstance(data, str) or isinstance(data, dict) or isinstance(data, tuple):
        return list(data)


my_str = 'abcd'
nums_tpl = (10, 20, 30, 40)
print(my_str)
print(nums_tpl)
print('\nРезультат:')
my_str = verification(my_str)
nums_tpl = verification(nums_tpl)

pairs = (
    (my_str[index], nums_tpl[index])
    for index in range(min_len(my_str, nums_tpl))
)
print(pairs)
for elem in pairs:
    print(elem)
