#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:56:14 2018

@author: pysantosh
"""

import webbrowser
import time
brk=0
while(brk<3):    
    print('this program is started at '+time.ctime())
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=cEuU64Zt4B0")
    brk+=1