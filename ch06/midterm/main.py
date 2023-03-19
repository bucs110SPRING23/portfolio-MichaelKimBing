import turtle
import random

window = turtle.screensize(canvwidth = 1920, canvheight= 1080, bg = "black")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")


#Drawing a single star
def star():
    x = 5
    my_turtle.color("white")
    my_turtle.begin_fill()
    while x > 0:
        my_turtle.forward(25)
        my_turtle.left(145)
        x = x - 1
    my_turtle.end_fill()


#Test:
# def main():
#     star()

# main()



#Drawing a bunch of stars
def heavenly_body():
    number_of_stars = 0
    while number_of_stars < 5:
        width = random.randrange(-300,300)
        height = random.randrange(-300, 300)
        star()
        my_turtle.penup()
        my_turtle.goto(width,height)
        my_turtle.pendown()
        my_turtle.speed(10)
        number_of_stars += 1



#Test:
# def main():
#     heavenly_body()

# main()


# def special_function_for_tie_fighter_positions():

# def tie_fights_coordinates():

# def tie_fighters(): 


