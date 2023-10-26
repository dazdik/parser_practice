import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/1/index.html')
    buttons = driver.find_elements(By.CLASS_NAME, 'button-container')
    for button in buttons:

        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
