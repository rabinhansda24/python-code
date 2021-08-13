import requests
from bs4 import BeautifulSoup

url = "https://github.com/vinta/awesome-python"

q = input("Query? ")

r = requests.get(url)

html = BeautifulSoup(r.content, 'html5lib')


link_html = html.find("article", {'class': 'markdown-body entry-content container-lg'}).find_all('a')
links = {}
for a in link_html:
    if a.text and not a["href"].startswith('#'):
        links[a.text] = a["href"]


if q in links:
    print(f'Output: {links[q]}')
else:
    print("Query not found")