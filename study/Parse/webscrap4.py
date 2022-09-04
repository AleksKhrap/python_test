import requests
from bs4 import BeautifulSoup

num1 = 230
num2 = 300
t = h = 0
for i in range(num1, num2 + 1):
    s = ' '
    response = requests.get("https://www.imdb.com/name/nm0000" + str(i) + "/")
    soup = BeautifulSoup(response.text, "html.parser")
    d = {"id": 'details-height', "class": 'see-more inline canwrap'}
    if soup.find('div', d) is None:
        t += 1
        continue
    n = soup.find('div', d).text
    for j in range(n.find('(') + 1, n.find('\xa0m)')):
        s = s + n[j]
    h = h + float(s)
    l = 70 - t + 1
print(h / l)
