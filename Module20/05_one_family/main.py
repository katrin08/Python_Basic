family = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Максим'): 16,
    ('Иванова', 'Маша'): 44,
    ('Смирнов', 'Сергей'): 28
}

surname = input('Введите фамилию: ').title()
print()
for i_name, age in family.items():
    if surname in i_name or surname+'а' in i_name:
        print(i_name[0], i_name[1], age)
