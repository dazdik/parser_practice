from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get('https://parsinger.ru/draganddrop/1/index.html')

    red = driver.find_element(By.ID, 'draggable')
    container = driver.find_element(By.ID, 'field2')

    actions = ActionChains(driver)
    actions.drag_and_drop(red, container).perform()

    print(driver.find_element(By.ID, 'result').text)
