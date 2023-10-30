from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')


def unique_pairs():
    for x in window_size_x:
        for y in window_size_y:
            yield x, y


dct = defaultdict(int)

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    for x, y in unique_pairs():
        browser.set_window_size(x, y)
        try:
            print(int(browser.find_element(By.ID, 'result').text))
            dct['width'] = x
            dct['height'] = y
            print(dct)
            break
        except ValueError:
            continue
