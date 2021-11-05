# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 1
# Author: Nguyen Minh (s3931605)
# Created date: 29/10/2021 21:33
# Last modified date: 29/10/2021

import random
import turtle


def main():
    """
    To run all question answers, uncomment to run any questions
    :return: none
    """

    # question1()

    # question2()

    # question3a()

    # question3b()

    # question3c()

    # question3d()

    question3e()

    # question4()

    # question5()

    # question6()

#---------------------------------
def question1():
    """prints “We like Python's turtles!” 10 times """
    # for index in range(10):
    #     print("We like Python's turtles!")

    print("We like Python's turtles!\n" * 10)


def question2():
    """ prints 10 random numbers between 25 and 35 """
    for index in range(10):
        print(random.randint(25, 35))


def question3a():
    """draw An equilateral triangle"""
    # set up a graphic window
    win = turtle.Screen()

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.color("green")
    brush.pensize(10)
    brush.shape("circle")

    # We have 3 sides so we loop 3 times to draw each side
    for index in range(3):
        brush.forward(300)
        brush.left(120)  # create an angle of 120 degree difference than the horizontal axis

    #remove the shape from brush at the end
    brush.hideturtle()

    # pause the screen until we click
    win.exitonclick()


def question3b():
    """draw a square"""
    # set up a graphic window
    win = turtle.Screen()

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.color("green")
    brush.pensize(10)
    brush.shape("circle")

    # We have 4 sides so we loop 4 times to draw each side
    for index in range(4):
        brush.forward(300)
        brush.left(90)  # create an angle of 90 degree difference than the horizontal axis

    #remove the shape from brush at the end
    brush.hideturtle()

    # pause the screen until we click
    win.exitonclick()


def question3c():
    """draw a hexagon"""
    # set up a graphic window
    win = turtle.Screen()

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.color("green")
    brush.pensize(10)
    brush.shape("circle")

    # We divide the shape into 6 equilateral triangle pieces so we loop 6 times to draw each piece
    for index in range(6):
        # start from the bottom point to the right and draw first side
        brush.left(60)  # create an angle of 60 degree difference than the horizontal axis
        brush.forward(100)

    #remove the shape from brush at the end
    brush.hideturtle()

    # pause the screen until we click
    win.exitonclick()


def question3d():
    """draw a octagon"""
    # set up a graphic window
    win = turtle.Screen()

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.color("green")
    brush.pensize(10)
    brush.shape("circle")

    # We divide the shape into 8 isoceles triangle pieces so we loop 8 times to draw each piece
    for index in range(8):
        # start from the bottom point to the right and draw first side
        brush.left(45)  # create an angle of 45 degree difference than the horizontal axis
        brush.forward(100)

    #remove the shape from brush at the end
    brush.hideturtle()

    # pause the screen until we click
    win.exitonclick()

def question3e():
    """draw all polygons from 3 to 8 slides"""
    #Initialize color list for each shape
    colorList = ["red", "blue", "black", "green","yellow", "pink"]
    # set up a graphic window
    win = turtle.Screen()

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.color("green")
    brush.pensize(10)
    brush.shape("circle")

    #Move to different location for beauty
    brush.up()
    brush.goto(-100,-200)
    brush.down()

    # We have n sides so loop n times
    for index in range(6):
        brush.color(colorList[index])
        drawPolygon(brush,index + 3)


    #remove the shape from brush at the end
    brush.hideturtle()

    # pause the screen until we click
    win.exitonclick()

def drawPolygon(brush,side):
    """

    :param side: numbers of sides of the polygon
    :param brush: the brush used to draw

    :return: none
    """
    for index in range(side):
        brush.forward(200)
        brush.left(360/side)

def question4():
    """draw a star shape like this"""
    # set up a graphic window
    win = turtle.Screen()
    win.bgcolor("red")
    # create object brush from Turtle and add some properties

    brush = turtle.Turtle()
    brush.pensize(10)
    brush.shape("circle")

    brush.color("yellow")

    #Move to different location for beauty
    brush.up()
    brush.goto(-100,-100)
    brush.down()

    # We divide the shape into 5 lines --> 1 line with different pattern
    # so we loop 4 times to draw 4 lines with same patterns

    brush.begin_fill()
    # Draw the initial line
    brush.left(72)
    brush.forward(300)

    # Draw the other lines that have same patterns
    for index in range(4):
        brush.right(144)
        brush.forward(300)

    brush.end_fill()

    brush.hideturtle()

    win.exitonclick()


def question5():
    """draw vietnamese flag like this"""
    # set up a graphic window with size 1000 1000 px , with red background
    win = turtle.Screen()
    win.setup(1000, 1000)
    win.bgcolor("red")

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.pensize(10)
    brush.shape("arrow")

    # Center the flag
    brush.up()
    brush.goto(-72, -144)
    brush.down()

    # fill the flag
    brush.color("yellow")
    brush.begin_fill()

    # Draw the initial line
    brush.left(36)
    brush.forward(100)

    # Loop to draw other line with same patterns
    for index in range(5):
        brush.right(72)
        brush.forward(200)

        brush.left(144)
        brush.forward(200)

    brush.end_fill()

    win.exitonclick()


def question6():
    """draw a clock shape like this"""
    # set up a graphic window
    win = turtle.Screen()
    win.setup(500, 500)
    win.bgcolor("purple")

    # create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.color("green")
    brush.pensize(5)
    brush.shape("turtle")

    # Clock have 12 hours --> each angle is 30 degree --> loop 12 times to draw each piece of the clock
    for index in range(12):
        # Set the vector 30degree to the left of the original vector
        brush.left(30)

        # move the brush 140px without trait
        brush.up()
        brush.forward(140)

        # draw a line 20px forward
        brush.down()
        brush.forward(20)

        # move the brush 20px forward without trait and stamp the brush shape
        brush.up()
        brush.forward(20)
        brush.stamp()

        # reset the position of the brush to its original position
        brush.goto(0, 0)
        brush.down()

    win.exitonclick()

main()

