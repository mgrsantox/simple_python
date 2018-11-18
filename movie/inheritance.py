#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:43:37 2018

@author: pysantosh
"""

class Parent():
    def __init__(self, name, eye_color):
        self.name = name
        self.eyecolor = eye_color
bill = Parent('Henry', 'Blue')
print(bill.name)