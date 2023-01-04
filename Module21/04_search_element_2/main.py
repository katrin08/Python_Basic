site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth):
    if depth >= 1:
        if key in struct:
            return struct[key]
    else:
        return 'None'
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


user_key = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if answer == 'y':
    lvl = int(input('Введите максимальную глубину:'))
    value = find_key(site, user_key, lvl)
else:
    value = find_key(site, user_key, depth = 10000)
if value:
    print('Значение ключа:', value)
else:
    print('Такого ключа в структуре сайта нет')
