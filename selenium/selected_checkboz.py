from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'parent')
    numbers = []
    for field in fields:
        if field.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            numbers.append(int(field.find_element(By.TAG_NAME, 'textarea').text))

    print(sum(numbers))
