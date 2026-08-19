import turtle
import math
import time

#====================Screen========================
screen = turtle.Screen()
screen.title('DDA Line Drawing Algorithm')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

#====================Pen===========================
t = turtle.Turtle()
# t.speed(0)
t.penup()
t.hideturtle()

#====================Draw Axes=====================
def draw_axes():
    t.pensize(1)
    t.pencolor('gray')

    # X-axis
    t.penup()
    t.goto(0, 400)
    t.pendown()
    t.goto(1000, 400)

    # Y-axis
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.goto(500, 800)

    screen.update()

#====================DDA Algorithm=================
def dda(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    t.penup()
    t.goto(x1, y1)
    t.dot(5, color)
    for i in range(0, steps):
        x1 = x1 + x_inc
        y1 = y1 + y_inc
        t.goto(round(x1), round(y1))
        t.dot(5, color)

    screen.update()

#====================Main Part=====================
draw_axes()
time.sleep(1.0)

x1, y1 = 300, 300
x2, y2 = 600, 600
dda(x1, y1, x2, y2, 'Red')

#================Keep Screen Open==================
screen.exitonclick()
