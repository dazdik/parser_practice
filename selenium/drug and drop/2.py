import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with Chrome() as driver:
    driver.implicitly_wait(5)
    driver.get('https://parsinger.ru/selenium/5.10/2/index.html')

    target_area = driver.find_element(By.CLASS_NAME, 'draganddrop_end')
    drop = driver.find_element(By.ID, 'main_container').size['width'] - \
        target_area.size['width'] + \
        driver.find_element(By.ID, 'draganddrop1').size['width']

    actions = ActionChains(driver)

    for i in range(1, 11):
        square = driver.find_element(By.ID, f'draganddrop{i}')
        time.sleep(2)
        actions.click_and_hold(square).move_by_offset(drop, 0).release().perform()
    print(driver.find_element(By.ID, 'message').text)
