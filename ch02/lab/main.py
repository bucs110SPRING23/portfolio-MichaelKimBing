#Part A:

#Race 1
import random
x1 = random.randint(1,100)
x2 = random.randint(1,100)
import turtle
window = turtle.Screen()
ford_turtle = turtle.Turtle()
ford_turtle.shape("turtle")
ford_turtle.color("blue")
ferrari_turtle = turtle.Turtle()
ferrari_turtle.shape("turtle")
ferrari_turtle.color("red")
ford_turtle.penup()
ferrari_turtle.penup()
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)
ford_turtle.pendown() #ask about if these turtle needs a line
ferrari_turtle.pendown()
ford_turtle.forward(x1)
ferrari_turtle.forward(x2)
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)






#Race 2:
y1 = random.randrange(1,100)
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)
for i in range (y1):    #confused on to making a loop
    ford_turtle.forward(i)
    ferrari_turtle.forward(i)
    ford_turtle.goto(-100,20)
    ferrari_turtle.goto(-100,-20)
window.exitonclick()





#Part B:
import pygame
import math
pygame.init()
window = pygame.display.set_mode()
screen_size = screen.get_size()
dimmensions1 = screen_size [0]/2, screen_size[1]/2
points= []
num_sides = int #ask them what does this mean?
side_length = int
for i in range ():
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    pygame.wait(1000)
window.fill("blue")
pygame.display.flip()
