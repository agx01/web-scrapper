# -*- coding: utf-8 -*-

#import the library used to query a website
import urllib3
http = urllib3.PoolManager()
urllib3.disable_warnings()

search = "List of state and union territory capitals in India"
search = search.replace(" ", "_")
#specify the url
wiki = "http://en.wikipedia.org/wiki/" + search

#Query the website and return the html to the variable page
page = http.request('GET',wiki)
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the age variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page.data,"lxml")

paras = soup.find_all("p")

str(paras[0].get_text())
