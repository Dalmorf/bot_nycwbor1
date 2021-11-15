import requests
from bs4 import BeautifulSoup
import json
import logging
import sys
import datetime
from collections import namedtuple

url = "https://www.nytimes.com/crosswords/game/mini"
response = requests.get(url)

try:
    html_content = response.content
except:
    sys.stdout.write("Content alınamadı.\n")
else:
    sys.stdout.write("Content alındı.\n")

soup = BeautifulSoup(html_content,"html.parser")
basliklar = soup.find_all("h3",{"class":"ClueList-title--1-3oW"})
sayilar = soup.find_all("span",{"class":"Clue-label--2IdMY"})
ipuclari = soup.find_all("span",{"Clue-text--3lZl7"})

basliklar = [baslik.text for baslik in basliklar]    
sayilar = [sayi.text for sayi in sayilar]
ipuclari = [ipucu.text for ipucu in ipuclari]

Clue = namedtuple('Clue', ['group', 'number', 'string'])
clues = [Clue(basliklar[0], sayilar[i], ipuclari[i]) for i in range(5)]
clues.extend([Clue(basliklar[1], sayilar[i], ipuclari[i]) for i in range(5,10)])
data = [clue._asdict() for clue in clues]

date = datetime.datetime.now()
fileName = "ipucu-{}.json"

try:
    with open(fileName.format(date.strftime("%d_%m_%y")), 'w') as json_dosya:
        json.dump(data, json_dosya, indent=4)
except:
    sys.stdout.write("Json dosyası oluşturulurken hata oldu.\n")
else:
    sys.stdout.write("Json dosyası oluşturuldu.\n")

result = zip(sayilar,ipuclari)
result = tuple(result)

for a in result:
    if a==result[0]:
        print("> === ",basliklar[0]," ===")
    elif a==result[5]:
        print("> === ",basliklar[1]," ===")
    print("> ",a[0],". ",a[1])



