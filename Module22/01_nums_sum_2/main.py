def func_open(file_name):
    numbers_sum = 0
    file_num = open(file_name, 'r', encoding='utf-8')
    for i_line in file_num:
        clear_line = i_line.strip()
        if clear_line:
            numbers_sum += int(clear_line)
    file_num.close()

    return numbers_sum


def func_answer(answer):
    file_answer = open('answer.txt', 'w')
    file_answer.write(answer)
    file_answer.close()


result = func_open('numbers.txt')
func_answer(str(result))
