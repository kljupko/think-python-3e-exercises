from copy import copy
import math

# NOT using jupyturtle
import turtle

def jumpto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def moveto(x, y):
    turtle.goto(x, y)



# The exercises require the classes below.

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def translated(self, dx, dy):
        point = copy(self)
        point.translate(dx, dy)
        return point
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

class Line:
    """Represents a line in 2-D space."""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Line ({self.p1}, {self.p2})"

    def draw(self):
        jumpto(self.p1.x, self.p1.y)
        moveto(self.p2.x, self.p2.y)

    # added for exercise 2
    def __eq__(self, other):
        return (self.p1 == other.p1) and (self.p2 == other.p2)
        
    # added for exercise 3
    def midpoint(self):
        mx = (self.p1.x + self.p2.x) / 2
        my = (self.p1.y + self.p2.y) / 2
        return Point(mx, my)

class Rectangle:
    """Represents a rectangle.

    Attributes: width, height, top-left corner.
    """

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        return f"Rectangle: {self.width}x{self.height} @ {self.corner}"

    def make_points(self):
        p1 = self.corner
        p2 = p1.translated(self.width, 0)
        p3 = p2.translated(0, self.height)
        p4 = p3.translated(-self.width, 0)
        return p1, p2, p3, p4

    def make_lines(self):
        p1, p2, p3, p4 = self.make_points()
        return Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)

    def draw(self):
        lines = self.make_lines()
        for line in lines:
            line.draw()
    
    # added for exercise 4
    def midpoint(self):
        return self.corner.translated(self.width/2, self.height/2)
    
    # added for exercise 5
    def make_cross(self):
        line_top, line_right, line_bot, line_left = self.make_lines()
        mtop = line_top.midpoint()
        mright = line_right.midpoint()
        mbot = line_bot.midpoint()
        mleft = line_left.midpoint()
        
        print("printing midpoints t, r, b, l")
        print(mtop, mright, mbot, mleft, end="\n")
        print()
        
        return Line(mtop, mbot), Line(mleft, mright)





# EXERCISE 1
# Consider asking a chatbot for help. Noted.
# -----------





# EXERCISE 2
# Write an __eq__ method for Line.
# -----------

# added to the class above, tested here
p1 = Point()
p2 = Point(-150, -345)
line1 = Line(p1, p2)
line2 = copy(line1)

print(f"Line1: {line1}")
print(f"Line2: {line2}")
print(f"Lines one and two are equal: {line1 == line2}")
print()





# EXERCISE 3
# Write a "midpoint" method for Line that returns a Point in the middle of the line.
# -----------

# added to the class above, tested here
print(f"Line1 midpoint: {line1.midpoint()}")
print()
line1.draw()
jumpto(line1.midpoint().x, line1.midpoint().y)





# EXERCISE 4
# Write a "midpoint" for Rectangle that returns a Point in the center
# -----------

# added to the class above, tested here
rect = Rectangle(200, 100, Point(20, 20))
rect.draw()
print(f"Rectangle: {rect}")
print(f"Midpoint: {rect.midpoint()}")
print()
jumpto(rect.midpoint().x, rect.midpoint().y)





# EXERCISE 5
# Write a "make_cross" method for Rectangle that will use "make_lines" to get the lines, compute their midpoints.
# Then make and return a list of two lines using those midpoints to draw a cross.
# -----------

# added to the class above, tested here
cross_lines = rect.make_cross()
for line in cross_lines:
    print(f"Cross line: {line}")
    line.draw()





# EXERCISE 6
# Create a Circle class with attributes center (Point) and radius (number).
# Include methods __init__, __str__, and a draw method.
# -----------

class Circle:
    """Represents a circle."""
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def __str__(self):
        return f"Circle @ {self.center} with a radius of {self.radius}"
    
    def draw(self):
        n = 30
        angle = 360 / n
        length = 2 * math.pi * self.radius / n
        
        jumpto(self.center.x, self.center.y)
        turtle.penup()
        turtle.forward(self.radius)
        turtle.pendown()
        turtle.left(90)
        for i in range(n):
            turtle.forward(length)
            turtle.left(angle)

center = Point(150, -200)
radius = 50
circle = Circle(center, radius)
print()
print(circle)
circle.draw()

turtle.done()
