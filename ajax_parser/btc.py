from random import randint

import requests
from fake_useragent import UserAgent

ua = UserAgent(min_percentage=1.3)

headers = {
    'user-agent': ua.random,
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
