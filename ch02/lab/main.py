import random
import turtle
import pygame
import math


#Part A:

#Race 1:
window = turtle.Screen()
ford_turtle = turtle.Turtle()
ford_turtle.shape("turtle")
ford_turtle.color("blue")
ford_turtle.speed(1)
ferrari_turtle = turtle.Turtle()
ferrari_turtle.shape("turtle")
ferrari_turtle.color("red")
ferrari_turtle.speed(1)
ford_turtle.penup()
ferrari_turtle.penup()
x1 = random.randint(1,100)
x2 = random.randint(1,100)
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)
ford_turtle.forward(x1)
ferrari_turtle.forward(x2)
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)

#Race 2:
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)
for i in range(10):
    y1 = random.randrange(1,11)
    y2 = random.randrange(1,11)
    ford_turtle.forward(y1)
    ferrari_turtle.forward(y2)
ford_turtle.goto(-100,20)
ferrari_turtle.goto(-100,-20)
window.exitonclick()





#Part B:
pygame.init()
window = pygame.display.set_mode()
side_length = int(100)
xpos = 960
ypos = 540
window.fill("white")
for num_sides in [3, 4, 6, 20, 100, 360]:
    points= []
    for i in range(0,num_sides,1):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    pygame.draw.polygon(window, "blue", points)
    pygame.display.flip()
    pygame.time.wait(1000)
    window.fill("white")
    
    
    
    
    
