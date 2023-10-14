import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.8/8/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

merged_elements = soup.find_all(lambda tag: tag.has_attr('colspan') and not tag.find(True))
print(sum(int(el.text) for el in merged_elements))
