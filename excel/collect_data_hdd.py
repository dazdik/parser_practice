import csv

import requests
from bs4 import BeautifulSoup

with open('res1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор',
                     'Ёмкость', 'Объем буферной памяти', 'Цена'])


def get_data():

    base_url = 'https://parsinger.ru/html/'
    name = []
    description = []
    price = []

    for i in range(1, 5):
        url = f'{base_url}index4_page_{i}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name += [name.text.strip() for name in soup.find_all('a', class_='name_item')]
        description += [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price += [price.text for price in soup.find_all('p', class_='price')]

    return name, description, price


with open('res1.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    name, description, price = get_data()
    for item, descr, price in zip(name, description, price):

        # Формируем строку для записи
        flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
        writer.writerow(flatten)

print('Файл res1.csv создан')
