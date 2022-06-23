counts_order = int(input('Введите количество заказов: '))
orders_dict = dict()
order_list = list()

for i_order in range(1, counts_order +1):
    order_list.clear()
    order_list = input(f'{i_order}-й заказ: ').split()
    if order_list[0] in orders_dict.keys():
        if order_list[1] in orders_dict[order_list[0]].keys():
            summ_ord = orders_dict[order_list[0]][order_list[1]]
            orders_dict[order_list[0]][order_list[1]] = int(summ_ord) + int(order_list[2])
        else:
            orders_dict[order_list[0]][order_list[1]] = int(order_list[2])

    else:
        orders_dict[order_list[0]] = {
            order_list[1]: int(order_list[2])
        }


for i_name in orders_dict.keys():
    print(f'\n{i_name}:')
    for i_val in sorted(orders_dict[i_name].keys()):
        print(' ' * len(i_name), f'{i_val}:', orders_dict[i_name][i_val])
