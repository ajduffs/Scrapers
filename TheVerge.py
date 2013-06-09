from bs4 import BeautifulSoup
import urllib2

start = 'http://www.theverge.com/users/tomwarren/blog'
page = urllib2.urlopen(start).read()
soup = BeautifulSoup(page)

for item in soup.findAll("li", {"item"}):
    for link in item.find_all('a'):
        print link.get('href')

"""
Another simple scraper for authors at The Verge
"""

