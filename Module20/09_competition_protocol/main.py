def func(result, data):
    for i_keys, i_val in data.items():
        if i_keys == result[1]:
            return max(int(i_val), int(result[0]))


def sort(data):
    sort_list = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return dict(sort_list)


data = dict()
num_count = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')

for i_num in range(num_count):
    data = sort(data)
    result = input(f'{i_num+1}-я запись: ').split()
    if result[1] in data:
        data[result[1]] = int(func(result, data))
    else:
        data[result[1]] = int(result[0])

print('\nИтоги соревнований:')
answer = dict(list(data.items())[:3])
i_rec = 1
for i_play, ball in answer.items():
    print(f'{i_rec}-e место. {i_play} ({ball})')
    i_rec += 1
