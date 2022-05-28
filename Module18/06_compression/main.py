
string = list(input('Введите строку: '))

code_string = ''
count_sym = 1

for i_sym in range(len(string)):
    if i_sym == len(string) - 1:
        code_string += string[i_sym] + str(count_sym)
    else:
        if string[i_sym] == string[i_sym + 1]:
            count_sym += 1
        else:
            code_string += string[i_sym] + str(count_sym)
            count_sym = 1


print(code_string)


