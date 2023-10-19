from collections import defaultdict

import requests
from fake_useragent import UserAgent


ua = UserAgent()
headers = {'User-Agent': ua.random}
url = 'https://parsinger.ru/4.6/1/res.json'
response = requests.get(url=url, headers=headers).json()

# Создать словарь, в котором ключами будут категории, а значениями - суммы произведений "article" и "rating"
res = defaultdict(int)
for item in response:
    name_category = item.get('categories')
    res[name_category] += (int(item['article']) * int(item['description']['rating']))

print(dict(res))




