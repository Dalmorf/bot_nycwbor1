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
    print("Bağlantı kurulamadı.")
    exit()
else:
    print("Bağlantı kuruldu.")

try:
    html_content = response.content
except:
    print("Content alınamadı.")
else:
    print("Content alındı.")

soup = BeautifulSoup(html_content,"html.parser")

#across = soup.find("div","ClueList-wrapper--3m-kd")
#across = across.find_next_siblings("span")
#print(len(across))



sayilar = soup.select('span:is(.Clue-label--2IdMY)')
print(len(sayilar))

ipuclari = soup.find_all("span",{"Clue-text--3lZl7"})


#basliklar = [baslik.text for baslik in basliklar]
sayilar = [sayi.text for sayi in sayilar]
ipuclari = [ipucu.text for ipucu in ipuclari]

Clue = namedtuple('Clue', ['group', 'number', 'string'])
clues = [Clue("Across", sayilar[i], ipuclari[i]) for i in range(5)]
clues.extend([Clue("Down", sayilar[i], ipuclari[i]) for i in range(5,10)])


#clues = map(Clue, list(zip(itertools.repeat(basliklar[0]), sayilar, ipuclari)))

#clues = list(map(Clue,basliklar[0], itertools.repeat(sayilar,1), itertools.repeat(ipuclari,1)))

#clues = list(map(Clue(basliklar[0], sayilar, ipuclari)))

data = [clue._asdict() for clue in clues]

date = datetime.datetime.now()

try:
    with open("db/ipucu-{}.json".format(date.strftime("%d_%m_%Y")), 'w', encoding='utf-8') as json_dosya:
        json.dump(data, json_dosya, indent=4)
except:
    print("Json dosyası oluşturulurken hata oldu.")
else:
    print("Json dosyası oluşturuldu.")

for a in tuple(zip(sayilar,ipuclari)):
    if a[1]==ipuclari[0]:
        print("> === Across ===")
    elif a[1]==ipuclari[5]:
        print("> === Down ===")
    print("> ",a[0],". ",a[1])



