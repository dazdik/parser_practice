from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/2/index.html')
    element = driver.find_element(By.ID, 'draggable')
    actions = ActionChains(driver)

    for box in driver.find_elements(By.CLASS_NAME, 'box'):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'draggable')))
        actions.drag_and_drop(element, box).perform()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'message')))
    print(driver.find_element(By.ID, 'message').text)
