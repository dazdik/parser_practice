from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/3/index.html')
    check_button = driver.find_element(By.CSS_SELECTOR, 'input[type="button"]')
    for button in driver.find_elements(By.CSS_SELECTOR, 'span[class="pin"]'):
        number = button.text
        check_button.click()
        alert = driver.switch_to.alert
        alert.send_keys(number)
        alert.accept()
        result = driver.find_element(By.CSS_SELECTOR, 'p[id="result"]').text
        if result != 'Неверный пин-код':
            print(result)
            break
