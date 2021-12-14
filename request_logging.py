import requests
from bs4 import BeautifulSoup
import json
import logging
import sys
import datetime
import itertools  
from collections import namedtuple

try:
    response = requests.get("https://www.nytimes.com/crosswords/game/mini")
except requests.ConnectionError:
    sys.stdout.write("Bağlantı kurulamadı.\n")
    exit()
else:
    sys.stdout.write("Bağlantı kuruldu.\n")

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
#clues = [Clue(basliklar[0], sayilar[i], ipuclari[i]) for i in range(5)]
#clues.extend([Clue(basliklar[1], sayilar[i], ipuclari[i]) for i in range(5,10)])


#clues = map(Clue, list(zip(itertools.repeat(basliklar[0]), sayilar, ipuclari)))

clues = list(map(Clue,basliklar[0], itertools.repeat(sayilar,1), itertools.repeat(ipuclari,1)))

#clues = list(map(Clue(basliklar[0], sayilar, ipuclari)))

data = [clue._asdict() for clue in clues]

date = datetime.datetime.now()

try:
    with open("ipucu-{}.json".format(date.strftime("%d_%m_%Y")), 'w', encoding='utf-8') as json_dosya:
        json.dump(data, json_dosya, indent=4)
except:
    sys.stdout.write("Json dosyası oluşturulurken hata oldu.\n")
else:
    sys.stdout.write("Json dosyası oluşturuldu.\n")

for a in tuple(zip(sayilar,ipuclari)):
    if a[1]==ipuclari[0]:
        print("> === ",basliklar[0]," ===")
    elif a[1]==ipuclari[5]:
        print("> === ",basliklar[1]," ===")
    print("> ",a[0],". ",a[1])



