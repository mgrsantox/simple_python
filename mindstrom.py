#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:21:20 2018

@author: pysantosh
"""

import turtle
window = turtle.Screen()
window.bgcolor('green')

def draw_square():
    count = 0
    santosh = turtle.Turtle()
    santosh.speed(3)
    while(count<4):    
        santosh.forward(100)
        santosh.rt(90)
        count +=1
def draw_circle():
    rana = turtle.Turtle()
    rana.shape('arrow')
    rana.color('yellow')
    rana.circle(100)
    
 

draw_square()
draw_circle()
window.exitonclick()