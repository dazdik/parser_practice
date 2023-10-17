import json

import requests
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/html/'


def get_soup(relative_path) -> BeautifulSoup:
    response = requests.get(url=relative_path)
    response.encoding = 'utf-8'

    return BeautifulSoup(response.text, 'lxml')


# сбор всех категорий
def get_categories() -> list:
    soup = get_soup('https://parsinger.ru/html/index1_page_1.html')
    return [f"{base_url}{category['href']}" for category in soup.find('div', class_='nav_menu').find_all('a')]


# сбор всех страниц пагинации из категории
def get_pages() -> list:
    pages = []
    for category in get_categories():
        soup = get_soup(category)
        pages += [f"{base_url}{page['href']}" for page in soup.find('div', class_='pagen').find_all('a')]
    return pages


def get_json() -> json:
    pages = get_pages()
    result = []
    for page in pages:
        soup = get_soup(page)
        name = [i.text.strip() for i in soup.find_all('a', 'name_item')]
        information = [i.text.split('\n') for i in soup.find_all('div', 'description')]
        price = [x.text for x in soup.find_all('p', 'price')]
        for item, info_card, price_item in zip(name, information, price):
            result.append({
                'Наименование': item,
                info_card[1].split(': ')[0].strip(): info_card[1].split(': ')[1].strip(),
                info_card[2].split(': ')[0].strip(): info_card[2].split(': ')[1].strip(),
                info_card[3].split(': ')[0].strip(): info_card[3].split(': ')[1].strip(),
                info_card[4].split(': ')[0].strip(): info_card[4].split(': ')[1].strip(),
                'Цена': price_item
            })
    return result


with open('result.json', 'w', encoding='utf-8') as file:
    res = get_json()
    json.dump(res, file, indent=4, ensure_ascii=False)
