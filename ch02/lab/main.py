#Part A:

#Race 1
import random
x = random.randint(1,100)
import turtle
window = turtle.Screen()
ford_turtle = turtle.Turtle()
ford_turtle.shape("turtle")
ford_turtle.color("blue")
ferrari_turtle = turtle.Turtle()
ferrari_turtle.shape("turtle")
ferrari_turtle.color("red")
for _ in ford_turtle.forward(x), ferrari_turtle.forward(x):
    ford_turtle.penup()
    ford_turtle.pendown()
    ferrari_turtle.penup()
    ferrari_turtle.pendown()
    ford_turtle.goto(-100,20)
    ferrari_turtle.goto(-100,-20)
window.exitonclick()