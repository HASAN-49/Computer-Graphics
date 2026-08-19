import turtle
import math
import time

#=======================Screen=======================
screen = turtle.Screen()
screen.title('Deterministic Koch Curve')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

#=========================Pen========================
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

#=======================Koch=========================
def koch(start, end, depth = 3):
    # Base case
    if depth == 0:
        t.pendown()
        t.goto(end)
        screen.update()
        return

    # devide into 3 segments
    dx = (end[0] - start[0]) / 3
    dy = (end[1] - start[1]) / 3
    p1 = (start[0] + dx, start[1] + dy)
    p3 = (start[0] + 2 * dx, start[1] + 2 * dy)
    theta = math.radians(60)
    px = p1[0] + (p3[0] - p1[0]) * math.cos(theta) - (p3[1] - p1[1]) * math.sin(theta)
    py = p1[1] + (p3[0] - p1[0]) * math.sin(theta) + (p3[1] - p1[1]) * math.cos(theta)
    p2 = (px, py)

    # Call itself
    koch(start, p1, depth - 1)
    koch(p1, p2, depth - 1)
    koch(p2, p3, depth - 1)
    koch(p3, end, depth - 1)

#=======================Main Part====================
start = (200, 400)
end = (800, 400)
print(start, end)
depth = 3
t.penup()
t.goto(start)
t.pensize(3)
t.color('blue')
koch(start, end, depth)

#===================Keep Screen Open=================
screen.exitonclick()