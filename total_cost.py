import lxml
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.3/5/index.html'

response = requests.get(url=url)

response.encoding = 'utf-8'


def calculate_total_price(html: str) -> float:
    # Инициализация BeautifulSoup.
    soup = BeautifulSoup(html, 'lxml')
    price_for_all = soup.find_all('p', class_='count price')
    total_count = soup.find_all('p', class_='count stock')
    total_price = 0
    for price, count in zip(price_for_all, total_count):
        total_price += (float(price.text.split('$')[1]) * int(count.text.split(': ')[1]))

    return total_price


print(f"Общая стоимость в случае продажи всех товаров: ${calculate_total_price(response.text)}")
