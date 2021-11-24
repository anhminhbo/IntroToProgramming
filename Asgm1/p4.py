# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 09/11/2021 21:18
# Last modified date: 09/11/2021 23:32

import turtle
# # exercise3 = __import__('3')
#
# def main():
#     # total_flour_in_kg,decision,total_cost = exercise3.flour_order(10,5,5,10)
#
#     draw_bar_chart("01/01/2021",4,0,0,10)



def draw_bar_chart(record_date, large_thick, large_thin, medium_thick, medium_thin):
    """
    Draw bar chart for total pizzas sold
    :param record_date: date to show on x-axis
    :param large_thick: quantity of this kind of pizza
    :param large_thin: quantity of this kind of pizza
    :param medium_thick: quantity of this kind of pizza
    :param medium_thin: quantity of this kind of pizza
    :return: none
    """
    # Create a list content type of pizza
    type_of_pizza = [large_thick,large_thin,medium_thick,medium_thin]

    # Calculate total pizzas
    total_pizzas = calculate_total_pizzas(large_thick, large_thin, medium_thick, medium_thin)

    # Create a color list for each bar
    color_list = ["red","pink","green","blue"]

    # Set up screen
    screen = setup_screen()

    # Set up pen
    pen = setup_pen()

    # Draw x-y axis
    draw_x_y_axis(pen,total_pizzas)

    # Draw date
    draw_date(pen,record_date)

    # Create reset Position to reset after each draw of a pizza bar
    resetPosition = (-130, -400)

    # Loops numbers of pizza types to draw each pizza bar
    for index in range(len(type_of_pizza)):
        # Go to the reset Position to begin draw
        reset_position(pen,resetPosition)

        # Draw each pizza bar with input pizza type and color
        pen.setheading(180)
        resetPosition = draw_bar(pen,type_of_pizza[index],color_list[index])

    # Go to the reset Position to begin draw next thing
    reset_position(pen, resetPosition)

    # draw total pizzas above the bar chart
    draw_total_pizzas(pen,total_pizzas)

    screen.exitonclick()

def setup_screen():
    """
    Set up and return the screen of Turtle
    :return: screen of Turtle
    """
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)

    return screen

def setup_pen():
    """
    Set up and return the pen to draw
    :return: pen of Turtle
    """
    pen = turtle.Turtle()
    pen.pensize("0")
    pen.shape("arrow")

    # Set up this initial position to draw
    pen.up()
    pen.goto(-200,-400)
    pen.down()

    return pen

def draw_x_y_axis(pen,total_pizza_s):
    """
    Draw the x and y axis
    :param pen: pen Turtle to draw
    :param total_pizza_s: total of pizzas
    :return: none
    """
    # Draw the y-axis
    pen.setheading(90)
    pen.forward(total_pizza_s*10 + 20)
    pen.stamp() # Stamp to create the shape of the pen

    # Reset position to draw next thing
    pen.goto(-200, -400)

    # Draw the x-axis
    pen.setheading(0)
    pen.forward(200)
    pen.stamp()# Stamp to create the shape of the pen


def draw_date(pen,date):
    """
    Draw the date below the bar
    :param pen: pen Turtle to draw
    :param date: the input date to draw below the bar
    :return: none
    """
    # Set up the position to draw
    pen.up()
    pen.goto(-140,-420)
    pen.down()

    # pen.write() to write the date with given font
    pen.write(date, font=("Arial", 16,"normal"))

def draw_bar(pen,pizza_type,color_type):
    """
    Draw bar for each pizza
    :param pen: pen Turtle to draw
    :param pizza_type: pizza type
    :param color_type: color for each pizza bar
    :return: tuple
    """
    # Initialize draw position for each bar
    draw_position = ()

    # Begin fill with the input color
    pen.begin_fill()
    pen.color(color_type)

    # Divide the rectangle bar into 2 sides with same pattern => loop 2 times to draw each side
    for index in range(2):
        # draw the height of bar
        pen.right(90)
        pen.forward(pizza_type*10)

        # Handle this to output the reset position to draw next pizza bar
        if index == 0:
            draw_position = pen.position()

        # draw the width of bar
        pen.right(90)
        pen.forward(55)

    # End fill to fill the given color for the bar shape
    pen.end_fill()

    return draw_position

def calculate_total_pizzas(large_thick_quantity, large_thin_quantity, medium_thick_quantity, medium_thin_quantity):
    """
    Calculate and return the total of pizzas
    :param large_thick_quantity: quantity of this kind of pizza
    :param large_thin_quantity: quantity of this kind of pizza
    :param medium_thick_quantity: quantity of this kind of pizza
    :param medium_thin_quantity: quantity of this kind of pizza
    :return: integer
    """
    return large_thick_quantity + large_thin_quantity + medium_thick_quantity + medium_thin_quantity

def draw_total_pizzas(pen,total):
    """
    Draw total pizzas above the bar graph
    :param pen: pen Turtle to draw
    :param total: total of pizzas
    :return: none
    """
    # Change color to write
    pen.color("black")

    # Write the given pizzas with font because total_pizzas is int ==> convert to str
    pen.write(str(total), font=("Arial", 16,"normal"))

    # Hide the turtle for beauty
    pen.hideturtle()


def reset_position(pen,position):
    """
    Set the pen to go to reset Position to begin draw
    :param pen: pen of Turtle to draw
    :param position: the position for each repetitive drawing
    :return: none
    """
    pen.up()
    pen.goto(position[0], position[1])
    pen.down()

# main()



