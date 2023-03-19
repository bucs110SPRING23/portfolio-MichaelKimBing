import turtle
import random

window = turtle.screensize()
turtle.Screen().bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")


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

#Function For Positions of Tie Fighters, generating random:
def wave_function(n)
    count = 0
    while n > 0:
        count +=1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    return count


#Coordinate System For Tie_Fights
def tie_fights_coordinates(limit_number_of_tie_fighters):
    objs_in_sequence = {}
    for i in range(2,limit_number_of_tie_fighters):
        a = threenp1(i)
        objs_in_sequence[i] = a
    return objs_in_sequence

#Drawing the Tie Fighters:
def tie_fighters():
    

# def tie_fighters(): 

def death_star():
    my_turtle.penup()
    my_turtle.goto(300,300)
    my_turtle.color((169,169,169))
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle()
    my_turtle.end_fill()



def alderon:
````my_turtle.penup()
    my_turtle.goto(300,300)
    my_turtle.color("blue")
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle()
    my_turtle.end_fill()


#Laser:
def threenp1(x):
    count = 0
    while n > 0:
        count +=1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    return count

def shooting_laser(upper_limit):
    objs_in_sequence = {}
    for i in range(2,upper_limit):
        a = threenp1(i)
        objs_in_sequence[i] = a
    return objs_in_sequence

def laser_graph_coordinates(threeplus1_iters_dict):
    tuple_threeplus1_iters_dict = [(n,iters) for n, iters in threeplus1_iters_dict.items()]
    my_turtle.penup()
    my_turtle.gotto()
    my_turtle.pendown()


# Final Main
def main():
    limit_number_of_tie_fighters = int(input("Enter The Number Of Tie Fighters:"))
    upper_limit = 1000

    heavenly_body()
    death_star()
    alderon()

main()