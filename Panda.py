# simple python code to draw Panda

import turtle

myTurtle = turtle.Turtle()
turtle.Screen().bgcolor("gray")


def circles(color, radius):
    # Set the fill
    myTurtle.fillcolor(color)
    # Start filling the color
    myTurtle.begin_fill()
    # Draw a circle
    myTurtle.circle(radius)
    # Ending the filling of the color
    myTurtle.end_fill()


# Draw first ear
myTurtle.up()
myTurtle.setpos(-35, 95)
circles('black', 15)
# Draw second ear
myTurtle.up()
myTurtle.setpos(35, 95)
myTurtle.down()
circles('black', 15)
# ....... Draw face ......#
myTurtle.up()
myTurtle.setpos(0, 35)
myTurtle.down()
circles('white', 40)

# #####Draw eyes black#####
# Draw first eye
myTurtle.up()
myTurtle.setpos(-18, 75)
circles('black', 8)
# Draw second eye
myTurtle.up()
myTurtle.setpos(18, 75)
myTurtle.down()
circles('black', 8)
# #####Draw eyes white####
# Draw first eye
myTurtle.up()
myTurtle.setpos(-18, 77)
myTurtle.down()
circles('white', 4)
# Draw second eye
myTurtle.up()
myTurtle.setpos(18, 77)
myTurtle.down()
circles('white', 4)
# ####Draw nose####
myTurtle.up()
myTurtle.setpos(0, 55)
circles('black', 5)
# ####Draw mouth####
myTurtle.setpos(0, 55)
myTurtle.down()
myTurtle.right(90)
myTurtle.circle(5, 180)
myTurtle.up()
myTurtle.setpos(0, 55)
myTurtle.down()
myTurtle.left(360)
myTurtle.circle(5, -180)
