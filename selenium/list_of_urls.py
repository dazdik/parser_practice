from math import sqrt

from selenium import webdriver
from selenium.webdriver.common.by import By

secret_code = 0
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html']


with webdriver.Chrome() as browser:
    [browser.execute_script(f'window.open("{site}", "_blank{i}");') for site, i in zip(sites, range(1, len(sites) + 1))]
    for handle in browser.window_handles[1:]:
        browser.switch_to.window(handle)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        secret_code += sqrt(int(browser.find_element(By.ID, 'result').text))
    print(round(secret_code, 9))
