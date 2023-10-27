import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(1)
    tag_p = browser.find_element(By.TAG_NAME, 'input')
    while True:
        tag_p.send_keys(Keys.DOWN)
        if browser.find_elements(By.CLASS_NAME, 'last-of-list'):
            break
    tag_p = browser.find_element(By.ID, 'scroll-container')
    print(sum(map(int, tag_p.text.split())))
