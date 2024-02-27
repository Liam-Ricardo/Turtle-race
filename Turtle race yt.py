# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:12:16 2020

@author: LRJPu
"""

import time
import turtle
from turtle import Turtle
from random import randint

#window setup
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("forestgreen")
turtle.color("blue")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("Turtle Race",font=("Arial",30,"bold"))
turtle.penup()

#Dirt
turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#finish line
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color('black')
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range (10):
    turtle.setpos(finish_line, (150 - (i*square_size*2)))
    turtle.stamp()
    
for j in range(10):
    turtle.setpos(finish_line+ square_size, ((150-square_size)-(j*square_size*2)))
    turtle.stamp()
turtle.hideturtle()

#Turtle 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color('black')
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()

#Turtle 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color('cyan')
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()

#Turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color('magenta')
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()

#Turtle 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color('yellow')
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()

time.sleep(15)

#move the turtles
for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))

turtles= [turtle1,turtle2,turtle3,turtle4]
a=np.linspace[0,150,1]
if turtle1.xcor()==200:
       turtle.penup()
       turtle.color("blue")
       turtle.setpos(-140,100)
       turtle.write("Turtle 1 wins! ",font=("Arial",30,"bold"))
       turtle.penup()
       
if turtle2.xcor()==200:
       turtle.penup()
       turtle.color("blue")
       turtle.setpos(-140,100)
       turtle.write("Turtle 2 wins! ",font=("Arial",30,"bold"))
       turtle.penup()
if turtle3.xcor()==200:
       turtle.penup()
       turtle.color("blue")
       turtle.setpos(-140,100)
       turtle.write("Turtle 3 wins! ",font=("Arial",30,"bold"))
       turtle.penup()
if turtle4.xcor()==200:
       turtle.penup()
       turtle.color("blue")
       turtle.setpos(-140,100)
       turtle.write("Turtle 4 wins! ",font=("Arial",30,"bold"))
       turtle.penup()
    
turtle.exitonclick()
