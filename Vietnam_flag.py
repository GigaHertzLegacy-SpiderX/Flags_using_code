import turtle
wn = turtle.Screen()            
wn.bgcolor("red")              
width = 750;            
height = 500;            
star = 80;         
 
wn.setup(width = width, height = height)
wn.title("Vietnam")
 
t = turtle.Turtle()
t.color("red")               
t.setx((width - star)/2 - width/2)
t.sety(star/4)
t.color("yellow")
t.shape("blank")             
t.pensize(3)                 

t.fillcolor("Yellow")
t.begin_fill()
# Draw the flag
for side in range(5):
    t.forward(star)
    t.right(144)
    t.forward(star)
    t.right(72 - 144)
t.end_fill()
turtle.hideturtle()
turtle.done()
