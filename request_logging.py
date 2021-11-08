import requests
from bs4 import BeautifulSoup

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

print("> === ",baslik[0]," ===")
for i in range(0,5):
    print("> ",sayi[i],". ",ipucu[i])
print("> === ",baslik[1]," ===")   
for i in range(5,10):
    print("> ",sayi[i],". ",ipucu[i])

