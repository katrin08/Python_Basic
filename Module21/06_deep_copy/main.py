import copy
import json
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def func_copy(struct, key, change):
    if key in struct:
        struct[key] = change
        return site
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = func_copy(sub_struct, key, change)
            if result:
                return site


count_site = int(input('Сколько сайтов: '))
site_product = dict()

for _ in range(count_site):
    name = input('Введите название продукта для нового сайта:')
    dict_key = {'title': f'Куплю/продам {name} недорого', 'h2': f'У нас самая низкая цена на {name}'}
    for val in dict_key:
        func_copy(site, val, dict_key[val])
    product = f'Сайт для {name}'
    copy_site = copy.deepcopy(site)
    site_product[product] = copy_site
    for i_key, i_val in site_product.items():
        print('site = ', json.dumps(site_product[i_key], ensure_ascii=False, indent=4))
