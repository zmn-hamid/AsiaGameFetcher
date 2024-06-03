import os

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


URL = "https://status.asia-game.org/CS16_AsiaGame/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table")

data = []
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all("td")[1:-1]
    data.append([col.text.strip() for col in cols])


os.system("cls" if os.name == "nt" else "clear")
print(tabulate(data, headers=["IP", "Server Name", "Map", "Status"]))
