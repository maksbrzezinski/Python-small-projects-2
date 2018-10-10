#! /usr/bin/env/ python 3
#lucky.py - opens a few lucky shots in Google

import requests, sys, webbrowser, bs4

print('Wyszukwianie...')    #Komunikat wyświetlany podczas
                            #pobierania strony Google.
res = requests.get('http://www.google.pl/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Pobranie łączy z kilkoma pierwszywmi wynikami wyszukiwania.

soup = bs4.BeautifulSoup(res.text)

#TODO: Otworzenie karty przeglądarki WWW dla każdego wyniku wyszukiwania.

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.pl' + linkElems[i].get('href'))



