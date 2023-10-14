import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.8/7/index.html'
response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

data = soup.select('td')
print(sum(int(d.text) for d in data if int(d.text) % 3 == 0))
