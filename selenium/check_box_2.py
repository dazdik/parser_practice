from numbers import numbers

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

ua = UserAgent()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user_agent={ua.random}')


with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/5/5.html')
    checkbox = browser.find_elements(By.CLASS_NAME, 'check')
    for ch in checkbox:
        if int(ch.get_attribute('value')) in numbers:
            ch.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
