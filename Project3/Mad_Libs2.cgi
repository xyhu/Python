#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:18:38 2014

@author: huxiangyu
"""
import cgitb
cgitb.enable() # remember to change directory here

import cgi
import pickle

"""
A function that format the keys and values in form in the desired order. 
Otherwise, the dictionary ordered the item automatically, which is not what we
want
input: a dictionar-like object returned by cgi.FieldStorage(), keys in the desired order
output: values
"""
def desiredOrder(form, lexal):
    values = []
    values.append(form.getvalue(lexal[0]))
    values.append(form.getvalue(lexal[1]))
    values.append(form.getvalue(lexal[2]))
    return values


f = open("tmp.pck","r")
sentenceChosen = pickle.load(f)
lexalCat2 = pickle.load(f)
f.close()

form = cgi.FieldStorage()
userInput = tuple(desiredOrder(form,lexalCat2))


print 'Content-Type: text/html'
print
print sentenceChosen % userInput
print '\n'
print '<a href="http://inst.eecs.berkeley.edu/~cs9h-cd/Mad_Libs.cgi">Do it Again</a>'
print

if __name__ == "__main__":
    import doctest
    doctest.testmod() 