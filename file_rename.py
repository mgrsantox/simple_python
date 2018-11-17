#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:27:24 2018

@author: pysantosh
"""
import os

tns_table = str.maketrans("0123456789","          ","0123456789")

def file_rename():
    file_list = os.listdir("/home/pysantosh/Desktop/files")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir('/home/pysantosh/Desktop/files')
    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(tns_table))
    os.chdir(saved_path)

file_rename()
