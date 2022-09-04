import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = 'https://www.py4e.com/'
response = requests.get(url)
soup = BeautifulSoup(requests.get(url).content, "html.parser")
external_urls = set()
s = 0


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


for a_tag in soup.findAll("a"):
    href = a_tag.attrs.get("href")
    if not is_valid(href):
        continue
    if href == "" or href is None:
        continue
    if href in external_urls:
        continue
    if href[:5] == "https":
        s += 1
        external_urls.add(href)
for i in range(len(external_urls)):
    print(external_urls.pop())
print('Кол-во уникальных ссылок: ', s)
