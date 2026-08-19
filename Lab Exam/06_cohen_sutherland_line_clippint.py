import turtle
import math
import time

#=======================Screen=====================
screen = turtle.Screen()
screen.title('Cohen Sutherland Line Clipping Algorithm')
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

#=======================Pen========================
t = turtle.Turtle()
# t.speed(0)
t.penup()
t.hideturtle()

#=======================Draw Axes==================
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

#=======================Rectangle==================
def draw_rectangle(x_min, y_min, x_max, y_max, color):
    t.pensize(3)
    t.pencolor(color)

    t.penup()
    t.goto(x_min, y_min)

    t.pendown()
    t.goto(x_max, y_min)
    t.goto(x_max, y_max)
    t.goto(x_min, y_max)
    t.goto(x_min, y_min)

    screen.update()

#========================Line Draw=================
def draw_line(x1, y1, x2, y2, color):
    t.pensize(3)
    t.pencolor(color)

    t.penup()
    t.goto(x1, y1)

    t.pendown()
    t.goto(x2, y2)

    screen.update()

#======================Code Region=================
# code values
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

def code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE

    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT

    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP

    return code

#====================Cohen Sutherland==============
def cohen(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = code(x2, y2, x_min, y_min, x_max, y_max)
    print(code1, code2)

    while True:
        # completely inside
        if code1 == 0 and code2 == 0:
            return True, x1, y1, x2, y2

        # completely outside
        elif code1 & code2 != 0:
            return False, None, None, None, None

        # partially inside
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # top
            if code_out & TOP != 0:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            # bottom
            elif code_out & BOTTOM != 0:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            # right
            elif code_out & RIGHT != 0:
                x = x_max
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            # left
            else:
                x = x_min
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)

            # Update code 
            if code_out == code1:
                x1, y1 = x, y
                code1 = code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                code2 = code(x2, y2, x_min, y_min, x_max, y_max)

#=======================Main Part==================
draw_axes()

# Clipping Window
x_min, y_min = 300, 250
x_max, y_max = 700, 550
draw_rectangle(x_min, y_min, x_max, y_max, 'blue')

# Original Line
x1, y1 = 150, 150
x2, y2 = 850, 650
draw_line(x1, y1, x2, y2, 'gray')

# Perform Cohen Sutherland
accepted, cx1, cy1, cx2, cy2 = cohen(x1, y1, x2, y2, x_min, y_min, x_max, y_max)

if accepted == True:
    draw_line(cx1, cy1, cx2, cy2, 'red')
    print('Line Accepted')
    print('Clipped Line:')
    print('Start: ', cx1, cy1)
    print('End: ', cx2, cy2)
else:
    print('Line Rejected')

#====================Keep Screen Open==============
screen.exitonclick()
