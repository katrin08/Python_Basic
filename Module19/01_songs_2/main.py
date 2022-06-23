violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

summ_song = 0
count_song = int(input('Сколько песен выбрать? '))

for num in range(count_song):
    name_song = input(f'Название {num+1}-ой песни: ')
    for i_song, i_time in violator_songs.items():
        if name_song == i_song:
            summ_song += i_time

print('Общее время звучания песен:', round(summ_song, 2), 'минуты')
