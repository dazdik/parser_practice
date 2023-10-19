from collections import defaultdict

import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}
url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url, headers=headers).json()

res = defaultdict(int)

for item in response:
    name_category = item.get('categories')
    res[name_category] += (int(item['count']) * int(item['price'].split()[0]))

print(dict(res))
