def func_count(i_key):
        total_sum = 0
        sum_quan = 0
        for i in range(len(goods_new[i_key])):
            sum_quan += goods_new[i_key][i]['quantity']
            total_sum += goods_new[i_key][i]['quantity'] * goods_new[i_key][i]['price']
        return i_key, sum_quan, total_sum


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

goods_new = dict()
for keys_goods, val_goods in goods.items():
    for keys_store, val_store in store.items():
        if val_goods == keys_store:
            goods_new[keys_goods] = val_store
sum_quan = 0

for i_key in goods_new.keys():
    key, sum, total_sum = func_count(i_key)
    print(key, '-',  sum, 'штук, стоимость', total_sum, 'рублей')

