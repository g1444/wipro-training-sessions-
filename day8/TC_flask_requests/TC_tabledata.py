import json
import requests
from bs4 import BeautifulSoup

url="https://www.w3schools.com/html/html_tables.asp"

responses=requests.get(url)
soup=BeautifulSoup(responses.text,"html.parser")
page_title=soup.title.string if soup.title else "no Title"
print(page_title)

table_data=[]
table=soup.find("table")
if table:
    rows=table.findAll("tr")
    for row in rows[1:]:
        coloumns=row.findAll("td")
        row_data=[col.text.strip() for col in coloumns]
        print(row_data)
        table_data.append(row_data)
extracted_data={
    "page_title": page_title,
    "table_data": table_data

}
with open("extracted_data.json","w",encoding="utf-8") as file:
    json.dump(extracted_data,file,indent=4)