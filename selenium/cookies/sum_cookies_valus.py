from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    print(sum(int(cookie['value']) for cookie in webdriver.get_cookies() if 'secret' in cookie['name']))
