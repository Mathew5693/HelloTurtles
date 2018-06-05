'''
Poly.py
Mathew Apanovich U72055800
Creates a polygon (minimum of 3 sides) based on user inputs such as sidelength, number of sides and color.
'''

import turtle
wn = turtle.Screen()
wn.title('Polygon!')

t = turtle.Turtle()

i = 0
numSides = wn.numinput('Polygon Creator', 'Enter number of sides:', 3, 3, 999)
lenSides = wn.numinput('Polygon Creator', 'Enter the length of the sides:', 50, 5, 99)
color = wn.textinput('Polygon Creator', 'Enter a color (i.e. Red, Green, Blue):')

degree = 360/numSides

t.pencolor(color)
t.fillcolor(color)
t.width(5)

t.begin_fill()
while i != numSides:
    t.forward(lenSides)
    t.left(degree)
    i += 1

t.end_fill()


wn.exitonclick()