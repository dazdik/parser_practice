import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/2/index.html')
    input_text = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    input_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Проверить"]')
    for button in driver.find_elements(By.CSS_SELECTOR, 'input[type="button"]'):
        button.click()
        alert = driver.switch_to.alert
        code = alert.text
        alert.accept()
        input_text.send_keys(code)
        input_button.click()
        result = driver.find_element(By.CSS_SELECTOR, 'p[id="result"]').text
        if result != 'Неверный пин-код':
            print(result)
            break
