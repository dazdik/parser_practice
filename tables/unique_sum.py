import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')

rows = table.find_all('td')
total_sum = sum({float(row.text) for row in rows})

print(total_sum)
