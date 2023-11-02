from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    for id in ids_to_find[::-1]:
        WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, f"{id}"))).click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
