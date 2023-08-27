import os


def size_dir(cur_path):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            list_size[0] += os.path.getsize(path)/1024
            list_size[1] += 1
        if os.path.isdir(path):
            size_dir(path)
            list_size[2] += 1


path_dir = os.path.abspath(os.path.join('..', '..', 'Module14'))
print(path_dir)
list_size = [0, 0, 0]
size_dir(path_dir)

print('Размер каталога (в Кб):', list_size[0])
print('Количество подкаталогов:', list_size[2])
print('Количество файлов:', list_size[1])
