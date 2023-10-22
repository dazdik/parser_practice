import ast
import time

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

ua = UserAgent()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user_agent={ua.random}')

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    res = browser.find_element(By.ID, 'text_box').text
    parsed_expression = ast.parse(res, mode='eval')
    result = eval(compile(parsed_expression, filename='<string>', mode='eval'))
    browser.find_element(By.ID, 'selectId').send_keys(result)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)
