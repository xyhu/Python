# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 13:55:34 2014

@author: huxiangyu
"""
import urllib
import string
from bs4 import BeautifulSoup

"""
The following process inserts the data from the website and cleans it
"""
url = urllib.urlopen("http://www.landofbasketball.com/championships/year_by_year.htm")
html = url.read()

# using beatuiful soup
soup = BeautifulSoup(html)
text = soup.get_text()
# The string constains multiple text(e.g. headers) that is not what we need for
# the purpose of the program. Thus, need to find the index for the most recent
# year 
startIndex = text.index('2013-14')
# the index of the one after s. It is good since when slicing, it is up-to this
# element but not including it, which is what we want
endIndex = text.index('Chicago Stags') + len('Chicago Stags')
# slicing the string to contain only info we need
text_clean = text[startIndex:endIndex]

# split the text into list
textSplit = string.split(text_clean,'\n')
# remove empty strings
textSplit2 = filter(None,textSplit)
# remove empty strings that have a space in it
textSplit3 = filter(lambda x:x != ' ', textSplit2)
# finals MVP started from year 1968-69
data1 = textSplit3[:46*8]
# season MVP started from 1955-56
data2 = textSplit3[46*8:(46*8+13*6)]
# the first few years have no final MVP or season MVP
data3 = textSplit3[(46*8+13*6):]

"""
Create a dictionary for data1 with years to be keys, and all other info as values
input: data1
output: a dictionary
"""
def championDic1(x):
    """
    >>> sample = ['year', 'Champion', 'Score', 'Runner-Up', 'Finals-MVP','
    Finals_MVP_team','Season-MVP', 'Season_MVP_team']
    >>> championDic1(sample)
    {'year': 'Champion\nScore\nRunner-Up\nFinals-MVP\nFinals_MVP_team\nSeason-MVP\nSeason_MVP_team'}
    """
    dic = {}
    indice = [y for y in range(len(x)) if y % 8 == 0]
    for i in indice:
        dic[x[i]] = string.join(x[i+1:i+8], '\n')
    return dic
    
"""
Create a dictionary for data2 with years to be keys, and all other info as values
input: data2
output: a dictionary
"""
def championDic2(x):
    """
    >>> sample = ['year', 'Champion', 'Score', 'Runner-Up','Season-MVP', 'Season_MVP_team']
    >>> championDic2(sample)
    {'year': 'Champion\nScore\nRunner-Up\nSeason-MVP\nSeason_MVP_team'}
    """
    dic = {}
    indice = [y for y in range(len(x)) if y % 6 == 0]
    for i in indice:
        dic[x[i]] = string.join(x[i+1:i+6], '\n')
    return dic

"""
Create a dictionary for data3 with years to be keys, and all other info as values
input: data3
output: a dictionary
"""
def championDic3(x):
    """
    >>> sample = ['year', 'Champion', 'Score', 'Runner-Up']
    >>> championDic3(sample)
    {'year': 'Champion\nScore\nRunner-Up'}
    """
    dic = {}
    indice = [y for y in range(len(x)) if y % 4 == 0]
    for i in indice:
        dic[x[i]] = string.join(x[i+1:i+4], '\n')
    return dic

"""
If year are given, then champions, and all the available information will show up
input: year from user input
output: all the info
"""
def NBA(userInput):
    """
    >>> NBA('2013-14')
    San Antonio Spurs 
    4-1
    Miami Heat
    Kawhi Leonard
    (San Antonio Spurs)
    Kevin Durant
    (Oklahoma City Thunder)
    """
    if userInput in championDic1(data1).keys():
        print championDic1(data1)[userInput]
    elif userInput in championDic2(data2).keys():
        print championDic2(data2)[userInput]
    elif userInput in championDic3(data3).keys():
        print championDic3(data3)[userInput]
    else:
        print "The format of your unit for SOURCE_UNIT is wrong."

"""
Keep asking user input until user choose to quit
input: no argument needed
output: if user doesn't choose to quit, keep asking for new year/quit 
from user
"""
def keepAsking(): 
    userRequest = raw_input("Find the NBA champion of year XXXX-XX, or (q)uit]: ")
    if userRequest == 'q' or userRequest == 'quit':
        print "Thanks for checking NBA champions with me."
    else:
        NBA(userRequest)       
        keepAsking()



"""
Welcoming message to the users
"""
print "Want to find out the NBA champions for a particular year? Simply tell me the year (e.g. 2013-14), and I will tell you everything as follows:"
print
print "\tChampion\n\tScore\n\tRunner-up\n\tFinal-MVP\n\tFinal-MVP's team\n\tSeason-MVP\n\tSeason-MVP's team"
print "Please note that Finals MVP started from year 1968-69, Season MVP started from 1955-56"

keepAsking()

if __name__ == "__main__":
    import doctest
    doctest.testmod() 