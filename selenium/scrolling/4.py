from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_2/')

    actions = ActionChains(driver)
    div = driver.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for i in range(10):
        actions.move_to_element(div).scroll_by_amount(1, 500).perform()

    total = sum(int(p.text) for p in driver.find_elements(By.TAG_NAME, 'p') if p.text)
    print(total)
