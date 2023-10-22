import time

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

ua = UserAgent()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user_agent={ua.random}')

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    all_options = browser.find_elements(By.TAG_NAME, 'option')
    value_form = sum(int(opt.text) for opt in all_options)
    browser.find_element(By.ID, 'input_result').send_keys(value_form)

    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)
