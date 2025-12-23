import turtle

t = turtle.Turtle()
t.speed(3)

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

draw_polygon(3, 100)
t.penup()
t.forward(150)
t.pendown()

draw_polygon(4, 100)
t.penup()
t.forward(150)
t.pendown()

for _ in range(2):
    t.forward(120)
    t.left(90)
    t.forward(80)
    t.left(90)

t.penup()
t.forward(170)
t.pendown()

draw_polygon(6, 70)

turtle.done()
