#By default this scrapes all articles by Mathew Ingram on GigaOM, but it can be remixed for other authors/sites
import urllib2
from bs4 import BeautifulSoup
import re

i = 1
#iterator for page numbers

while i < 4:
    start = ('http://gigaom.com/author/mathewingram/page/' + str(i))
    page = urllib2.urlopen(start).read()
    soup = BeautifulSoup(page)
    i = i + 1

    for item in soup.findAll("h1", {"entry-title"}):
        for link in item.find_all('a'):
            print link.get('href')


