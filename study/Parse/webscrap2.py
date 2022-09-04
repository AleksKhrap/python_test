import requests
from bs4 import BeautifulSoup

url = 'https://py4e-data.dr-chuck.net/comments_42.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

d = {"class": "comments"}
n = soup.find_all('span', d)
s = 0
for i in n:
    s += int(i.text)
print(s)
