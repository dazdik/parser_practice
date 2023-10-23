from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while browser.find_element(By.ID, 'result').text == 'refresh page':
        browser.refresh()
    print(browser.find_element(By.ID, 'result').text)
