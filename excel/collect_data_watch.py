import csv

import requests
from bs4 import BeautifulSoup

with open('watch.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
                     'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
                     'Ссылка на карточку с товаром'])


def get_soup(relative_path) -> BeautifulSoup:
    response = requests.get(url=f'https://parsinger.ru/html/{relative_path}')
    response.encoding = 'utf-8'

    return BeautifulSoup(response.text, 'lxml')


def get_item_links() -> list:
    links = []
    for i in range(1, 5):
        soup = get_soup(f'index1_page_{i}.html')
        links += [tag['href'] for tag in soup.find('div', class_='item_card').find_all('a', class_='name_item')]
    return links


def get_data() -> tuple[list, list, list, list, list, list, list]:
    headers = []
    articles = []
    descriptions = []
    in_stock = []
    prices = []
    old_prices = []
    urls = []
    links = get_item_links()

    for link in links:
        soup = get_soup(link)
        headers += [header.text.strip() for header in soup.find('p', id='p_header')]
        articles += [article.text.split(': ')[1].strip() for article in soup.find('p', class_='article')]
        descriptions += [x.text.split('\n') for x in soup.find_all('ul', id='description')]
        in_stock += [x.text.split(': ')[1] for x in soup.find('span', id='in_stock')]
        prices += [price.text for price in soup.find('span', id='price')]
        old_prices += [old.text for old in soup.find('span', id='old_price')]
        urls += [f'https://parsinger.ru/html/{link}']

    return headers, articles, descriptions, in_stock, prices, old_prices, urls


with open('watch.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    headers, articles, descriptions, in_stock, prices, old_prices, urls = get_data()
    for item, article, descr, stock, price, old_price, url in zip(
            headers, articles, descriptions, in_stock, prices, old_prices, urls):

        # Формируем строку для записи
        flatten = item, article, *[x.split(':')[1].strip() for x in descr if x], stock, price, old_price, url
        writer.writerow(flatten)

print('Файл watch.csv создан')
