import random

first_team = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
print('Первая команда:', first_team)
second_team = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
print('Вторая команда:', second_team)

winner_team = [first_team[i] if first_team[i] > second_team[i] else second_team[i] for i in range(20)]
print('Победители тура:', winner_team)
