##!/usr/bin/python3.6
##  John Williams
##  105201054
##  Date: Thu. Oct. 4, 2018
##  Program: scrape.py

import sys
import webbrowser
import requests
import bs4
import mmap
import re

def mapIt():

    if len(sys.argv) > 1:
        #get address from command line
        address = ' '.join(sys.argv[1])
    else:
        address = 'Lawrence Street Center, Denver, CO'

    webbrowser.open('https://www.google.com/maps/place/' + address)

##############################
def webGet(url):

    webpage = requests.get(url) # get webpage via http request 
    try:
        webpage.raise_for_status() # use exeptions for the error handeling
    except Exception as e:
        print('There was a problem with the url {}'.format(e))
    return webpage

##############################
def printToFile(url, filename):
    webpage = webGet(url) # instanciate webpage object
    webFile = open(filename, 'wb')

    for chunk in webpage.iter_content(10000):
        webFile.write(chunk)# write webpage to file via chunks --> this is independent of formatting like html

##############################
def formattedHTML(filename, formattedFilename):
    file = open(filename, 'r+') # open input file 
    data = mmap.mmap(file.fileno(), 0) # parse data to memory map 
    html = bs4.BeautifulSoup(data, 'html.parser') # parse down to html 
    formatted = html.prettify('utf-8') # set encoding of file to UTF8
    formattedFile=open(formattedFilename, "wb") # open formatted file
    formattedFile.write(formatted) # write to file 
    formattedFile.close() # close file



##############################
def parseHTML(filename, searchWord, numWordsBefore, numWordsAfter):
    # 
    print ('***Searching in {} for the keyword {}***'.format(filename, searchWord))
    file = open(filename, 'r+') # open file
    data = mmap.mmap(file.fileno(), 0) # make datamap that can be used for regex

    regexString = "(\\S+\\s+)"
    regexString = regexString + "{" + str(numWordsBefore) + "}"
    regexString = regexString + "\\b" + searchWord + "\\b" + "(\\S+\\s+)" # set parameters for regex search {#words before \\ regex \\ #words after}
    regexString = regexString + "{" + str(numWordsAfter) + "}"

    for match in re.finditer(regexString, data.read().decode('utf-8')): # for each item that matches the regex print it
        print('Start:{}, End:{}\n\n{}'.format(match.start(), match.end(), match.group()) )
    file.close() # close the file

##############################
def justText(filename):
    file = open(filename, 'r+')
    data = mmap.mmap(file.fileno(), 0)   #Memory map handles the memory for large files, acts like a string
    html = bs4.BeautifulSoup(data, 'html.parser') # move datamap to html
    text = html.get_text() # print output of html without tags as simple text
    print(text)


##############################
def justLinks(filename):
    file = open(filename, 'r+') # open file 
    data = mmap.mmap(file.fileno(), 0) # make memory map 
    html = bs4.BeautifulSoup(data, 'html.parser') # push to html 
    links = html.findAll("a", href=True) # strip document for all possible links
    for link in links: # print all links in document starting with http 
        if link['href'].startswith('http'):
            print (link)

def postToForm():
    # set header
    header = {'User-Agent': 'FireFox... of coarse'} 
    # make post for http request
    r = requests.post('http://localhost/csci5742.php', data={'name':'John Williams (Not the composer)','movie':'Dr. Who with David Tennant'}, headers=header ) 
    print (r.text) # print contents of responce from request
    print (r.headers)




if __name__ == '__main__':
    # move both files from the server to individual files 
    printToFile('https://automatetheboringstuff.com/files/rj.txt', 'RomeoAndJuliet.txt')
    printToFile('https://en.wikipedia.org/wiki/Computer_security', 'wiki.html')

   # search for specific strings in files
    parseHTML('RomeoAndJuliet.txt', 'Juliet', 4,4) 
   # parseHTML('wiki.html', 'security', 4,4)

   # justText('wiki.html')
   # justLinks('wiki.html')
   # formattedHTML('wiki.html', 'wikipretty.html')
   # 
    postToForm()
else:
    print("imported rather than run directly")

