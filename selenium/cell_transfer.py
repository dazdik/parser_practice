import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/5.5/4/1.html")
time.sleep(2)


# Находим все родительские элементы
parents = browser.find_elements(By.CLASS_NAME, 'parent')

# Проходимся по каждому родительскому элементу
for parent in parents:
    # Находим textarea и checkbox внутри родительского элемента
    color = parent.find_elements(By.TAG_NAME, 'textarea')
    number = color[0].text
    color[0].clear()
    color[1].send_keys(number)
    parent.find_element(By.TAG_NAME, 'button').click()
time.sleep(2)
browser.quit()
