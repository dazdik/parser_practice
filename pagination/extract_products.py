import lxml
import requests
from bs4 import BeautifulSoup


def extract_products() -> list:
    """
    Извлечение списка товаров с каждой целевой страницы.
    """
    list_of_products = []

    for i in range(1, 5):
        url = f'https://parsinger.ru/html/index3_page_{i}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        products_from_page = [product.text for product in soup.find_all('a', class_='name_item')]
        list_of_products.append(products_from_page)

    return list_of_products


print(extract_products())
