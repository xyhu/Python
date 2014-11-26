# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 17:20:32 2014

@author: huxiangyu
"""

import os
os.chdir("/Users/huxiangyu/Documents/ZhengShi/Programming/CS9H/project4")
from Turtle import Turtle
from Vector import *
from Color import *
from math import sin, cos, atan2, pi
from Mouse import *

class Cat(Turtle):       #### Inherit behavior from Turtle
    """This cat tries to catch the mouse."""

    def __init__(self, position, heading, center, cAngle, mouse, cRad, pPerM,
                 fill=red, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.center = center
        self.cAngle = cAngle
        self.mAngle = mouse.angle

        # pixel per meter, note that statue's radius is 1m
        self.pPerM = pPerM
        self.radius = cRad
        self.oldAngle = cAngle
        
    
    def getshape(self):
        """Overwrites the original one from baseclass-now a sqaure"""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        size = 4.0
        return [self.position + forward*size,
                self.position + right*size,
                self.position - forward*size,
                self.position - right*size]
    
    def getnextstate(self):
        """Overwrites the original one from baseclass-moving based on 
        visibility of the mouse
        >>> M = Mouse(Vector(200,170),0,Vector(200,200),10, 25)
        >>> C = Cat(Vector(200,140),0,Vector(200,200),0, M,25, 25)
        >>> C.getnextstate()
        Vector(200, 165), 0


        """
        # the relative position to the center of the statue
        adjPosition = self.position - self.center

        # if cat see the mouse, it moves towards the statues for 1m
        if (self.radius+ self.pPerM)*cos((self.cAngle - self.mAngle)*pi/180) >= 1.0 and self.radius >= self.pPerM:
            self.radius = self.radius - self.pPerM
            return self.position - unit(self.cAngle)*self.pPerM, self.heading
        # cat moves counterclockwise for 1.25m if it doesn't see the mouse, the distance between them >= 1m
        elif (self.radius+ self.pPerM)*cos((self.cAngle - self.mAngle)*pi/180) < 1.0 and self.radius >= self.pPerM:
            d = 1.25*self.pPerM
            # changes of angle(radian) for d distance move along the circle
            changesOfAngle = d/(self.radius + self.pPerM)
            # convert radian angle to degree angle
            changesOfAngle = changesOfAngle*180/pi
            # obtain new position of the mouse, and overwrites the self.position and angle
            self.position = adjPosition.rotate(-changesOfAngle) +  self.center
            # because the mouse moves counterclockwise, we subtract the changes of angle from current angle.
            self.cAngle = self.cAngle - changesOfAngle
            # the heading direction is perpendicular to the direction that angle is pointing to 
            self.heading = self.cAngle - 90
            return (self.position, self.heading)
        # the distance between cat and the statue is close enough that the cat cannot move 1m towards the statue
        elif self.radius < self.pPerM:
            d = 1.25*self.pPerM
            # changes of angle(radian) for d distance move along the circle
            changesOfAngle = d/(self.radius + self.pPerM)
            # convert radian angle to degree angle
            changesOfAngle = changesOfAngle*180/pi
            # assign current angle to be the old angle
            self.oldAngle = self.cAngle
            # update the self.cAngle to be the new angle
            self.cAngle = self.cAngle - changesOfAngle
            
            # the cat can catch the mouse, then stop there, no update on the position and angle
            if cos((self.mAngle - self.oldAngle)*pi/180) > cos((self.cAngle - self.oldAngle)*pi/180) and cos((self.cAngle - self.mAngle)*pi/180) > cos((self.cAngle - self.oldAngle)*pi/180) and self.oldAngle != self.cAngle:
                exit()
            # the cat cannot catch the mouse, then keep moving 1.25m along the circle
            else:
                # obtain new position of the mouse, and overwrites the self.position and angle
                self.position = adjPosition.rotate(-changesOfAngle) +  self.center
                # the heading direction is perpendicular to the direction that angle is pointing to 
                self.heading = self.cAngle - 90
                return (self.position, self.heading)


        
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()       
        
            