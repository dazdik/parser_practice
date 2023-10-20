import os
import time

from dotenv import load_dotenv
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

options = {'proxy': {
    'http': os.getenv('HTTP_PROXY'),
    'https': os.getenv('HTTPS_PROXY'),
}}

ua = UserAgent()
opts = webdriver.ChromeOptions()
opts.add_argument(f"user-agent={ua.random}")

with webdriver.Chrome(seleniumwire_options=options, options=opts) as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'form_box')

    for field in fields:
        form_element = field.find_element(By.CLASS_NAME, 'form').send_keys('Text')

    send_element = browser.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(3)
