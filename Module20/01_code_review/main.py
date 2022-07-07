students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    string = ''
    lst = set(j for i in dict for j in dict[i]['interests'])
    for i in dict:
        string += dict[i]['surname']
    return lst, len(string)


pairs = []
for i in students:
    pairs.append((i, students[i]['age']))

my_lst, l = f(students)
print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов: ', my_lst)
print('Общая длина всех фамилий студентов:', l)
