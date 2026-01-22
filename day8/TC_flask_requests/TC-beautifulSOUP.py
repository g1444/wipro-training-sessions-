from bs4 import BeautifulSoup
import json,requests

url="https://anikai.to/home"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
page_title=soup.title.string if soup.title else "no title"
print(page_title)

for link in soup.findAll("a"):
    href=link.get("href")
    print(href)
