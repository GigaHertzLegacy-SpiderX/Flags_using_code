import turtle
from turtle import *

#Screen
wn = turtle.Screen()
wn.setup(width=1000, height=890)
wn.title("Bangladesh")
wn.bgcolor("Green")

#Circle
turtle.pencolor("Red")
turtle.speed(0)

turtle.up()
turtle.setpos(-86, -160)
turtle.down()

turtle.fillcolor("Red")
turtle.begin_fill()
turtle.circle(190)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
