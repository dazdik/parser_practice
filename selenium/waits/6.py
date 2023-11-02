from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    banner = browser.find_element(By.CLASS_NAME, 'close')
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable(banner)).click()
    WebDriverWait(browser, 15).until(EC.invisibility_of_element_located(banner))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.find_element(By.ID, 'message').text)
