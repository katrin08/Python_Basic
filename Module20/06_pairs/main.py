import random

origin_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', origin_list)
new_list = [
    (origin_list[i], origin_list[i+1])
    for i in range(0, len(origin_list), 2)
]
print('Новый список:', new_list)

new_list_2 = [
    (origin_list[i_keys], origin_list[i_keys + 1])
    for i_keys, i_val in enumerate(origin_list)
    if i_keys % 2 == 0
]
print('Новый список:', new_list_2)
