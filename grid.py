'''
Poly.py
Mathew Apanovich U72055800
Creates a user defined grid using turtle by taking in the amount of space between each line from the user.
'''

import turtle

#provides user with interface
turtle.setup(800, 600)
wn = turtle.Screen()
wn.title('Welcome to the Grid!')

#call turtle, increase width and speed of turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

#promts user for spacing
spacing = wn.numinput('Grid', 'Enter grid spacing:', 10, 10, 100)

#stores width and height of screen
(width, height) = wn.screensize()

t.penup()
t.setposition(-width, height)
t.pendown()

#defines x and y to the screen length, then divines by the spacing input by the user
#to tell the program how many lines can fit in the screen. Also used to increment for loops.
x = (width * 2)/spacing
y = (height* 2)/spacing


#for loops to space each line for the grid

#creates horizontal lines for the grid
for i in range(int(y) + 1):

    (xpos, ypos) = t.position()
    t.forward(width * 2)
    t.penup()
    t.setposition(xpos, ypos - spacing)
    t.pendown()

#reset the position of the turtle when all verticle lines are finished
t.penup()
t.setposition(-width, height)
t.pendown()
t.right(90)

#creates vertical lines for the grid
for j in range(int(x) + 1):

    (xpos, ypos) = t.position()
    t.forward(height * 2)
    t.penup()
    t.setposition(xpos + spacing, ypos)
    t.pendown()


wn.exitonclick()