def func_palindrom(num_list):
    revers_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        revers_list.append(num_list[i_num])
    if num_list == revers_list:
        return True
    else:
        return False


nums = []
new_list = []
answer_list = []
count_list = int(input('Кол-во чисел: '))

for _ in range(count_list):
    number = int(input('Число: '))
    nums.append(number)

print('\nПоследовательность:', nums)

for i_nums in range(0, len(nums)):
    for i_mn in range(i_nums, len(nums)):
        new_list.append(nums[i_mn])
    if func_palindrom(new_list):
        for i_answer in range(0, i_nums):
            answer_list.append(nums[i_answer])
        answer_list.reverse()
        break
    new_list = []

print('Нужно приписать чисел:', len(answer_list))
print('Сами числа:', answer_list)
