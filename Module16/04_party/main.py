guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) >= 6:
            print('Прости,', name+', но мест нет.')
        else:
            print('Привет,', name)
            guests.append(name)
    if answer == 'ушел':
        name = input('Имя гостя: ')
        print('Пока,', name)
        guests.remove(name)
    if answer == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
