skates_list = []
people_list = []
coincidence = 0
skates_count = int(input('Кол-во коньков: '))
for i_skates in range(skates_count):
    skates = int(input(f'Размер {i_skates+1} пары:'))
    skates_list.append(skates)

people_count = int(input('Кол-во людей: '))
for i_people in range(people_count):
    people = int(input(f'Размер ноги {i_people+1} человека:'))
    people_list.append(people)
print(skates_list, people_list)

for _ in range(skates_count):
    min_skates = min(skates_list)
    min_peoples = min(people_list)
    if min_skates >= min_peoples:
        coincidence += 1
        skates_list.remove(min_skates)
        people_list.remove(min_peoples)
    else:
        skates_list.remove(min_skates)

print('Наибольшее кол-во людей, которые могут взять ролики:', coincidence)
