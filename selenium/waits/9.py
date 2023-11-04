from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    for container in browser.find_elements(By.CLASS_NAME, 'container'):
        locator = (By.CSS_SELECTOR, 'input[type="checkbox"')
        WebDriverWait(container, 20).until(EC.element_located_selection_state_to_be(locator, True))
        container.find_element(By.TAG_NAME, 'button').click()

    print(browser.find_element(By.CSS_SELECTOR, 'p[id="result"]').text)
