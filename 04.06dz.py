#4
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    res = soup.find_all('h1')
    for i in res:
        print(res)
else:
    print(f"Немає підклчення {response.status_code}")