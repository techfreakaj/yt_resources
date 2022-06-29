# Program to print logo of google.

import turtle

# get the instance of turtle
myTurtle = turtle.Turtle()
# select color
myTurtle.color('#4285F4', '#4285F4')  # RBG value of color
# change the pen size
myTurtle.pensize(5)
# change the drawing speed
myTurtle.speed(3)

myTurtle.forward(120)
myTurtle.right(90)
myTurtle.circle(-150, 50)  # first circle for red color
myTurtle.color('#0F9D58')
myTurtle.circle(-150, 100)
myTurtle.color('#F4B400')
myTurtle.circle(-150, 60)
myTurtle.color('#DB4437', '#DB4437')

myTurtle.begin_fill()
myTurtle.circle(-150, 100)
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.circle(100, 100)
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.end_fill()

myTurtle.begin_fill()

# second circle for yellow color

myTurtle.color("#F4B400", "#F4B400")
myTurtle.right(180)
myTurtle.forward(50)
myTurtle.right(90)

myTurtle.circle(100, 60)
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.circle(-150, 60)
myTurtle.end_fill()

# third circle of green color
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.circle(100, 60)
myTurtle.color('#0F9D58', '#0F9D58')
myTurtle.begin_fill()
myTurtle.circle(100, 100)
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.circle(-150, 100)
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.end_fill()

# Draw last circle

myTurtle.right(90)
myTurtle.circle(100, 100)
myTurtle.color('#4285F4', '#4285F4')
myTurtle.begin_fill()
myTurtle.circle(100, 25)
myTurtle.left(115)
myTurtle.forward(65)
myTurtle.right(90)
myTurtle.forward(42)
myTurtle.right(90)
myTurtle.forward(124)
myTurtle.right(90)
myTurtle.circle(-150, 50)
myTurtle.right(90)
myTurtle.forward(50)

myTurtle.end_fill()
myTurtle.penup()
