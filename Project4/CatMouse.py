# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 13:55:37 2014

@author: huxiangyu
"""
from Tkinter import *                  # Import everything from Tkinter
import os
os.chdir("/Users/huxiangyu/Documents/ZhengShi/Programming/CS9H/project4")
from Arena import Arena               # Import our Arena
from Cat  import Cat                  # Import our Cat
from Mouse  import Mouse              # Import our Mouse
from Statue import Statue             # Import our Statue
from Vector import *                  # Import everything from our Vector

"""
Obtain initial position based on the initial angle
input: angle, position at 0 degree (0 degree is at the top), center position of the statue
output: initial position
"""
def obInit(position, angle, center):
	"""
	>>> p = Vector(230, 200)
	>>> angle = 90
	>>> c = Vector(200,200)
	>>> obInit(p,angle,c)
	Vector(200, 170)
	"""
	if angle > 360.0:
	    angle = angle - 360
	if angle < - 360:
	    angle = -angle - 360
	if angle > -360 and angle < 0:
	    angle = -angle
	adjPosition = position - center
	newposition = adjPosition.rotate(angle) + center
	return newposition






tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen

# pixel meter conversion
pixelPerM = 25

# Create a statue with the corresponding position, heding = 0, up
s_posi = Vector(200,200)
arena.add(Statue(s_posi, 0, pixelPerM)) 

""" Create a mouse with the corresponding position and initial angle"""
# the initial angle where the mouse starts
m_angle = 396.0
# heading direction is perpendicular to the angle
m_head = m_angle - 90
# the 0 degree position for mouse.The distance a little bigger than the radius since I don't want part of their 
m_posi0 = Vector(s_posi.x,s_posi.y - pixelPerM - 5)
# obtain the initial position of the mouse
m_posi_start = obInit(m_posi0, m_angle, s_posi)
# create a mouse instance
M = Mouse(m_posi_start,m_head,s_posi,m_angle, pixelPerM)
arena.add(M)


""" Create a cat with the corresponding position and initial angle"""
cRadius = 4.0*pixelPerM
# this angle is the initial angle where the mouse starts
c_angle = 35.0
c_head = c_angle - 90

# the 0 degree position for cat. The distance a little bigger than the radius since I don't want part of their 
# body overlap with the statue
c_posi0 = Vector(s_posi.x, s_posi.y - pixelPerM - cRadius - 10)
# obtain the initial position of the mouse
c_posi_start = obInit(c_posi0, c_angle, s_posi)
# create a cat instance
C = Cat(c_posi_start,c_head,s_posi,c_angle, M,cRadius, pixelPerM)
arena.add(C)

M.cat = C


tk.mainloop()                          # Enter the Tkinter event loop

if __name__ == "__main__":
    import doctest
    doctest.testmod()