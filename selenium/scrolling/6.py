import time

from selenium import webdriver
from selenium.common import (NoAlertPresentException,
                             UnexpectedAlertPresentException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')

    actions = ActionChains(driver)
    [actions.move_to_element(item).scroll_to_element(item).perform() for item in driver.find_elements(
        By.CLASS_NAME, 'child_container')]
    checkbox = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    for ch in checkbox:
        value = int(ch.get_attribute('value'))
        if value % 2 == 0:
            actions.move_to_element(ch).click().perform()

    alert_button = driver.find_element(By.CLASS_NAME, "alert_button")
    alert_button.click()
    time.sleep(1)
    try:
        alert = Alert(driver)
        alert_text = alert.text
        print("Текст из алерт-окна:", alert_text)
        alert.accept()
    except (NoAlertPresentException, UnexpectedAlertPresentException):
        print("Алерт не найден")
