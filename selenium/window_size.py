import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    browser.set_window_size(555, 555)

    width_el = browser.find_element(By.ID, 'width')
    height_el = browser.find_element(By.ID, 'height')

    X = 555 - int(width_el.text.split(':')[1])

    Y = 555 - int(height_el.text.split(':')[1])

    browser.set_window_size(555 + X, 555 + Y)

    time.sleep(1)

    result = browser.find_element(By.ID, 'result')
    print(result.text)
