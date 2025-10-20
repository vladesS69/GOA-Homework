from turtle import *


#we want to paint a house 


#step 1: draw a square
speed(5)
width(5)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door
forward(70)
color("red")
left(90)
begin_fill()
forward(120)   #height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()






#make the sun
penup()
goto(-300,300)
pendown()
color("yellow")
begin_fill()
circle(50)
end_fill()

exitonclick()


#done




