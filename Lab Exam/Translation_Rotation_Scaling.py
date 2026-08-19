import turtle
import math
import time

#==================Screen=======================
screen = turtle.Screen()
screen.title('2D Geometric Transformation')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

#==================Pen==========================
t = turtle.Turtle()
# t.speed(0)
t.penup()
# t.hideturtle()

#=================Draw Axes=====================
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

#=================Draw Shape====================
def draw_shape(points, color):
    t.pensize(3)
    t.pencolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for x, y in points[1:]:
        t.goto(x, y)
    t.goto(points[0])
    screen.update()

#=================Center the Triangle===========
def center_triangle(points):
    base_x = 500
    base_y = 400
    triangle = []
    for x, y in points:
        triangle.append((x + base_x - 55, y + base_y - 25))
    return triangle

#=================Translation===================
def translate(points, tx, ty):
    translated = []
    for x, y in points:
        translated.append((x + tx, y + ty))
    return translated

#=================Rotation======================
def rotation(points, theta, xr, yr):
    rotated = []
    for x, y in points:
        new_x = xr + (x - xr) * math.cos(theta) - (y - yr) * math.sin(theta)
        new_y = yr + (x - xr) * math.sin(theta) + (y - yr) * math.cos(theta)
        rotated.append((new_x, new_y))
    return rotated

#=================Scaling=======================
def scaling(points, sx, sy, xf, yf):
    scaled = []
    for x, y in points:
        new_x = xf + (x - xf) * sx
        new_y = yf + (y - yf) * sy
        scaled.append((new_x, new_y))
    return scaled

#=================Main Part=====================
draw_axes()
original_triangle = [(5, 5), (105, 5), (55, 55)]
draw_shape(original_triangle, 'Black')

triangle = center_triangle(original_triangle)
draw_shape(triangle, 'Black')

translated = translate(triangle, tx=100, ty=100)
draw_shape(translated, 'Green')

cx, cy, cnt = 0, 0, 0
for x, y in translated:
    cx += x
    cy += y
    cnt += 1
cx /= cnt
cy /= cnt
theta = math.radians(90)

rotated = rotation(translated, theta=theta, xr=cx, yr=cy)
draw_shape(rotated, 'Blue')

sx, sy = 1.5, 1.5
scaled = scaling(rotated, sx=sx, sy=sy, xf=cx, yf=cy)
draw_shape(scaled, 'Red')

#=================Keep Screen Open==============
screen.exitonclick()
