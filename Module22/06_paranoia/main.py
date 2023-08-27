import os

def cipher(path, file):
    print('Содержимое файла', file)
    text_file = open(path, 'r')
    step = 0
    for i_line in text_file:
        print(i_line, end='')
        step += 1
        txt = ''
        for symbol in i_line:
            for index, elem in enumerate(alphabet):
                if symbol.lower() == elem:
                    index = index + step
                    if index > len(alphabet):
                        index = index-len(alphabet)
                    if symbol.isupper():
                        txt += alphabet[index].upper()
                    else:
                        txt += alphabet[index]

        func_save('\n'+ txt)
    text_file.close()

def func_save(txt):
    file_name = 'cipher_text.txt'
    save_file = open(file_name, 'a')
    save_file.write(txt)
    save_file.close()


alphabet = list('abcdefghijklmnopqrstuvwxyz')
file = 'text.txt'
path_file = os.path.abspath(os.path.join('..', file))

cipher(path_file, file)

print('\nСодержимое файла cipher_text.txt:', end='')
answer = open(os.path.abspath('cipher_text.txt'), 'r')
for line in answer:
    print(line, end='')
answer.close()
