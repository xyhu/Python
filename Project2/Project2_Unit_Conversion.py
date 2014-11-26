# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 21:49:42 2014

@author: huxiangyu
"""
import string

"""
Welcoming message to the users
"""
print "Welcome to our Python-powered Unit Converter v1.0 by Xiangyu Hu!You can convert Distances , Weights & Volumes to one another, but only within units of the same category, which are shown below. E.g.: 1 mi in ft"
print
print "\tDistances: ft cm mm mi m yd km in\n\tWeights: lb mg kg oz g\n\tVolumes: floz qt cup mL L gal pint\n"


"""
Creating Conversion table for distance. Using meter as the mediate unit for 
conversion. All the numbers denoted are conversion for 1 unit
"""

othersToMeter = {'ft': 0.3048,
                 'cm': 0.01,
                 'mm': 0.001,
                 'mi': 1609.34,
                 'yd': 0.9144,
                 'km': 1000,
                 'in': 0.0254,
                 'm': 1}

meterToOthers = {'ft': 3.28084,
                 'cm': 100,
                 'mm': 1000,
                 'mi': 0.000621371,
                 'yd': 1.09361,
                 'km': 0.001,
                 'in': 39.3701,
                 'm': 1}

"""
Creating Conversion table for weight. Using kilogram as the mediate unit for 
conversion. All the numbers denoted are conversion for 1 unit
"""

othersToKg = {'lb': 0.453592,
              'mg': 1e-6,
              'oz': 0.0283495,
              'g': 0.001,
              'kg': 1}
              
kgToOthers = {'lb': 2.20462,
              'mg': 1e+6,
              'oz': 35.274,
              'g': 1000,
              'kg': 1}             

"""
Creating Conversion table for volume. Using liter as the mediate unit for 
conversion. All the numbers denoted are conversion for 1 unit. Oz is US oz, 
qt(quart) is US quart, cup is US cup, gal is US gal, pint is US pint
"""
othersToLiter = {'floz': 0.0295735,
                 'qt': 0.946353,
                 'cup': 0.236588,
                 'ml': 0.001,
                 'gal': 3.78541,
                 'pint': 0.473176,
                 'L': 1}
                 
literToOthers = {'floz': 33.814,
                 'qt': 1.05669,
                 'cup': 4.22675,
                 'ml': 1000,
                 'gal': 0.264172,
                 'pint': 2.11338,
                 'L':1}                


""" 
Conversion for distance
input: amt, source_unit, dest_unit
output: the number after conversion in destination unit
"""
def distance(amt, source_unit, dest_unit):
    """
    >>> distance(10, 'mi','m')
    16093.440000
    """
    # Conversion to meters first
    sourceToMeter = amt * othersToMeter[source_unit]
    # then convert to dest_unit
    meterToDest = sourceToMeter * meterToOthers[dest_unit]
    return meterToDest

""" 
Conversion for weight
input: amt, source_unit, dest_unit
output: the number after conversion in destination unit
"""
def weight(amt, source_unit, dest_unit):
    """
    >>> weight(1, 'lb','oz')
    16.000000
    """
    # Conversion to kilogram first
    sourceToKg = amt * othersToKg[source_unit]
    # then convert to dest_unit
    kgToDest = sourceToKg * kgToOthers[dest_unit]
    return kgToDest




""" 
Conversion for weight
input: amt, source_unit, dest_unit
output: the number after conversion in destination unit
"""
def volume(amt, source_unit, dest_unit):
    """
    >>> volume(1, 'gal','qt')
    4.000000
    """
    # Conversion to liters first
    sourceToLiter = amt * othersToLiter[source_unit]
    # then convert to dest_unit
    literToDest = sourceToLiter * literToOthers[dest_unit]
    return literToDest

"""
Process conversion upon users request
input: user's request
output: the conversion result
"""   
def conversion(userRequest):
    """
    >>> conversion('10 mi in m')
    10 mi = 16093.440000 m
    >>> conversion('1 lb in oz')
    1 lb = 16.000000 oz
    """
    splitInput = string.split(userRequest)
    amt = float(splitInput[0])
    source_unit = splitInput[1]
    dest_unit = splitInput[3]

    # check if the user request for conversion of distance
    if source_unit in ('ft', 'cm', 'mm', 'mi', 'yd', 'km', 'in','m'):
        print amt, source_unit, "=", distance(amt,source_unit,dest_unit), dest_unit   

    # check if the user request for conversion of weight
    elif source_unit in ('lb', 'mg', 'kg', 'oz', 'g'):
        print amt, source_unit, "=", weight(amt,source_unit,dest_unit), dest_unit
    
    # check if the user request for conversion of volume
    elif source_unit in ('floz', 'qt', 'cup', 'mL', 'L', 'gal', 'pint'):
        print amt, source_unit, "=", volume(amt,source_unit,dest_unit), dest_unit
    # if nothing above, return error message
    else:
        print "The format of your unit for SOURCE_UNIT is wrong."

"""
Keep asking user input until user choose to quit
input: no argument needed
output: if user doesn't choose to quit, keep asking for new conversion/quit 
from user
"""
def keepAsking(): 
    userRequest = raw_input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ")
    if userRequest == 'q' or userRequest == 'quit':
        print "Thanks for converting with us. Y'all come back now, y'hear?"
    else:
        conversion(userRequest)       
        keepAsking()

keepAsking()

if __name__ == "__main__":
    import doctest
    doctest.testmod() 