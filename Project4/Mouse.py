# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 17:19:43 2014

@author: huxiangyu
"""
import os
os.chdir("/Users/huxiangyu/Documents/ZhengShi/Programming/CS9H/project4")
from Turtle import Turtle
from Vector import *
from Color import *
from Cat import *
class Mouse(Turtle):       #### Inherit behavior from Turtle
    """This Mouse moves in a circle forever."""

    def __init__(self, position, heading, center, angle, pPerM, cat=None, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.center = center
        # in degree
        self.angle = angle
        self.pPerM = pPerM
        # in degree
        self.cat = cat
    
    """Overwrites the original one from baseclass-now moving in a circle"""       
    def getnextstate(self):
        """
        >>> 
        >>> M = Mouse(Vector(230,200),0,Vector(200,200),90, 25)
        >>> C = Cat(Vector(170,200),0,Vector(200,200),270, M,1, 25)
        >>> M.cat = C
        >>> M.getnextstate()
        Vector(220.17, 177.79), -47.75

        """
        # if the cat catches the mouse, then mouse won't move
       
        if cos((self.angle - self.cat.oldAngle)*pi/180) > cos((self.cat.cAngle - self.cat.oldAngle)*pi/180) and cos((self.cat.cAngle - self.angle)*pi/180) > cos((self.cat.cAngle - self.cat.oldAngle)*pi/180) and self.cat.radius < self.pPerM and self.cat.oldAngle != self.cat.cAngle:
            exit()
        #if not, the mouse keeps moving along the circle
        else:
            # the relative position to the center of the statue
            adjPosition = self.position - self.center
            # obtain radius from the mouth to the center of the statue
            radius = adjPosition.length()
            # distance that the mouse move every step: 1m
            d = 1* self.pPerM
            # changes of angle(radian) for d distance move along the circle
            changesOfAngle = d/radius
            # convert radian angle to degree angle
            changesOfAngle = changesOfAngle*180/pi
            # obtain new position of the mouse, and overwrites the self.position and angle
            self.position = adjPosition.rotate(-changesOfAngle) +  self.center
            # because the mouse moves counterclockwise, we subtract the changes of angle from current angle.
            self.angle = self.angle - changesOfAngle
            # the heading direction is perpendicular to the direction that angle is pointing to 
            self.heading = self.angle - 90
            return (self.position, self.heading)
    
    def getshape(self):
        """Overwrites the original one from baseclass-now a sqaure"""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        size = 2.5
        return [self.position + forward*size,
                self.position + right*size,
                self.position - forward*size,
                self.position - right*size]

if __name__ == "__main__":
    import doctest
    doctest.testmod()