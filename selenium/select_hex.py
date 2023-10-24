import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

selector = By.CSS_SELECTOR


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    for i in browser.find_elements(selector, 'div[style*="background-color"]'):
        span = i.find_element(selector, 'span').text
        select_element = i.find_element(selector, 'select')
        select = Select(select_element).select_by_value(span)
        hex_el = i.find_element(selector, f'button[data-hex="{span}"]').click()
        i.find_element(selector, 'input[type="checkbox"]').click()
        i.find_element(selector, 'input[type="text"]').send_keys(span)
        i.find_element(By.XPATH, "//button[text()='Проверить']").click()
    browser.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()
    alert = Alert(browser)
    print(alert.text)
    alert.accept()
