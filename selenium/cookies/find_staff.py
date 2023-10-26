import time

from list_cookies import cookies

from selenium import webdriver
from selenium.webdriver.common.by import By

list_of_dicts = []
with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.6/1/index.html')

    for cookie in cookies:

        driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(0.5)
        user_dict = {
            'age': driver.find_element(By.ID, 'age').text.split(': ')[-1],
            'skills': len([skill.text for skill in driver.find_elements(By.TAG_NAME, 'li')]),
            'value': cookie['value']
        }
        list_of_dicts.append(user_dict)
        driver.delete_all_cookies()
    res = sorted(list_of_dicts, key=lambda x: (x['age'], -x['skills']))[0]
    print(res)
