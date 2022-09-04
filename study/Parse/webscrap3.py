import requests
from bs4 import BeautifulSoup

url = input("Ссылка на страницу: ")  # https://www.imdb.com/name/nm0362766/?ref_=nv_sr_srsg_0
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
d = {"id": 'details-height', "class": 'see-more inline canwrap'}
n = soup.find('div', d).text

for i in range(n.find('(') + 1, n.find('\xa0m)')):
    print(n[i], end="")
