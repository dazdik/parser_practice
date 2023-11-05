import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get('https://parsinger.ru/selenium/5.10/3/index.html')
    actions = ActionChains(driver)
    colors = driver.find_elements(By.CSS_SELECTOR, '.draganddrop.ui-draggable')
    draganddrop_ends = driver.find_elements(By.CSS_SELECTOR, '.draganddrop_end')

    for color in colors:
        color_el = color.value_of_css_property('background-color')
        target = None

        for end in draganddrop_ends:
            border_color = end.value_of_css_property('border-top-color')

            if color_el == border_color:
                target = end
                break

        if target:
            ActionChains(driver).drag_and_drop(color, target).perform()
            time.sleep(0.5)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'message')))
    message = driver.find_element(By.ID, 'message').text
    print('Сообщение:', message)
