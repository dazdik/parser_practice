import os
import time

from dotenv import load_dotenv
from fake_useragent import UserAgent
from faker import Faker
from seleniumwire import webdriver

from selenium.webdriver.common.by import By

load_dotenv()

seleniumwire_options = {'proxy': {
    'http': os.getenv('HTTP_PROXY'),
    'https': os.getenv('HTTPS_PROXY'),
}}

ua = UserAgent()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={ua.random}")

fake = Faker('ru_RU')
fake.random
info = [fake.first_name_male(), fake.last_name_male(),
        fake.middle_name_male(), fake.random_int(10, 99),
        fake.city_name(), fake.email()
        ]

with webdriver.Chrome(options=chrome_options, seleniumwire_options=seleniumwire_options) as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'form')

    for form_text, field in zip(info, fields):
        field.send_keys(form_text)

    send_element = browser.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(3)
