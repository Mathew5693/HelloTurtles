'''
benfordturtle.py
Mathew Apanovich U72055800
creates a bar graph based on the frequency of a the leading digit from a list
of numbers that is read in from a text file input by the user if that file is in the
benfordturtle directory
'''

import turtle

# turtle stuff
wn = turtle.Screen()
t = turtle.Turtle()

# more turtle stuff
wn.title('Benford: Leading Number Frequency Data!')
turtle.bgcolor("black")
turtle.setworldcoordinates(-1, 100, 100, -1)
print(t.position)
t.pencolor("white")
t.fillcolor("red")
t.width(2)
t.penup()
# t.speed(10)


def first(r):
    # gets first digit and returns it
    while r >= 10:
        r //= 10
    return r


def make_bar(tur, total, array):

    # for loop to count digit freq between 1 and 9
    # then draws bars based on data using turtle
    for m in range(1, 10):

        c = array.count(m)
        p = 100.0 * float(c) / float(total)

        tur.pendown()
        tur.begin_fill()
        tur.forward(c*5)
        tur.write(str(m) + ", " +str(p)+"%")
        tur.left(90)
        tur.forward(5)
        tur.left(90)
        tur.forward(c*5)
        tur.end_fill()
        tur.penup()
        tur.right(90)
        tur.forward(5)
        tur.right(90)


n = 0

# opens file from user input if the file is in the benford turtle directory
# strips the file input to just digits to be converted int later on
with open(wn.textinput('File Reader', 'Enter File name from Benford Directory:'), 'r') as f:
    count = []
    count = f.readlines()
    count = [x.strip() for x in count]
f.close()

# increments n for total items in the list and
# converts array list to integer, then gets the first digit
digit = []
for i in range(0, len(count)):
    count[i] = int(count[i])
    b = count[i]
    v = first(b)
    digit.append(v)
    n += 1

# draws the bars based off the information from the list
# takes in t (turtle), n(total items in list), and digits(array of first digits from list)
make_bar(t, n, digit)


wn.exitonclick()
