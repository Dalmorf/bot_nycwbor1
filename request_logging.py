import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.nytimes.com/crosswords/game/mini"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")
baslik = soup.find_all("h3",{"class":"ClueList-title--1-3oW"})
sayi = soup.find_all("span",{"class":"Clue-label--2IdMY"})
ipucu = soup.find_all("span",{"Clue-text--3lZl7"})

liste = list()

for i in range(len(baslik)):
    baslik[i] = (baslik[i].text).strip("\n").strip()

for i in range(len(sayi)):
    sayi[i] = (sayi[i].text).strip("\n").strip()
    ipucu[i] = (ipucu[i].text).strip("\n").strip()
    liste.append([sayi[i],ipucu[i]])


df = pd.DataFrame(liste,columns=[baslik[0],baslik[1]])
print(df)

