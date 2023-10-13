import lxml
import requests
from bs4 import BeautifulSoup


def get_soup(relative_path) -> BeautifulSoup:
    response = requests.get(url=f'https://parsinger.ru/html/{relative_path}')
    response.encoding = 'utf-8'

    return BeautifulSoup(response.text, 'lxml')


def get_all_categories() -> list:
    """
    Получение категорий.
    """
    url = 'https://parsinger.ru/html/index1_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    all_categories = [tag['href'] for tag in soup.find('div', {'class': 'nav_menu'}).find_all('a')]
    return all_categories


def get_pages() -> list:
    """
    Получение страниц пагинации для категорий.
    """
    all_categories = get_all_categories()
    all_pages = []

    for i in all_categories:
        soup = get_soup(i)
        all_pages += (tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a'))
    return all_pages


def get_all_items() -> list:
    """
    Получение всех карточек товара для категорий.
    """
    all_pages = get_pages()
    all_items = []

    for i in all_pages:
        soup = get_soup(i)
        all_items += [tag['href'] for tag in soup.find('div', {'class': 'item_card'}).find_all(
            'a', {'class': 'name_item'})]

    return all_items


def count_price_for_all() -> int:
    """
    Подсчет общей стоимости для всех товаров в наличии.
    """
    all_items = get_all_items()
    total_price = 0

    for i in all_items:
        soup = get_soup(i)
        total_price += int(soup.find('span', id='in_stock').text.split(': ')[1]) * \
            int(soup.find('span', id='price').text.split()[0])

    return total_price


print(count_price_for_all())
