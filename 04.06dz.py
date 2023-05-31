#3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/wiki/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    classs = soup.find_all("exampel_class")
    for i in classs:
        print(i)
else:
    print(f"Немає підклчення {response.status_code}")