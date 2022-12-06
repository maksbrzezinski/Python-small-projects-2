#! /usr/bin/env python 3
#downloadXkcd.py - Downloads all the comics published
#on xkcd.com.

import requests, os, bs4
from html.parser import HTMLParser

url = 'http://xkcd.com'             #Initial URL address
os.makedirs('xkcd', exist_ok=True)  #Comic arts are kept in the catalog ./xkcd.
while not url.endswith('#'):
    
    #Gets page
    
    print('Page download %s...' % url)
    parser = HTMLParser
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    #Gets URL of a comic file

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Fail to find comic image address.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

    #Pobranie obrazu.

    print('Image download %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    #Save an image in the ./xkcd catalog.

    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Get the 'Prev' button URL.

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    
                           

print('Ready!')
