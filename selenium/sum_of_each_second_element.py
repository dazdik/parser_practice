from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # запуск браузера в фоновом режиме


with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    numbers = browser.find_elements(By.CSS_SELECTOR, '.text p:nth-child(2)')
    print(sum(int(number.text) for number in numbers))
