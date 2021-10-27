from turtle import *

setup(800, 500)
speed(0)

x = -400
y = 250


def stripe():
    color("firebrick")
    begin_fill()
    for i in range(2):
        forward(800)
        right(90)
        forward(38)
        right(90)
    end_fill()


for i in range(7):
    penup()
    goto(x, y)
    pendown()
    stripe()
    y = y - 76

penup()
goto(-400, 250)
pendown()
color("navy")
begin_fill()

for i in range(2):
    forward(350)
    right(90)
    forward(266)
    right(90)
end_fill()


def star():
    color("white")
    begin_fill()
    for i in range(5):
        forward(20)
        right(144)
    end_fill()


x1 = -380
y1 = 230

x2 = -350
y2 = 205


def even_row():
    global x1
    global y1
    for i in range(6):
        penup()
        goto(x1, y1)
        pendown()
        star()
        x1 = x1 + 57


for i in range(5):
    even_row()
    x1 = -380
    y1 = y1 - 52


def odd_row():
    global x2
    global y2
    for i in range(5):
        penup()
        goto(x2, y2)
        pendown()
        star()
        x2 = x2 + 57


for i in range(4):
    odd_row()
    x2 = -350
    y2 = y2 - 51

hideturtle()
done()
