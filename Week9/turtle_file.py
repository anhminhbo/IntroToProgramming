import turtle


def main():
    draw_circle(180)

def draw_circle(radius):
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.circle(radius)
    pen.hideturtle()
    screen.exitonclick()

main()