from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

ua = UserAgent()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user_agen={ua.random}")

list_numbers = []

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    all_numbers = browser.find_elements(By.TAG_NAME, 'p')
    list_numbers += [int(number.text) for number in all_numbers]

print(sum(list_numbers))
