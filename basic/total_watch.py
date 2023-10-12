import lxml
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)

response.encoding = 'utf-8'


def total_cost(html: str) -> int:
    soup = BeautifulSoup(html, 'lxml')
    price_all = soup.find_all('p', class_='price')
    return sum(int(price.text.split()[0]) for price in price_all)


print(f'Сумма всех часов на странице {total_cost(response.text)} руб.')
