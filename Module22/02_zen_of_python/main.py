import os


def open_file(file_name):
    list = []
    text_file = open(file_name, 'r')
    for i_line in text_file:
        list.append(i_line)
    text_file.close()
    return list


text_list = open_file('zen.txt')

for index in range(len(text_list)-1, -1, -1):
    print(text_list[index], end='')
