#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:45:41 2018

@author: pysantosh
"""
import webbrowser as wb
class Movie():
    def __init__(self, movie_title, movie_image, movie_story, movie_trailer):
        self.title = movie_title
        self.image_url = movie_image
        self.story = movie_story
        self.trailer_youtube_url = movie_trailer
        
    def show_trailer(self):
        wb.open(self.trailer_youtube_url)
