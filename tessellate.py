from turtle import *
import math

# SETUP
speed(5)
bgcolor("black")
color("purple")
pensize(0.7)
x = 70
c = 3 #nr of columns
r = 3 #nr of rows

penup()
hideturtle
left(180)
forward(2*x+30)
right(90)
forward(2*x)
right(90)
pendown()

def hexagon(x):
    for i in range(6):
        for i in range(6):
            forward(x)
            left(60)
        left(60)
    hideturtle()

def row(x,c):
    for i in range(c):
        hexagon(x)
        penup()
        forward(3*x)
        pendown()

def tessellate(x,c,r):
    for i in range(r):
        row(x,c)
        penup()
        backward(c*3*x)
        right(90)
        forward(math.sqrt(3)*x)
        left(90)
        pendown()


tessellate(x,c,r)
