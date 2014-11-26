# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 14:07:24 2014

@author: huxiangyu
"""

"""
Read in the rule and the the number of timesteps using the sys.argv function 
from the sys module
"""
import sys
ruleNum = sys.argv[1]
nStep = sys.argv[2]

ruleNum = int(ruleNum)
nStep = int(nStep)

"""
Create the binary representation of the rule, from left to right are next
timestep status from bit7 to bit0
input: the rule number, an integer
output: the corresponding binary representation, a string
"""

def ruleBinary(x):
    """
    >>> ruleBinary(30)
    '00011110'
    """
    i = 7
    y = str()
    while i >=0:
        if x & 2**i == 0:
            y = y + '0'
        else:
            y = y + '1'
        i = i - 1
    return(y)


ruleBin = ruleBinary(ruleNum) 

"""
Create the 8 bits in binary form
"""    
bit0 = '000'
bit1 = '001'
bit2 = '010'
bit3 = '011'
bit4 = '100'
bit5 = '101'
bit6 = '110'
bit7 = '111'

"""
Create the first line with length nStep + 1, the middle element to be 1, the 
rest to be 0's
inputs: expecting the number of timesteps, an integer
outputs: the first line of the image, a string
"""
def firstLine(x):
    """
    >>> firstLine(3)
    '0001000'
    """
    line = '0'*x + '1' + '0'*x
    return(line)

start = firstLine(nStep)

""" 
Check conditions for bits
input: 
    x: a string of length 3, with either 1 or 0 as elements
    y: the binary representation of a rule, a string
output: a string of length 1, which is the status of the next timestep
"""
def checkBit(x,y):
    """
    >>> checkBit('000', '00011110')
    '0'
    """
    if x == bit0:
        return(y[7])
    elif x == bit1:
        return(y[6])
    elif x == bit2:
        return(y[5])
    elif x == bit3:
        return(y[4])
    elif x == bit4:
        return(y[3])
    elif x == bit5:
        return(y[2])
    elif x == bit6:
        return(y[1])
    elif x == bit7:
        return(y[0])



"""
Create status for the next time step from the current line
input: 
    x: the current line, a string
    y: the binary representation of a rule, a string
output: the next line, a string
"""
def nextLine(x,y):
    """
    >>> nextLine('0001000', '00011110')
    '0011100'
    """
    # first element on the line
    f = '0'+ x[:2]
    new = checkBit(f,y)
    
    # the rest elements on the line up to the last element
    i = 1
    while i <= len(x)-2:
        new = new + checkBit(x[i-1:i+2],y)
        i = i + 1
        
    # the last element on the line
    l = x[len(x)-2:] + '0'
    new = new + checkBit(l,y)
    
    return(new)

"""
Create new lines untils the number of rows reaches the desired number
(2*nStep +1)
input: 
    x: the first line, a string
    y: the binary representation of a rule, a string
    z: the number of timesteps, an integer
output: the entire bitmap
"""
def bitMap(x,y,z):
    """
    >>> bitMap('0001000', '00011110', 3)
    P1 7 4
    0001000
    0011100
    0110010
    1101111
    """
    print 'P1', 2*z+1, z+1
    print x, '\n',    
    i = 1
    while i <= z:
        x = nextLine(x,y)
        print x, '\n',
        i = i+1

bitMap(start, ruleBin, nStep)


if __name__ == "__main__":
    import doctest
    doctest.testmod() 