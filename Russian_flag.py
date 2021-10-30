import turtle
from turtle import *

wn = turtle.Screen()
wn.setup(width=500, height=500)
wn.title("Flag of Russia")
speed(0)

penup()
goto(-300, 100)
pendown()

# BLue

color("blue")
begin_fill()
forward(600)
right(90)
forward(150)
right(90)
forward(600)
forward(90)
right(90)
forward(150)
right(90)
forward(100)
end_fill()
penup()
left(90)

# Red
color("Red")

goto(-390, -50)
pendown()

begin_fill()
right(180)
forward(150)
left(90)
forward(690)
left(90)
forward(150)
left(90)
forward(690)
end_fill()

hideturtle()
done()
