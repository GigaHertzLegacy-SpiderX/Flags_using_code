import turtle

# Screen
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Brazil")
wn.bgcolor("Green")


# yellow losange
turtle.penup()
turtle.goto(-5, -180)
turtle.pendown()
turtle.color("Yellow")
turtle.begin_fill()
turtle.setheading(142)
turtle.forward(300)
turtle.setheading(40)
turtle.forward(300)

turtle.setheading(-40)
turtle.forward(300)
turtle.setheading(-141)
turtle.forward(297)
turtle.end_fill()

# blue circle
turtle.penup()
turtle.goto(42, -47)
turtle.pendown()
turtle.begin_fill()
turtle.color("Blue")
turtle.circle(-85)
turtle.end_fill()

# white arc
turtle.penup()
turtle.goto(64, -10)
turtle.setheading(120)
turtle.forward(1)
turtle.pendown()
turtle.setheading(120)
turtle.color("White")
turtle.pensize(10)
turtle.circle(110, 92)

turtle.done()