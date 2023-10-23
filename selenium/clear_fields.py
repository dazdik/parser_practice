from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'text-field')
    for field in fields:
        field.clear()

    browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert.text
    print(alert)
