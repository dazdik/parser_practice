from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/methods/5/index.html')
    dict_expire = defaultdict(int)
    urls = [url.get_attribute('href') for url in driver.find_elements(By.TAG_NAME, 'a')]
    for url in urls:
        driver.get(url)
        expiry = driver.get_cookies()[0]['expiry']
        dict_expire[url] = expiry
    max_exp_url = max(dict_expire, key=lambda k: dict_expire[k])
    driver.get(max_exp_url)
    print(driver.find_element(By.ID, 'result').text)
