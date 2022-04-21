def func_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


first_class = []
second_class = []
first_class.extend(list(range(160, 176, 2)))
second_class.extend(list(range(162, 181, 3)))
first_class.extend(second_class)

func_sort(first_class)
print('Отсортированный список учеников: ', first_class)
