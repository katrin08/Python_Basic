def func_add(phonebook):
    name = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
    if verivication(name, phonebook):
        print('Такой человек уже есть в контактах.')
    else:
        phonebook[tuple(name)] = int(input('Введите номер телефона: '))
    print('Текущий словарь контактов:', phonebook)
    return phonebook


def func_search(phonebook):
    name_search = input('Введите фамилию для поиска: ').title()
    for i_name, i_num in phonebook.items():
        if name_search in i_name or name_search in i_name:
            print(i_name[0],i_name[1], i_num)


def verivication(name, phonebook):
    for elem in phonebook.keys():
        if tuple(name) == elem:
            return True
    return False


phonebook = dict()
while True:
    print('\nВведите номер действия:')
    print('1. Добавить контакт')
    print('2. Найти человека')
    action = int(input())
    if action == 1:
        func_add(phonebook)
    elif action == 2:
        func_search(phonebook)
    else:
        print('Ошибка ввода')
