from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'text-field')
    for field in fields:
        if field.get_attribute('data-enabled'):
            field.clear()

    browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert.text
    print(alert)
