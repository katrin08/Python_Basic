def func(name):
    error_list = list('@№$%^&*()')
    for i_sym in error_list:
        if name.startswith(i_sym):
            return True


file_name = input('Название файла: ')

if func(file_name):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith('.txt' or '.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')

