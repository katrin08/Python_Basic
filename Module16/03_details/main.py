shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
count_detail = 0
total_summa = 0
detail = input('Название детали: ')

for i in range(len(shop)):
    if shop[i][0] == detail:
        total_summa += shop[i][1]
        count_detail += 1

print('Кол-во деталей — ', count_detail)
print('Общая стоимость — ', total_summa)
