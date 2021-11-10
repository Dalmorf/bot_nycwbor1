import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nytimes.com/crosswords/game/mini"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")
baslik = soup.find_all("h3",{"class":"ClueList-title--1-3oW"})
sayi = soup.find_all("span",{"class":"Clue-label--2IdMY"})
ipucu = soup.find_all("span",{"Clue-text--3lZl7"})

for i in range(len(baslik)):
    baslik[i] = (baslik[i].text).strip("\n").strip()

for i in range(len(sayi)):
    sayi[i] = (sayi[i].text).strip("\n").strip()
    ipucu[i] = (ipucu[i].text).strip("\n").strip()    

data = {
        baslik[0]:{
            "number":[sayi[0],sayi[1],sayi[2],sayi[3],sayi[4]],
            "string":[ipucu[0],ipucu[1],ipucu[2],ipucu[3],ipucu[4]]
        },
        baslik[1]:{
            "number":[sayi[5],sayi[6],sayi[7],sayi[8],sayi[9]],
            "string":[ipucu[5],ipucu[6],ipucu[7],ipucu[8],ipucu[9]]
        }
    }

with open('data.json', 'w') as json_dosya:
  json.dump(data, json_dosya)

print("> === ",baslik[0]," ===")
for i in range(0,5):
    print("> ",sayi[i],". ",ipucu[i])
print("> === ",baslik[1]," ===")   
for i in range(5,10):
    print("> ",sayi[i],". ",ipucu[i])

.