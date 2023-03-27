#We left off talking about classes, and the idea for a class is essentially a blue print for an object, which is a description of what this object is made of and what is the object made of

#Example:
class Point:
    """docstring for Point"""

    def __init__(self):
        self.xcoor = 0
        self.ycoor = 0
        self.color = "red"
        #We don't care of the actual value of the data we only care of the actual result of the data

#You can thinkg of class == type (which is pretty much the same thing, describing the type of what it does)
#Class are named with TitleCase meaning like: class ColorPoint 
        #It is not standard to do lower case like colorPoint

#to import it from a different file you just do:
import point #which this calls for that class
#Basically when you are a calling the class, what python is doing is:
    #1. look in the current folder for the file/module
    #2. look in python installed modules
    #3. look in the python library
#If you have a import that is located in a folder within the folder
import extrafolder.module
#If you didnt want do keep doing folder within in the folder you can do
from extrafolder.module import point


p1 = point.Point() #initialize a point object
print(p1.xcoor,p1.ycoor,p1.color, type(p1))
p2 = point.Point() #initialize another point object

#Cases:

#snakecase: snake_case, underscores for spaces, all lowercase
#camelcase: camelCase, capital for spaces, starts lowercase
#TitleCase: TitleCase, capital for spaces, starts capital


#With classes you can apply default parameters and pass them:
class Point:
    """docstring for Point"""

    #functions are called methods when they in a class - when you see a method you woul say that it is part of the class
    #thirst parameter to any medthos id 'self'
    def __init__(self, x=0, y =0, color = "red"): #of course if you call this with changing of the variables those will change the value of those parameters
        #the "self." part in this code is basically ties the data into the objects scope
        self.xcoor = x
        self.ycoor = y
        self.color = color


#Let's say we had:
import turtle
points = []
for p in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    points.append(point.Point(x,y,"orange"))


t = turtle.Turtle()
for p in points:
    t.color(p.color)
    t.goto(p.xcoor,p.ycoor)

turtle.Screen().exitonclick()



#We can also do additional functionality in a class so let's say we had:
import random #you need to import into the class like this
class Point:
    def __init__(self, x=0, y =0, color = "red"):
        self.xcoor = x
        self.ycoor = y
        self.color = color

    def random_color(self):
        new_color = [
            random.randint(0,255), #this should work but not too sure what the rgb needs either tuple or list
            random.randint(0,255),
            random.randint(0,255)
        ]
        self.color = new_color
        #No return is needed

    #Now what this function will do is then add in another condition where the program will change the rgb value of the color

    #Now in the other file when you do 
    t = turtle.Turtle():
    for p in points:
        p.random_color("red") #This will give you an error by stating 2 arguments since the random_color has self as an argument as so it is the p. as one argument and then whatever you put which in this case is "red" as the 2nd argument
        p.random_color() #this is the correct way since you already gave the argument from the Point class
        t.color(p.color)
        t.goto(p,xcoor,p.ycoor)



#MVC - Model Biew Controller
#This is the basically the general GUI program that you will need to do and technically it is for accumulator patterns
#This assist us with helping complex code

#The usefulness is it helps us with Design Patterns
#Design Patterns - language independent

#Basic design for the MVC is:

#View - displays things on screen
    #pygame is what helps what should be in the view
    #turtle is another "view" that we could use

#Controller - controls things on screen