from random import choice

import requests

file_path = '../user_agent.txt'
with open(file_path, 'r') as file:
    proxys = file.read().split('\n')

headers = {
    'user-agent': choice(proxys),
    'x-requested-with': 'XMLHttpRequest'
}

data = {
    'GiveName': 'Tinkoff',
    'GetName': 'Monero',
    'Sum': 10000,
    'Direction': 0
}

url = 'https://bitality.cc/Home/GetSum?'

response = requests.get(url=url, headers=headers, params=data).json()

print(response)
