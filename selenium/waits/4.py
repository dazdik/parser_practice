from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
