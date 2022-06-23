number_of_men = int(input('Введите количество человек: '))
family = dict()
count = 0

for i_men in range(1, number_of_men):
    pair = input(f'{i_men}-я пара: ').split()
    if pair[1] in family:

        family[pair[0]] = family[pair[1]] + 1
    else:
        family[pair[1]] = count
        count += 1
        family[pair[0]] = count

print('\n«Высота» каждого члена семьи:')

for i_keys, i_val in sorted(family.items()):
    print(i_keys, i_val)
