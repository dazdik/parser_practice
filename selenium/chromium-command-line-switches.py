import csv

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

with open("commands_translate.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["команда", "перевод"])

r = requests.get("https://peter.sh/experiments/chromium-command-line-switches/")
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "lxml")
n, d = [], []
name = [n.append(i.text.replace(" ⊗", "") \
                 .replace(" ↪", "") \
                 .replace("", "").split("\n")[1]) for i in soup.find("table", class_="overview-table").find_all("tr")]

description = [d.append(i.text.replace(" ⊗", "") \
                        .replace(" ↪", "") \
                        .replace("", "").replace(
    "----------------------------------------------------------------------------- ", "") \
                        .replace("/prefetch:# ", "") \
                        .replace("#", "").split("\n")[2]) for i in
               soup.find("table", class_="overview-table").find_all("tr")]
n, d = n[2:], d[2:]
for nm, des in zip(n, d):
    st = nm, TextBlob(des).translate(from_lang="en", to="ru")
    file = open("commands_translate.csv", "a", newline="", encoding="utf-8-sig")
    writer = csv.writer(file, delimiter=',')
    writer.writerow(st)
file.close()
print("commands_translate.csv готов!")
