import turtle

# Screen
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Japan")
wn.bgcolor("White")

# Circle

turtle.pencolor("Red")
turtle.speed(0)

turtle.up()
turtle.setpos(-86, -160)
turtle.down()

turtle.fillcolor("Red")
turtle.begin_fill()
turtle.circle(160)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
