from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    browser.set_window_size(1980, 1020)
    res = 0
    for number in range(1, 6):
        scroll_container = browser.find_element(By.ID, f'scroll-container_{number}')
        flag_break = ''
        span_list = []
        while 'last-of-list' not in flag_break:
            ActionChains(browser).scroll_from_origin(ScrollOrigin.from_element(scroll_container), 0, 2000).perform()
            spans = scroll_container.find_elements(By.TAG_NAME, 'span')
            for span in spans:
                if span not in span_list:
                    span_list.append(span)
                    res += int(span.text)
                    flag_break += span.get_attribute('class')
    print(res)
