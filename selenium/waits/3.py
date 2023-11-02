from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    print(WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))).text)
