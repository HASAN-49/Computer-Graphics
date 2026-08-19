import turtle
import time
import math

#=====================Screen====================
screen = turtle.Screen()
screen.title('Snowflake Koch Curve')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

#=====================Pen=======================
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

#=====================Koch======================
def koch(start, end, depth):
    if depth == 0:
        t.pendown()
        t.goto(end)
        screen.update()
        return

    dx = (end[0] - start[0]) / 3
    dy = (end[1] - start[1]) / 3
    p1 = (start[0] + dx, start[1] + dy)
    p3 = (start[0] + 2 * dx, start[1] + 2 * dy)
    theta = math.radians(-60)
    px = p1[0] + (p3[0] - p1[0]) * math.cos(theta) - (p3[1] - p1[1]) * math.sin(theta)
    py = p1[1] + (p3[0] - p1[0]) * math.sin(theta) + (p3[1] - p1[1]) * math.cos(theta)
    p2 = (px, py)

    koch(start, p1, depth - 1)
    koch(p1, p2, depth - 1)
    koch(p2, p3, depth - 1)
    koch(p3, end, depth - 1)

#====================Snowflake==================
def snowflake(triangle, depth, color):
    t.penup()
    t.goto(triangle[0])
    t.pensize(3)
    t.color(color)
    for i in range(len(triangle)):
        koch(triangle[i], triangle[(i + 1) % len(triangle)], depth)

#=====================Main Part=================
cx, cy = 500, 400    # Center
side = 300
height = math.sqrt(3) * side / 2
triangle = []
triangle.append((cx, cy + 2 * height / 3))
triangle.append((cx - side / 2, cy - height / 3))
triangle.append((cx + side / 2, cy - height / 3))
depth = 3
snowflake(triangle, depth, 'blue')

#=================Keep Screen Open==============
screen.exitonclick()