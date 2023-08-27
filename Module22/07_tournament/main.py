import os


def func_first_tour(path):
    print('Содержимое файла first_tour.txt:')
    first_tour = open(path, 'r')
    ball = int(first_tour.readline())
    print(ball)
    for i_line in first_tour:
        print(i_line, end='')
        list_data =  i_line.split()
        if ball < int(list_data[2]):
            second_list.append(i_line.split())
    first_tour.close()
    sort_list = sorted(second_list, key=lambda human: human[2], reverse=True)
    func_save(sort_list)


def func_save(sort_list):
    second_tour = open('second_tour.txt', 'a')
    second_tour.write(str(len(sort_list)))
    for index, elem in enumerate(sort_list):
        result = ''
        result += f'\n{str(index+1)}) {elem[1][0]}.  {elem[0]}  {str(elem[2])}'
        second_tour.write(str(result))
    second_tour.close()


file_path = os.path.abspath(os.path.join('..', 'first_tour.txt'))
second_list = []
func_first_tour(file_path)

print()
print('\nСодержимое файла second_tour.txt:')
second_tour = open('second_tour.txt', 'r')
for i_line in second_tour:
    print(i_line, end='')
second_tour.close()