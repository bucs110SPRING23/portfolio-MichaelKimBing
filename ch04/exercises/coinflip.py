import turtle
import random

window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.speed(0)
distance = 10
angle = 0 
is_in_screen = True

flip = []
while is_in_screen:
    coin = random.randint(0,1)
    if coin:
        my_turtle.right(angle)
    else:
        my_turtle.left(angle)
    my_turtle.forward(distance)

    turtleX = my_turtle.xcor()
    turtleY = my_turtle.ycor()

    x_range = window.window_width()/2
    y_range = window.window_height()/2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False

# window.exitonclick()