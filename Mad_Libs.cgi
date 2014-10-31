#!/usr/local/bin/python

"""
Created on Wed Oct 29 10:13:23 2014

@author: huxiangyu
"""
import cgitb
cgitb.enable() 

import cgi
import random
import pickle

sentences = ['To %s sentences for this %s is so %s',
            '%s cannot %s your %s',
            'It is so %s that Naruto is going to %s in %s',
            "I don't %s if I should %s phd or go to %s",
            'I %s to %s in %s']


sen_lexalCat = {'To %s sentences for this %s is so %s': ('VERB','NOUN', 'ADJECTIVE'),
            '%s cannot %s your %s':('NOUN','VERB','NOUN'),
            'It is so %s that Naruto is going to %s in %s': ('ADJECTIVE', 'VERB','NOUN'),
            "I don't %s if I should %s phd or go to %s":('VERB','VERB', 'VERB'),
            'I %s to %s in %s':('VERB','VERB','NOUN')}

sen_lexalCat2 = {'To %s sentences for this %s is so %s': ('VERB','NOUN', 'ADJECTIVE'),
            '%s cannot %s your %s':('NOUN','VERB','NOUN2'),
            'It is so %s that Naruto is going to %s in %s': ('ADJECTIVE', 'VERB','NOUN'),
            "I don't %s if I should %s phd or go to %s":('VERB','VERB2', 'VERB3'),
            'I %s to %s in %s':('VERB','VERB2','NOUN')}

"""
A function that randomly pick a sentence
input: no argument
output: sentences selested
"""
def generateSentence():
    """
    >>> generateSentence()
    'To %s sentences for this %s is so %s'
    """
    ind = int(random.random()*5)
    sen = sentences[ind]
    return sen



"""
A function that randomly pick a sentence and outputs the lexal categories for
users
input: sentense selected
output: lexal categories
"""
def generateLexalCat(s):
    """
    >>> generateLexalCat('%s cannot %s your %s')
    ('NOUN','VERB','NOUN')
    """
    cat = sen_lexalCat[s]
    return cat

"""
A function that randomly pick a sentence and outputs the lexal categories for
users
input: sentense selected
output: lexal categories, with duplicates being numbered
"""
def generateLexalCat2(s):
    """
    >>> generateLexalCat2('%s cannot %s your %s')
    ('NOUN','VERB','NOUN2')
    """
    cat = sen_lexalCat2[s]
    return cat

"""
A function that write to the html file with the lexal categories
input: lexal categories, a tuple, and s:sentence chosen
output: html code
"""
def generateHtml(lexal, s):
    global sen_lexalCat2
    lexal2 = sen_lexalCat2[s]
    
    line2 = "Enter an %s: <input type=text name=%s><br>" % (lexal[0], lexal2[0])
    line3 = "Enter an %s: <input type=text name=%s><br>" % (lexal[1], lexal2[1])
    line4 = "Enter an %s: <input type=text name=%s><br>" % (lexal[2], lexal2[2])
    
    print 'Content-Type: text/html'
    print
    print '<form action="Mad_Libs2.cgi">'
    print
    print line2
    print line3
    print line4
    print
    print '<input type=submit value="Okay">'
    print
    print '</form>'
   
       
sentenceChosen = generateSentence()
lexalCat = generateLexalCat(sentenceChosen)
lexalCat2 = generateLexalCat2(sentenceChosen)
generateHtml(lexalCat, sentenceChosen)

f = open("tmp.pck","w")
pickle.dump(sentenceChosen+'\n', f)
pickle.dump(lexalCat2, f)
f.close()



if __name__ == "__main__":
    import doctest
    doctest.testmod() 