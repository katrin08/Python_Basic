count_str = int(input('Количество стран: '))

country_dict = dict()
for i in range(count_str):
    string = input(f'{i+1}-ая страна: ').split()
    country_dict[string[0]] = string[1:]

for i_num in range(3):
    city = input(f'\n{i_num + 1}-й город: ')
    for i_country, i_city in country_dict.items():
        if city in i_city:
            print('Город {0} расположен в стране {1}.'.format(city, i_country))
            break
    else:
        print(f'По городу {city} данных нет.')
