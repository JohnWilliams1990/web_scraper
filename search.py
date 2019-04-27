#!/usr/bin/python3
#  John Williams
#  105201054
#  Date: Thu. Apr. 4, 2019
#  Program: search.py
#
#  Credit should be given to https://www.rubydevices.com.au/blog/how-to-scrape-bing 
#  for the use of bueatiful soup at least for the getContent function. 

import sys
import requests
import bs4
import re
import urllib.request as urllib2

# bingSearch(arrayvars,numberOfPages)
# Function used to search bing for applicable urls for the serrch terms that are provided. 
# variables: 
#
# arrayvars     -> List of strings used for words in the search.
# numberOfPages -> How many bing pages should be searched. This will amplify the number of 
#                  URLs that are returned
# returns: List of URLs from the bing pages

def bingSearch(arrayvars,numberOfPages):
    urls = []
    for itemNumber in range(0,numberOfPages):
        searchString = "http://www.bing.com/search?q=" + "%2B".join(arrayvars) + "&count=100"  + "&First=" + str(itemNumber*30)
        #print(searchString)
        #getContent(searchString)
        getRequest = urllib2.Request(searchString, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
        urlfile = urllib2.urlopen(getRequest)
        htmlResult = urlfile.read(200000)
        soup = bs4.BeautifulSoup(htmlResult, 'html.parser')
        links = soup.findAll('a', href=True)
        cleanLinks = []
        for link in links:
            # microsoft styles pages must be removed
            y = re.match("(.*go.microsoft.*)" ,(link.get('href')))
            # get links that are in anchors with hrefences
            z = re.match("(http[s]*:\/\/[www]*).*",(link.get('href')))
            if z and not y :
                cleanLinks.append((link.get('href')))
        urls.extend(cleanLinks)
    urls = list(set(urls))
    return urls

# getContent(url):
# Function used to display some tags that are used in the bing webpage that come from the 
# bing search. 
# variables: 
#
# urls -> should be a http://www.bing.com URL because of the various tags that are in the page
# returns: nothing

def getContent(url):
# https://www.rubydevices.com.au/blog/how-to-scrape-bing
    getRequest = urllib2.Request(url, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    urlfile = urllib2.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()
    #print(htmlResult)
    soup =  bs4.BeautifulSoup(htmlResult, 'html.parser')
    [s.extract() for s in soup('span')]
    unwantedTags = ['a', 'strong', 'cite']
    for tag in unwantedTags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    results = soup.findAll('li', { "class" : "b_algo" })
    for result in results:
        print ("# TITLE: " + str(result.find('h2')).replace(" ", " ") + "\n#")
        print ("# DESCRIPTION: " + str(result.find('p')).replace(" ", " "))
        print ("# ___________________________________________________________\n#")

if __name__ == '__main__':

    # sys.argv[1:] search terms are all listed in the array except for the first term
    urls1 = [] # list of urls
    numberOfPages = 5 # pages in bing to traverse
    urls1 =  bingSearch(sys.argv[1:], numberOfPages)
    for link in urls1: 
        print(link)
