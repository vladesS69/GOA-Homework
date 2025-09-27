from turtle import *
#we want to paint a car
color("red")

begin_fill()
for i in range(4):
    forward(200)
    right(90)
end_fill()

#we want to paint a window of the car 
color("blue")

begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()
#we want to paint a wheeel of the car
color("black")

begin_fill()
circle(20)
end_fill()
#move to the other wheel
#move the turtle without drawing a line 
#lift the pen up
penup()

forward(200)
pendown()