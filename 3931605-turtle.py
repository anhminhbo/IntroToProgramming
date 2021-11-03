# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 03/11/2021 11:33
# Last modified date: 03/11/2021 15:35

import math
import turtle

def main():
    """
    Run the main program to draw I <3 U for your lover
    :param: none
    :return: none
    """

    # set up a graphic window
    win = turtle.Screen()

    # Create a window screen of width x height: 1200x1200 which means that
    # x-axis(-600 to 600 from bottom to top)
    # y-axis(-600 to 600 from left to right)
    win.setup(width = 1200, height =1200)
    win.bgcolor("green")

    #create object brush from Turtle and add some properties
    brush = turtle.Turtle()
    brush.pensize(5)
    brush.shape("turtle")

    #Initalize the brush position on screen for letter I
    brush.up()
    brush.goto(-400,300)
    brush.down()


    # draw I
    drawI(brush)

    # move the brush to heart position
    brush.up()
    brush.goto(0,-150)
    brush.down()

    # draw Heart
    drawHeart(brush)

    #move the brush to letter U position
    brush.up()
    brush.goto(400,-300)
    brush.setheading(180)
    brush.down()

    # draw letter U
    drawU(brush)

    win.exitonclick()

def drawI(brush):

    """
    draw letter T on the screen
    :param: brush: the pen we create to draw
    :return: none
    """

#     fill color
    brush.color('yellow')
    brush.begin_fill()

# Divide I into 2 pieces with same pattern --> loop 2 times to draw each patern
    for index in range(2):
        brush.forward(100)

        brush.right(90)
        brush.forward(100)

        brush.right(90)
        brush.forward(50)

        brush.left(90)
        brush.forward(400)

        brush.left(90)
        brush.forward(50)

        brush.right(90)
        brush.forward(100)

        brush.right(90)
        brush.forward(100)

    brush.end_fill()

def drawHeart(brush):
    """
    draw heart on the screen
    :param: brush: the pen we create to draw
    :return: none
    """

    #     fill color
    brush.color('red')
    brush.begin_fill()

    #draw heart
    # Draw the bottom of the heart
    brush.left(140)
    brush.forward(180)

    # circle help we draw a circle
    #-90:clock-wise 90 radius, 200 degrees circle only not 360 degrees full circle
    brush.circle(-90, 200)

    #setheading is get a 60 degree angle from right to left at current position
    brush.setheading(60)

    #draw half heart
    brush.circle(-90, 200)
    brush.forward(180)

    brush.end_fill()

def drawU(brush):
    """
    draw letter U on the screen
    :param: brush: the pen we create to draw
    :return: none
    """

    #     fill color
    brush.color('yellow')
    brush.begin_fill()

    # draw letter U
    # Draw the right part of U
    brush.forward(100)

    brush.right(90)
    brush.forward(600)

    brush.right(90)
    brush.forward(50)

    brush.right(90)
    brush.forward(500)

    brush.left(90)
    brush.forward(50)


    #Draw the left part of U
    brush.forward(50)

    brush.left(90)
    brush.forward(500)

    brush.right(90)
    brush.forward(50)

    brush.right(90)
    brush.forward(600)

    brush.right(90)
    brush.forward(100)

    brush.end_fill()

    brush.hideturtle()


main()



