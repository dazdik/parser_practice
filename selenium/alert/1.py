import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/1/index.html')
    for button in driver.find_elements(By.CSS_SELECTOR, 'input[type="button"]'):
        button.click()
        time.sleep(2)
        prompt = driver.switch_to.alert
        prompt.accept()
        text = driver.find_element(By.CSS_SELECTOR, 'p[id="result"]').text
        if text:
            print(text)
            break
