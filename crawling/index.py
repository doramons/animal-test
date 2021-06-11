#!/usr/bin/env python3
# Anchor extraction from HTML document

from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.naver.com/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    f = open("새파일.txt", 'w',encoding='utf-8')
    for anchor in soup.select('a.nav'):
        data = str(i) + anchor.get_text() +'\n'
        i += 1
        f.write(data)
    f.close()
        


