from turtle import *

wn = Screen()
wn.setup(width=800, height=600)
wn.title("Indonesia")

penup()
goto(-700, 330)
pendown()

speed(0)

color("red")
begin_fill()
for count in range(8):
  forward(1800)
  right(90)
  forward(350)
  right(90)
end_fill()

hideturtle()
done()
