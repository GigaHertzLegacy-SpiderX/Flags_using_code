import turtle

# Screen
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Flamengo")
turtle.speed(0)


def make_strip(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(75)
    turtle.setheading(0)
    turtle.forward(800)
    turtle.setheading(270)
    turtle.forward(75)
    turtle.setheading(180)
    turtle.forward(800)
    turtle.end_fill()


def make_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(size)
    turtle.setheading(0)
    turtle.forward(size)
    turtle.setheading(270)
    turtle.forward(size)
    turtle.setheading(180)
    turtle.forward(size)
    turtle.end_fill()


for i in range(8):
    if i % 2 == 0:
        make_strip(-400, -300 + i * 75, "Red")
    else:
        make_strip(-400, -300 + i * 75, "Black")

make_square(-400, 75, 225, "Black")
make_square(-396, 79, 218, "Red")

#TODO: better "CRF" Lettering
aux_x = -300  # to center the lettering
aux_y = 260  # to center the lettering
font_height = 150
font_width = 70

turtle.goto(aux_x, aux_y)
turtle.color("White")
turtle.pensize(10)
turtle.penup()

# Drawing C
turtle.pendown()
turtle.setheading(180)
turtle.fd(font_width)
turtle.setheading(270)
turtle.fd(font_height)
turtle.setheading(0)
turtle.fd(font_width)

# Drawing R
turtle.penup()
turtle.goto(aux_x - 20, aux_y - font_height - 10)
turtle.pendown()
turtle.setheading(90)
turtle.fd(font_height + 30)
turtle.setheading(0)
turtle.fd(font_width)
turtle.setheading(270)
turtle.fd((font_height + 30) / 2)
turtle.setheading(180)
turtle.fd(font_width)
turtle.setheading(315)
turtle.fd(1.414 * font_width + 10)

# Drawing F
turtle.penup()
turtle.goto(aux_x + 2 * font_width - 40, aux_y)
turtle.pendown()
turtle.setheading(180)
turtle.fd(font_width)
turtle.setheading(270)
turtle.fd(font_height)
turtle.penup()
turtle.goto(aux_x + 2 * font_width - 40, aux_y - font_height / 2 + 20)
turtle.pendown()
turtle.setheading(180)
turtle.fd(font_width)


turtle.done()
