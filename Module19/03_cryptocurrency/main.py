data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
list_keys = list()
list_val = list()

for i in data.keys():
    list_keys.append(i)
for i_eth in data['ETH'].keys():
    list_keys.append(i_eth)
for i_tok_1 in data['tokens'][0].keys():
    list_keys.append(i_tok_1)
for i_tok_1_2 in data['tokens'][0]['fst_token_info'].keys():
    list_keys.append(i_tok_1_2)
for i_tok_2_1 in data['tokens'][1].keys():
    list_keys.append(i_tok_2_1)
for i_tok_2_2 in data['tokens'][1]['sec_token_info'].keys():
    list_keys.append(i_tok_2_2)


for i in data.values():
    list_val.append(i)
for i_eth in data['ETH'].values():
    list_val.append(i_eth)
for i_tok_1 in data['tokens'][0].values():
    list_val.append(i_tok_1)
for i_tok_1_2 in data['tokens'][0]['fst_token_info'].values():
    list_val.append(i_tok_1_2)
for i_tok_2_1 in data['tokens'][1].values():
    list_val.append(i_tok_2_1)
for i_tok_2_2 in data['tokens'][1]['sec_token_info'].values():
    list_val.append(i_tok_2_2)


print('Список ключей: ', list_keys)
print('\nСписок значений', list_val)

data['ETH']['total_diff'] = 100
data['tokens'][0]['fst_token_info']['name'] = 'doge'
memory = data['tokens'][0].pop('total_out')
data['tokens'][1].pop('total_out')
data['ETH']['total_out'] = memory
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')


