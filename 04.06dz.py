#2
import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/wiki/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find_all("table")
    for i in table:
        rows = i.find_all('tr')
        for row in rows:
            every_row = row.find_all(['td', 'th'])
            for text_in_row in every_row:
                print(text_in_row.get.text().strip)
else:
    print(f"немає підклчення {response.status_code}")