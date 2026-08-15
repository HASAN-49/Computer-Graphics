import turtle
import time
import math

#========================SCREEN SECTION========================
screen = turtle.Screen()
screen.title('2D Geometric Transformations')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

screen.tracer(0)

#=======================PEN SECTION========================
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

#=======================DRAW SHAPE========================
def draw_shape(points, color):
    t.pencolor(color)
    t.pensize(3)

    t.penup()
    t.goto(points[0])
    t.dot(5, color)

    t.pendown()
    for x, y in points[1:]:
        t.goto(x, y)
        t.dot(5, color)

    t.goto(points[0])
    t.penup()
    screen.update()

#=======================DRAW COORDINATE AXES========================
def draw_axes():
    t.pencolor('gray')
    t.pensize(1)

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

    t.penup()

    screen.update()

#=======================Translation========================
def translation(x, y, tx, ty):
    return x + tx, y + ty

#=======================Scaling========================
# x' = xf + (x - xf) * sx
# y' = yf + (y - yf) * sy
def scaling(x, y, sx, sy, xf, yf):
    x_new = xf + sx * (x - xf)
    y_new = yf + sy * (y - yf)
    return x_new, y_new

#=======================Rotation========================
# x' = xr + (x - xr) * cos(theta) - (y - yr) * sin(theta)
# y' = yr + (x - xr) * sin(theta) + (y - yr) * cos(theta)
def rotation(x, y, theta, xr, yr):
    x_new = xr + (x - xr) * math.cos(theta) - (y - yr) * math.sin(theta)
    y_new = yr + (x - xr) * math.sin(theta) + (y - yr) * math.cos(theta)
    return x_new, y_new

#======================Original Triangle========================
originial = [
    (-40, -40),
    (40, -40),
    (0, 60)
]

#======================Center the original triangle========================
base_x = 500
base_y = 400
triangle = []
for x, y in originial:
    triangle.append((x + base_x, y + base_y))

draw_axes()
draw_shape(originial, 'black')
time.sleep(1.5)
draw_shape(triangle, 'black')
time.sleep(1.5)

#======================Translation========================
tx, ty = 150, 100
translated = []
for x, y in triangle:
    translated.append(translation(x, y, tx, ty))

draw_shape(translated, 'green')
time.sleep(1.5)

#======================find center of translated triangle========================
cx = sum(x for x, y in translated) / len(translated)
cy = sum(y for x, y in translated) / len(translated)

#======================Scaling========================
sx, sy = 1.5, 1.5
scaled = []
for x, y in translated:
    scaled.append(scaling(x, y, sx, sy, cx, cy))

draw_shape(scaled, 'blue')
time.sleep(1.5)

#======================Rotation========================
theta = math.radians(90)
rotated = []
for x, y in scaled:
    rotated.append(rotation(x, y, theta, cx, cy))

draw_shape(rotated, 'red')
time.sleep(1.5)

#======================KEEP WINDOW OPEN=========================
screen.exitonclick()
