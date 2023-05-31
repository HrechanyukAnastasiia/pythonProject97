#1
import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/wiki/")
if response.status_code == 200:
    req = BeautifulSoup(response.content, "html.parser")
    for i in req.find_all('h2'):
        i.extract()
    text = ' '.join(req.stripped_strings)
    words = text.split()
    print(words)
else:
    print(f"Немає підключення {response.status_code}")