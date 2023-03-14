import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
sides = int(input("Please Type Your Desired Number of Sides:"))
length = int(input("Please Type Your Desired Length of Each Side:"))
internal_angle = 360/sides
for i in range (sides):
    my_turtle.forward(length)
    my_turtle.left(internal_angle)
print("Drawing Complete and", "Here is Your Internal Angle:", internal_angle)
window.exitonclick()