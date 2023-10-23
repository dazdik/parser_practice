from selenium import webdriver
from selenium.webdriver.common.by import By

selector = By.CSS_SELECTOR


def read_clean(elem):
    (a := elem).clear()
    return a.text


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    for i in browser.find_elements(selector, '.parent'):
        gray, blue, button = i.find_elements(selector, 'textarea[color="gray"], textarea[color="blue"], button')
        blue.send_keys(read_clean(gray))
        button.click()
    browser.find_element(selector, 'button#checkAll').click()
    print(browser.find_element(selector, '#congrats').text)
