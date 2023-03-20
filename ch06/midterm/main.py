import turtle
import random

window = turtle.screensize()
turtle.Screen().bgcolor("black")

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

#Function For Positions of Tie Fighters, generating random:

def triangle_wave_function(x):
    count = 0
    while x > 1.0:
        count +=1
        if x % 2 == 0:
            x = 0
        else:
            x = int(50 * x) #Question
    return count

def triangle_wave_function_range(limit_fighters):
    coords_in_sequence = {}
    for i in range(2,limit_fighters):
        a = triangle_wave_function(i)
        coords_in_sequence[i] = a
    return coords_in_sequence
    
# Test Dictionary:
# def main():
#     limit_fighters = int(input("Deploy Tie Fighters:"))
#     triangle_wave_function_range_dict = triangle_wave_function_range(limit_fighters)
#     print(triangle_wave_function_range_dict)

# main()


#Drawing the Tie Fighters:


# Test Tuple:
# def tie_fighters(tie_fighters_dict):
#     tuple_position_tie_fighters = [(x,y) for x,y in tie_fighters_dict.items()]
#     return tuple_position_tie_fighters
# def main():
#     limit_fighters = int(input("Deploly Tie Fighters:"))
#     tie_fighters_dict = triangle_wave_function_range(limit_fighters)
#     coord_tie_fighters = tie_fighters(tie_fighters_dict)
#     print(coord_tie_fighters)

# main()

def wings():  #condense this part
    my_turtle.penup()
    my_turtle.color("green") #grey color
    my_turtle.pendown()
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.backward(200)
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
    my_turtle.left(180)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.backward(200)
    

def tie_fighters(my_turtle,tie_fighters_dict):
    tuple_position_tie_fighters = [(x,y) for x,y in tie_fighters_dict.items()]
    for g,z in tuple_position_tie_fighters:
        my_turtle.goto(g,z)
        my_turtle.dot(5, "red") #change to gray
        wings()
        my_turtle.penup

# def tie_fighters(tie_fighters_dict):
#     tuple_position_tie_fighters = [(x,y) for x,y in tie_fighters_dict.items()]
#     my_turtle.penup()
#     my_turtle.goto(500,400)
#     for i in range(len(tuple_position_tie_fighters)):
#         my_turtle.pendown
#         i = tuple_position_tie_fighters
#         my_turtle.goto(tuple_position_tie_fighters[i])
#         my_turtle.dot(5,color = "red")
#         wings()
#         my_turtle.penup()


#Laser:
def threenp1(n):
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
    my_turtle.penup
    for k,m in tuple_threeplus1_iters_dict:
        my_turtle.goto(k,m)
        my_turtle.color("green")
        my_turtle.pendown()
        


#Drawing Planets:
def death_star():
    # grey = (193,205,205)
    radius = [200,50]
    colors = ["white","black"]
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


# Final Main
def main():
    limit_fighters = int(input("Deploy Tie Fighters:"))
    heavenly_body()
    death_star()
    random_planet()
    tie_fighters_dict = triangle_wave_function_range(limit_fighters)
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    tie_fighters(my_turtle, tie_fighters_dict)
    upper_limit = 100000
    threeplus1_iters_dict = shooting_laser(upper_limit)
    laser_graph_coordinates(threeplus1_iters_dict)
    window.exitonclick()

main()