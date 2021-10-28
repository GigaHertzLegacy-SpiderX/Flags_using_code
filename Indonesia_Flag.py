from turtle import *

wn = Screen()

penup()
goto(-100,100)
pendown()

color("red")
begin_fill()
for count in range(2):
  forward(200)
  right(90)
  forward(50)
  right(90)
end_fill()

penup()
forward(200)
right(90)
forward(50)

begin_fill()
color("white")
for count in range(2):
  forward(50)
  right(90)
  forward(200)
  right(90)
end_fill()

color("black")
penup()
goto(0,125)
write("Flag of Indonesia",align="center", font=("Arial", 15, "normal"))
hideturtle()
