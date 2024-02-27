# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:20:07 2020

@author: LRJPu
"""
import time
import turtle

seconds = 45
minutes = 59
hours = 7

clock= turtle.Turtle()
clock.color('red')
clock.pensize(5)
clock.shape('turtle')
while True: 
    clock.clear()
    clock.write(str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2), font= ('arial', 25, 'normal'))
    seconds= seconds + 1
    time.sleep(1)
    if seconds >= 60:
        seconds=0
        minutes= minutes +1
    else:
        seconds=seconds
   
    if minutes>= 60:
        minutes=0
        hours= hours+1
    else:
        minutes= minutes