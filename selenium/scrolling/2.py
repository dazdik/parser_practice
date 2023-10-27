from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/scroll/2/index.html')

    actions = ActionChains(driver)
    total = []
    [actions.move_to_element(item).click().perform() for item in driver.find_elements(By.TAG_NAME, 'input')]
    total += [int(x.text) for x in driver.find_elements(By.TAG_NAME, 'span') if x.text.isdigit()]

    print(sum(total))
