list_friends = []
count_friends = int(input('Кол-во друзей: '))
count_receipts = int(input('Долговых расписок: '))

for index in range(1, count_friends+1):
    list_friends.append([index, 0])

for i_receipts in range(1, count_receipts+1):
    print()
    print(str(i_receipts) + '-я расписка')
    debtor = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    gold = int(input('Сколько: '))
    list_friends[debtor-1][1] -= gold
    list_friends[from_whom-1][1] += gold

print('\nБаланс друзей:')
for i_friends in range(len(list_friends)):
    print(list_friends[i_friends][0], ':', list_friends[i_friends][1])
