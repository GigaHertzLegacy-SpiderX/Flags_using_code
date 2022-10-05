import turtle as t
 
#chnage the speed of drawing
t.speed(5)
#stop writing
t.penup()
#change the pen position
t.goto(-500, 275)
#start writing
t.pendown()
#change the pen color 
t.color("black", "dark green")
t.begin_fill()
for n in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(550)
    t.right(90)
t.end_fill()
 
t.penup()
t.goto(150, 0)
 
t.penup()
t.backward(75)
t.left(90)
t.forward(125)
t.left(90)
t.pendown()
 
t.color("dark green", "white")
t.begin_fill()
#draw a circle with specified redius
t.circle(127.5)
t.end_fill()
 
t.penup()
t.goto(113, 127.5)
t.pendown()
 
t.color("dark green", "dark green")
t.begin_fill()
t.circle(107)
t.end_fill()
 
t.penup()
t.color("dark green", "white")
t.goto(225, 20)
t.right(20)
t.begin_fill()
for x in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
 
t.color("black", "white")
t.goto(-250, -275)
t.left(20)
t.pendown()
 
t.begin_fill()
for n in range(2):
    t.forward(250)
    t.right(90)
    t.forward(550)
    t.right(90)
t.end_fill()
 
t.penup()
t.goto(350, -255)
t.right(154)
t.color("white", "white")

t.hideturtle()
t.done()
