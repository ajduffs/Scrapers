import urllib2
from bs4 import BeautifulSoup
import re

start = 'http://www.miningaustralia.com.au/author/andrew%20duffy'
page = urllib2.urlopen(start).read()
soup = BeautifulSoup(page)


for item in soup.findAll("h1"):
    for link in item.find_all("a", href=re.compile("news")):
            print link.getText()
            print link.get('href')

for item in soup.findAll("h1"):
    for link in item.find_all("a", href=re.compile("features")):
            print link.getText()
            print link.get('href')

"""
A scraper using BeautifulSoup and regular expressions to collect my stories from the Australian Mining website. 
One loop is for news articles, and the other is for features. 
"""
