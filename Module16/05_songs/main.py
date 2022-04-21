violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
time = 0
count_music = int(input('Сколько песен выбрать? '))

for i in range(count_music):
    music = input(f'Название {i+1}-й песни:')
    for index in range(len(violator_songs)):
        if violator_songs[index][0] == music:
            time += violator_songs[index][1]

print('\nОбщее время звучания песен:', round(time, 2), 'минуты')
