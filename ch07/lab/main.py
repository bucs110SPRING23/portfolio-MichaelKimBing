#We will go over the substitutions and review what we did before:
#Substituions Exercise:
    #Remember you want to use one list to modify anothe list
    #Make you sure which list you should loop through if you want to modify
    #The reason they did k,v is it means whatever key or word that is reads it will replace it with the respective term which in this case is considered as v
    #in some cases you might want to replace everything as lower case when sending it out to the news article
            file_pointer = open("news.txt","r").lower()

    #remember that (dictionary).items(): {k:v,k1:v1,k2:v2, k3:v3, ...} ===> [(k,v), (k1,v1), (k2,v2), (k3,v3),...]

#Chapter 7:
#As you have been noticing, one of the things that becomes difficult is managing complexity
    #Any sort of advanced programming just manages complexity
    #Unix - basis of the idea of unix and the first iterating was ahut 10000 SLOC (source lines of code)
    #Chrome - 10,000,000 SLOC
    #OS X - 100,000,000 SLOC

#So we need someway to compartmentalize the program that doesnt require us to setting up the program
#We met with one situation and this case called complex objects
    #Primitives: int, str, fload, lists, drect, tuple
    #Turtle: x(int), y, eading, color(color), pensize(int)
        #Turle even has this situation - but what we want ot od have a type of the stuation
        #You can have it set as a dictiornary, but it doesnt tell you what to do

#We want to create something that gives us a way to bundle data and functions together:
    #First we need two things:
        #State - the current values of the data in the object
            #ie) what value of the x-coordinate is and what is the y-coordinate is on the coordinate grid 
        #Behavior - the functions that operate on the data in the object

#Over the next few courses, we are just gonna make a program that clicks on various parts of the screen
#First we will start with a point
    #Remember that the object should do one thing, it shouldn't only worry what it does to itself
    #State: x,y, color
    #Behavior: change_color,move


#We can think about this as Classes == Type (classes is the same thing as type)
import turtle
print(type(turtle.Turtle))
    # u see the class of the turtle
print(type(1))
    #If you notice there is no class different between the tyoes

t - turtle.Turtle()
print(type(t)) #complex
print(type(1)) #primitive
#This command wil produce the same time

#class are blueprints for objects
    #functions are stored algoithms
    #class as a stored data tyoe.
    #classes are nnot executable in code
    #Do not put executable code in global scope, deffiitions are fund{}


#Let's say we want a point object, then you need a point class
#Point class:
    #Instance: An object created from a speciic class
        #ie) t= turtle.Turtle() - t is an instance of Turtl
    #Instance variable : a variable that is paart of the inteance
        #ie) t,x,t.pos #nd pos are instance variabes
    #Interface: The functions and vaiables of an object
        #t.foward() #forward() part of the interface if turtle


#Point - there is no point "object" there is in a point, so you have to make it a class yourself

#To define a class:

###point.py - assuming this example is called this python
#def make_point(x,y): this has an alorithm that already has a class type- 
class Point:
        #style guides - user types always start with a capital letter when defining a class!
        #Usually, classes go in their own file
        #1 class per file
        pass #leave it like that so we come back to it later

### main.py

import point    #we have to name the module first
point.Point()
p1 = point.Point() #and the same way just like turtle you can do that - p1 is an instance of Point, Point is a class

class Point:
        def __init__(self):#this is how we define what this class has to do 
        #The double underscore is called "dunders", which is the double underscores on both sides of the name
            x = 0 #do not write it this way!!!
            y = 0
            color = "" #the issue is that remember with functions those variables are going to be deleted in memory, we want this to stick which is why the (self) comes around
            #self is the instance being cread - think of it as the blueprint
            self.x = 0 #This is the correct for this to stick arround so the dot operator accesses instance variables of the object
            self.y = 0
            self.color ""
        # adding self.var ties the scope of the variable
p1.x = 10 #now you can access that specific variable
    #Results you now get is the state of p1(x= 10, y=0, color = "")
p2.x = 5
    #Results you now state of p2(x= 5, y=0, color = "")

p1.color = "red"
    ##Results you now get is the state of p1(x= 10, y=0, color = red)

#Technically this is an alternative to dictionaryr, but the difference is we can't bundle the behavior