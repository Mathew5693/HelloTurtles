'''
Poly.py
Mathew Apanovich U72055800
Creates a polygon (minimum of 3 sides) based on user inputs such as sidelength, number of sides and color.
Then uses those polygons to create "pedals" based on the number of polygons the user decides
Fills the pedals with a random color if the user types yes
'''

import turtle
import random

#tutle settings and stuff
wn = turtle.Screen()
wn.title('Milti-Polygon!')
wn.colormode(255)
t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("white")
t.width(3)
#t.speed(0)

#user promts for inputs
numSides = wn.numinput('Polygon Creator', 'Enter number of sides:', 3, 3, 999)
lenSides = wn.numinput('Polygon Creator', 'Enter the length of the sides:', 50, 5, 999)
numPoly = wn.numinput('Polygon Creator', 'Enter the number of Polygons:', 3, 1, 99)
color = wn.textinput('Polygon Creator', 'Should the petals be filled(Yes or No)?')

#nested for loop

#first for loop to create multiple polygons based off the users input
for i in range(0, int(numPoly)):

    #randomizes color for filler just in case if the user selects yes
    randColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #if statement to comepare if user selected yes to fill petals, if true it will fill the petals
    if color == "Yes" or color == "yes":
        t.fillcolor(randColor)
        t.begin_fill()


#second for loop to create a signel polygon based off users input for number and length of sides
    for x in range(0, int(numSides)):
        t.forward(int(lenSides))
        t.left(360/numSides)

    t.end_fill()
    t.left(360/numPoly)


wn.exitonclick()
