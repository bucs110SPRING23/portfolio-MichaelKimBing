import turtle
import random

my_turtle = turtle.Turtle()

#Drawing a single star
def star():
    my_turtle.color("white")
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(25)
        my_turtle.left(145)
    my_turtle.end_fill()


#Drawing a bunch of stars
def heavenly_body():
    number_of_stars = 0
    while number_of_stars < 25:
        star()
        width = random.randrange(-800,800)
        height = random.randrange(-300,300)
        my_turtle.penup()
        my_turtle.goto(width,height)
        my_turtle.pendown()
        my_turtle.speed(10)
        number_of_stars += 1
    return number_of_stars


#Laser:
def laser_generator():
    colors = ["blue","green"]
    my_turtle.penup()
    my_turtle.goto(-330,-20)
    for c in colors:
            my_turtle.dot(60,c)
    
def laser_line(space,x,y):
    my_turtle.penup()
    my_turtle.goto(-330,0)
    my_turtle.color("green")
    my_turtle.pendown()
    my_turtle.right(290)
    for i in range(x):
        for _ in range(y):
            my_turtle.dot()
            my_turtle.forward(space)
            my_turtle.backward(space*y)
    my_turtle.forward(space)
    my_turtle.dot(100,"red")
    my_turtle.penup()

def explosion_function(w):
    while w >= 0:
        if w == 0:
            w = 0
        elif 1 <= w <= 3:
            w = int(50000)
        elif 4 <= w <= 6:
            w = int(500000)
        elif 7 <= w <= 10:
            w = int(50000000* w)
        else:
            w = int(5500000000)         
        return w

def explosion_function_range(intensity):
    coords_in_sequence = {}
    for i in range(0,intensity+1):
        a = explosion_function(i)
        coords_in_sequence[i] = a
    return coords_in_sequence

def casualities_number(numbers_of_people):
    tuple_explosion = [(i,values) for i, values in numbers_of_people.items()]

    values_explosion = [tup[1] for tup in tuple_explosion]
    max_so_far = values_explosion[1]
    for i in range(len(values_explosion)):
        if values_explosion[i] > max_so_far:
            max_so_far = values_explosion[i]
    my_turtle.goto(-400,300)
    my_turtle.color("yellow")
    my_turtle.write(f"Number of Casualities:{max_so_far}",font=["None",36])
    

#Drawing Planets:
def death_star():
    radius = [200,50]
    colors = ["grey","black"]
    my_turtle.penup()
    my_turtle.goto(-300,0)
    my_turtle.pendown()
    for r in radius:
        my_turtle.begin_fill()
        my_turtle.circle(r)
        my_turtle.end_fill()
        for c in colors:
            my_turtle.color(c)

def random_planet():
    my_turtle.penup()
    my_turtle.goto(200,100)
    my_turtle.color("blue")
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle(100)
    my_turtle.end_fill()
    my_turtle.penup()


# Main
def main():
    window = turtle.Screen()
    turtle.Screen().bgcolor("black")
    intensity = int(input("Enter Explosion Intensity:"))
    space = 10
    x = 2
    y = 5
    heavenly_body()
    death_star()
    random_planet()
    laser_generator()
    my_turtle.penup()
    laser_line(space,x,y)
    numbers_of_people = explosion_function_range(intensity)
    casualities_number(numbers_of_people)
    window.exitonclick()

main()