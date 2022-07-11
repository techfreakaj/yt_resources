import turtle
from turtle import *

# Output screen
screen = turtle.Screen()

pen = turtle.Turtle()
speed(1)

pen.penup()
pen.goto(-200, 125)
pen.pendown()

# Orange Rectangle
pen.color("orange")
pen.begin_fill()
pen.forward(400)
pen.right(90)
pen.forward(84)
pen.right(90)
pen.forward(400)
pen.end_fill()
pen.left(90)
pen.forward(84)

#Green Rectangle
pen.color("green")
pen.begin_fill()
pen.forward(84)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(84)
pen.end_fill()

#Inner Blue Circle
pen.penup()
pen.goto(35, 0)
pen.pendown()
pen.color("navy")
pen.begin_fill()
pen.circle(35)
pen.end_fill()

#White circle
pen.penup()
pen.goto(30, 0)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

#Mini Blue Circles of Flag
pen.penup()
pen.goto(-27, -4)
pen.pendown()
pen.color("navy")
for i in range(24):
    pen.begin_fill()
    pen.circle(2)
    pen.end_fill()
    pen.penup()
    pen.forward(7)
    pen.right(15)
    pen.pendown()

#Small Blue Circle
pen.color("navy")
pen.penup()
pen.goto(10, 0)
pen.pendown()
pen.begin_fill()
pen.circle(10)
pen.end_fill()

#24 spokes of the Dharma chakra
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.pensize(1)
for i in range(24):
    pen.forward(30)
    pen.backward(30)
    pen.left(15)

#Stick of the flag
pen.color("Black")
pen.pensize(10)
pen.penup()
pen.goto(-200,125)
pen.right(180)
pen.pendown()
pen.forward(800)

turtle.done()
