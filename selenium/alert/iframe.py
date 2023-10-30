import time

from selenium import webdriver
from selenium.common import (NoAlertPresentException,
                             UnexpectedAlertPresentException)
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')

    for iframe in driver.find_elements(By.TAG_NAME, 'iframe'):
        driver.switch_to.frame(iframe)
        iframe_content = driver.page_source
        driver.find_element(By.TAG_NAME, 'button').click()
        number = driver.find_element(By.TAG_NAME, 'p').text
        driver.switch_to.default_content()
        input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        input_field.clear()
        input_field.send_keys(number)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'button[id="checkBtn"]').click()

        try:
            alert = Alert(driver)
            alert_text = alert.text
            print("Текст из алерт-окна:", alert_text)
            alert.accept()
        except (NoAlertPresentException, UnexpectedAlertPresentException):
            print("Алерт не найден")
