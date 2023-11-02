import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

    codes = []
    for box in browser.find_elements(By.CLASS_NAME, 'box_button'):
        index = box.get_attribute('data-index')
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@data-index="{index}"]'))).click()

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'ad_window')))
        browser.find_element(By.ID, 'close_ad').click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, 'ad_window')))

        while not browser.find_element(By.XPATH, f'//div[@data-index="{index}"]').text:
            time.sleep(1)
        codes.append(box.text)

    print('-'.join(codes))
