import json

import requests
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/html/'


def get_soup(relative_path) -> BeautifulSoup:
    response = requests.get(url=relative_path)
    response.encoding = 'utf-8'

    return BeautifulSoup(response.text, 'lxml')


def get_pages() -> list:
    soup = get_soup('https://parsinger.ru/html/index2_page_1.html')
    return [f"{base_url}{page['href']}" for page in soup.find('div', class_='pagen').find_all('a')]


def get_cards() -> list:
    pages = get_pages()
    cards = []
    for page in pages:
        soup = get_soup(page)
        cards += [f"{base_url}{card['href']}" for card in soup.find(
            'div', class_='item_card').find_all('a', class_='name_item')]
    return cards


def get_json() -> list:
    mobile_json = []

    cards = get_cards()
    for card in cards:
        result = {}
        soup = get_soup(card)
        result.update({
            'categories': 'mobile',
            'name': soup.find('p', id='p_header').text.strip(),
            'article': soup.find('p', class_='article').text.split(': ')[1].strip(),
            'description': {i['id']: i.text.split(':')[1].strip() for i in soup.find_all('li')},
            'count': soup.find('span', id='in_stock').text.split(': ')[1].strip(),
            'price': soup.find('span', id='price').text,
            'old_price': soup.find('span', id='old_price').text,
            'link': card
        })

        mobile_json.append(result)
    return mobile_json


with open('mobile.json', 'w', encoding='utf-8') as file:
    res = get_json()
    json.dump(res, file, indent=4, ensure_ascii=False)
