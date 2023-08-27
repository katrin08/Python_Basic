import os


def func_analis(path):
    symbol_dict = {}
    text_file = open(path, 'r')
    text = text_file.read()
    print('Содержимое файла text.txt:')
    print(text)
    for symbol in text.lower():
        if symbol.isalpha():
            if not symbol in symbol_list:
                symbol_list.append(symbol)

    string = [sym.lower() for sym in text if sym.isalpha()]

    for elem in symbol_list:
        symbol_dict[elem] = round((string.count(elem)/len(string)), 3)
    text_file.close()
    sort_dict = dict(sorted(symbol_dict.items(), key=lambda key: (-key[1], key[0])))
    func_save(sort_dict)


def func_save(sort_dict):
    analis_data = open('analysis.txt', 'a')
    for key, value in sort_dict.items():
        analis_data.write(f'{key} {str(value)}\n')


file_path = os.path.abspath('text.txt')
print(file_path)
symbol_list = []
func_analis(file_path)

analis_data = open('analysis.txt', 'r')
print('\nСодержимое файла analysis.txt:')
for i_line in analis_data:
    print(i_line, end='')
analis_data.close()
