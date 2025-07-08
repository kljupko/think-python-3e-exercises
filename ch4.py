# The exercises in this file use the turtle module instead of jupyturtle

from turtle import forward, left, right, penup, pendown, clear, home, done, speed
import math
# required functions from the chapter

def polyline(n, length, angle):
	for i in range(n):
		forward(length)
		left(angle)

def polygon(n, length):
	angle = 360 / n
	polyline(n, length, angle)

def arc(radius, angle):
	arc_length = 2 * math.pi *radius * angle / 360
	n = 30
	length = arc_length / n
	step_angle = angle / n
	polyline(n, length, step_angle)

def circle(radius):
	arc(radius, 360)

def jump(length):
    """Move forward length units without leaving a trail.

    Postcondition: leaves the pen down
    """
    penup()
    forward(length)
    pendown()





# EXERCISE 1
# Write a function called "rectangle" that draws a rectangle with the given side lengths.
# ----------

def rectangle(width, height):
    """Draws a rectangle with the given width and height.
    """
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

rectangle(80, 40)





# EXERCISE 2
# Write a function called "rhombus" that draws a rhombus with a given side length and interior angle.
# ----------

# cleanup from previous exercise
clear()
penup()
home()
pendown()

def rhombus(length, angle):
    """Draws a rhombus with a given side length and interior angle.
    """
    for _ in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(180 - angle)

rhombus(50, 60)





# EXERCISE 3
# Write a more general "parallelogram" function that draws a quadrilateral with parallel sides.
# Then rewrite "rectangle" and "rhombus" to use "parallelogram".
# ----------

# cleanup
clear()
penup()
home()
pendown()

def parallelogram(width, height, angle):
    """Draws a quadrilateral parallelogram with the given side lengths and interior angle.
    """
    for _ in range(2):
        forward(width)
        left(angle)
        forward(height)
        left(180 - angle)

def rectangle(width, height):
    parallelogram(width, height, 90)

def rhombus(length, angle):
    parallelogram(length, length, angle)

rectangle(80, 40)
jump(100)
rhombus(50, 60)
jump(80)
parallelogram(80, 50, 60)





# EXERCISE 4
# Write a function called "triangle" which draws a triangle, then write a function called "draw_pie" that draws a pie made up of triangles.
# ----------

#cleanup
clear()
penup()
home()
pendown()

def triangle(base, sides):
    """Draws an isosceles triangle based on the parameters

    base: length of the base
    sides: length of the two identical sides
    """
    angle_A = 180 - math.degrees(math.acos(base / (2 * sides)))

    forward(base)
    left(angle_A)
    forward(sides)
    left(angle_A * 2 * -1)
    forward(sides)
    left(angle_A)

def draw_pie(radius, pieces):
    """Draws a pie made of triangles

    radius: the radius of the pie
    pieces: the number of pieces of the pie
    """
    base = 2 * radius * math.sin(math.pi / pieces)
    piece_angle = 360 / pieces
    for _ in range(pieces):
        triangle(base, radius)
        penup()
        forward(base)
        pendown()
        left(piece_angle)

draw_pie(50, 5)
jump(120)
draw_pie(50, 6)
jump(120)
draw_pie(50, 7)





# EXERCISE 5
# Do the same for petals and a flower.
# ----------

#cleanup
clear()
penup()
home()
pendown()

def petal(length, width):
  arc(length, width)
  left(180 - width)
  arc(length, width)
  left(180 - width)

def draw_flower(size, width, npetals):
  petal_angle = 360 / npetals
  for _ in range(npetals):
    petal(size, width)
    left(petal_angle)

draw_flower(60, 60, 6)
jump(120)
draw_flower(40, 90, 9)





# EXERCISE 6
# Use a chatbot to write a function that draws a spiral.
# ----------

#cleanup
clear()
penup()
home()
pendown()

def draw_spiral(length=100, angle=30, step=5):
    """
    Draws a spiral using turtle graphics.

    Parameters:
    - length: how far the spiral extends outward
    - angle: how much to turn at each step (degrees)
    - step: how much to increase line length per turn
    """
    speed(0)      # Fastest drawing speed
    dist = 0             # Initial forward distance

    while dist < length:
        forward(dist)
        left(angle)
        dist += step

draw_spiral(length=300, angle=30, step=5)
done()
