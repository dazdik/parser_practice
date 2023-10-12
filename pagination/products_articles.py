import lxml
import requests
from bs4 import BeautifulSoup


def get_all_pages() -> list:
    """
    Получение всех страниц из категории.
    """
    url = 'https://parsinger.ru/html/index3_page_1.html'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_pages = [tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a')]
    return all_pages


def get_items() -> list:
    """
    Получение карточек товара с каждой страницы пагинации.
    """
    all_pages = get_all_pages()
    all_item = []
    for i in all_pages:
        response = requests.get(url=f'https://parsinger.ru/html/{i}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        all_item += (tag['href'] for tag in soup.find_all('a', class_='name_item'))
    return all_item


def total_sum_articles() -> int:
    """
    Получение суммы всех артикулов с карточек товара.
    """
    all_items = get_items()
    total_sum = 0
    for i in all_items:
        response = requests.get(url=f'https://parsinger.ru/html/{i}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        total_sum += int(soup.find('p', class_='article').text.split(': ')[1])

    return total_sum


print(total_sum_articles())
