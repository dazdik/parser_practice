import re

from selenium import webdriver


def filter_cookies(name):

    return 'secret' in name and int(name[-1]) % 2 == 0


with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    print(sum(int(cookie['value']) for cookie in webdriver.get_cookies() if filter_cookies(cookie['name'])))
