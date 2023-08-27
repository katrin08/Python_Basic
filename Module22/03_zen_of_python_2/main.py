import os


path = os.path.abspath('zen.txt')
count_line = 0
count_symbol = 0
count_word = 0
text = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

file = open(path, 'r')
for i_line in file:
    count_symbol += len(list(letter for letter in i_line if letter.isalpha()))
    data = i_line.split()
    count_word += len(data)
    if data:
        count_line += 1
        for i_elem in i_line:
            if i_elem.lower() in alphabet:
                text += i_elem.lower()

file.close()

print('Количество букв в файле: ', count_symbol)
print('Количество слов в файле: ', count_word)
print('Количество строк в файле:', count_line)
print('Наиболее редкая буква:', min(text, key=text.count))
