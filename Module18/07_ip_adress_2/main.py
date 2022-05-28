def func(ip):
    ip_list = ip.split('.')
    for num in ip_list:
        if len([i for i in num if i.isalpha()]) != 0:
            print(num, '- это не целое число.')
            return False
        elif int(num) < 0:
            print(num, 'меньше 0.')
            return False
        elif int(num) > 255:
            print(num, 'превышает 255')
            return False
        elif len(ip_list) != 4:
            print('Адрес — это четыре числа, разделённые точками.')
            return False
    return True


ip = (input('Введите IP: '))

if func(ip):
    print('IP-адрес корректен.')








