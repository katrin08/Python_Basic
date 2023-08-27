import os


def func_verification(path, text, file):
    if os.path.exists(path):
        if os.path.exists(os.path.abspath(os.path.join(path,file))):
            answer = input('Вы действительно хотите перезаписать файл?').lower()
            if answer == 'да':
                print('Файл успешно перезаписан!')
                func_save(path, text, file)
            else:
                print('Изменения не сохранены')
        else:
            print('Файл успешно сохранён!')
            func_save(path,text, file)
    else:
        print('Такого пути не существует')


def func_save(path, text, file):
    file_path = os.path.abspath(os.path.join(path, file))
    file_save = open(file_path, 'w')
    file_save.write(text)
    file_save.close()


text = input('Введите строку: ')
text_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):').split()
#Users Екатерина PycharmProjects Python_Basic Module22
name_file = input('Введите имя файла: ') + '.txt'

dir_path = os.path.abspath(os.path.join(os.sep, *text_path))
print(dir_path)

func_verification(dir_path, text, name_file)
