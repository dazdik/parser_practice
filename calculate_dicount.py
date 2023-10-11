import lxml
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/hdd/4/4_1.html'

response = requests.get(url=url)


def calculate_discount(html: str) -> float:
    soup = BeautifulSoup(html, 'lxml')
    old_price = int(soup.find('span', id='old_price').text.split()[0])
    current_price = int(soup.find('span', id='price').text.split()[0])
    discount = (old_price - current_price) * 100 / old_price
    return round(discount, 1)


print(f'Размер скидки составляет: {calculate_discount(response.text)}%')
