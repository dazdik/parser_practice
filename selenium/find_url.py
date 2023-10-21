import time

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

ua = UserAgent()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={ua.random}")


with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    driver = browser.find_element(By.LINK_TEXT, "16243162441624").click()
    result = browser.find_element(By.ID, 'result').text
    print(result)
