import turtle
import math
import time

#===================Screen=====================================
screen = turtle.Screen()
screen.title('Bresenham Line Drawing Algorithm')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

#===================Pen========================================
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

#===================Draw Axes==================================
def draw_axes():
    t.pensize(1)
    t.pencolor('gray')
    # X-axis
    t.penup()
    t.goto(0, 400)
    t.pendown()
    t.goto(1000, 400)
    screen.update()
    # Y-axis
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.goto(500, 800)
    screen.update()

#===================Bresenham's Algorithm======================
def bresenham(x1, y1, x2, y2, color):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    t.penup()
    t.goto(x1, y1)
    t.dot(5, color)
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx
    for i in range(0, dx):
        if p < 0:
            x1 += 1
            p += 2 * dy
        else:
            x1 += 1
            y1 += 1
            p += 2 * dy - 2 * dx
        t.goto(x1, y1)
        t.dot(5, color)
    screen.update()
#===================Main Part==================================
draw_axes()
time.sleep(1.0)

x1, y1 = 400, 300
x2, y2 = 600, 500
bresenham(x1, y1, x2, y2, 'Red')

#===================Keep the Screen Open=======================
screen.exitonclick()
