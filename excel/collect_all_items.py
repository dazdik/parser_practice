import csv

import requests
from bs4 import BeautifulSoup

start_page = 'https://parsinger.ru/html/index1_page_1.html'
base_url = 'https://parsinger.ru/html/'


def get_soup(url) -> BeautifulSoup:
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


def get_categories() -> list:
    soup = get_soup(start_page)
    return [f"{base_url}{category['href']}" for category in soup.find('div', class_='nav_menu').find_all('a')]


def get_pages() -> list:
    pages = []
    for category in get_categories():
        soup = get_soup(category)
        pages += [f"{base_url}{page['href']}" for page in soup.find('div', 'pagen').find_all('a')]
    return pages


def info() -> csv:
    names = []
    descriptions = []
    prices = []
    for item in get_pages():
        soup = get_soup(item)
        names += [name.text.strip() for name in soup.find_all('a', class_='name_item')]
        descriptions += [i.text.split('\n') for i in soup.find_all('div', 'description')]
        prices += [price.text for price in soup.find_all('p', class_='price')]

    for name, descr, price in zip(names, descriptions, prices):
        flatten = name, *[x.split(': ')[1].strip() for x in descr if x], price
        file = open('all_items.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)
        file.close()


info()
