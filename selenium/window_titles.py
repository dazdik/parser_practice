import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

with Chrome() as browser:
    browser.get("https://parsinger.ru/blank/3/index.html")
    sum_numbers = 0
    for button in browser.find_elements(By.TAG_NAME, 'input'):

        browser.execute_script(f"{button.get_attribute('onclick')}")
    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        title = browser.title
        if title.isdigit():
            sum_numbers += int(title)

    print(sum_numbers)
