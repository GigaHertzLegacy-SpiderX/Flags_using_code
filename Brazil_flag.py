import turtle
import math

# Screen
wn = turtle.Screen()
wn.setup(width=900, height=600)
wn.title("Brazil")
wn.bgcolor("Green")

# yellow losange
turtle.penup()
turtle.goto(0, -270)
turtle.pendown()
turtle.color("Yellow")
turtle.begin_fill()
turtle.goto(-420, 0)
turtle.goto(0, 270)
turtle.goto(420, 0)
turtle.goto(0, -270)
turtle.end_fill()

radius = 175
# blue circle
turtle.penup()
turtle.goto(0, radius)
turtle.pendown()
turtle.begin_fill()
turtle.color("Blue")
turtle.circle(-radius)
turtle.end_fill()
turtle.penup()

# white arc
turtle.goto(radius, -20)
turtle.setheading(120)
turtle.forward(1)
turtle.pendown()
turtle.setheading(120)
turtle.color("White")
turtle.pensize(10)
turtle.circle(radius + 40, 110)

turtle.done()