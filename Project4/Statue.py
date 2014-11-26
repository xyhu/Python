# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 16:10:11 2014

@author: huxiangyu
"""

import os
os.chdir("/Users/huxiangyu/Documents/ZhengShi/Programming/CS9H/project4")

from Turtle import Turtle
from Vector import *
from Color import *

class Statue(Turtle):       #### Inherit behavior from Turtle
    """This Statue is a circle and will in the same place forever"""
    # Overwrites: add an argument
    def __init__(self, position, heading, pPerM, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.pixelperm = pPerM
    # change the shape of the statue to circle
    def getshape(self):
        
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*self.pixelperm, 
                self.position + forward*(6.0*self.pixelperm/7.0) + right*(4.0*self.pixelperm/7.0),
                self.position + forward*(4.0*self.pixelperm/7.0) + right*(6.0*self.pixelperm/7.0),
                self.position + right*self.pixelperm,
                self.position - forward*(4.0*self.pixelperm/7.0) + right*(6.0*self.pixelperm/7.0),
                self.position - forward*(6.0*self.pixelperm/7.0) + right*(4.0*self.pixelperm/7.0),
                self.position - forward*self.pixelperm,
                self.position - forward*(6.0*self.pixelperm/7.0) - right*(4.0*self.pixelperm/7.0),
                self.position - forward*(4.0*self.pixelperm/7.0) - right*(6.0*self.pixelperm/7.0),
                self.position - right*self.pixelperm,
                self.position + forward*(4.0*self.pixelperm/7.0) - right*(6.0*self.pixelperm/7.0),
                self.position + forward*(6.0*self.pixelperm/7.0) - right*(4.0*self.pixelperm/7.0),
                ]

