from turtle import *

wn = Screen()
wn.title("Flag of France")

penup()
goto(-50, 50)
pendown()

color("blue")
begin_fill()
for count in range(2):
    forward(50)
    right(90)
    forward(100)
    right(90)
end_fill()

penup()
forward(100)
pendown()

begin_fill()
color("red")
for count in range(2):
    forward(50)
    right(90)
    forward(100)
    right(90)
end_fill()

back(100)
color("black")
for i in range(2):
    forward(150)
    right(90)
    forward(100)
    right(90)

penup()
goto(25, 70)
write("Flag of France", align="center", font=("Arial", 15, "normal"))
hideturtle()
done()
