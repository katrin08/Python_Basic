def func_len(*args):
   return len(min(*args, key=len))


def func(count, my_list):
    answer = tuple(i_elem[count] for i_elem in my_list)
    return answer


def func_type(*args):
    new_list = [list(element) for element in args]
    return new_list


string = 'abcd'
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40)
my_dict = {'один':1, 'два':2, 'три':3, 'четыре':4}

new_ans = [func(index, func_type(string, my_list, my_tuple, my_dict))
           for index in range(func_len(string, my_list, my_tuple, my_dict))]
print(new_ans)