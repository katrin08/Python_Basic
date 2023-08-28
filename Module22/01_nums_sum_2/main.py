def func_open(file_name):
    numbers_sum = 0
    file_num = open(file_name, 'r', encoding='utf-8')
    for i_line in file_num:
        data = i_line.split()
        if data:
            for elem in data:
                numbers_sum += int(elem)
    file_num.close()

    return numbers_sum


def func_answer(answer):
    file_answer = open('answer.txt', 'w')
    file_answer.write(answer)
    file_answer.close()


result = func_open('numbers.txt')
func_answer(str(result))
