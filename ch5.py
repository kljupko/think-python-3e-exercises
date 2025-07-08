# EXERCISE 1
# The exercise requires the following

from time import time
now = time()

# The function returns the number of seconds since January 1, 1970, 00:00:00 UTC
# Use floor division and modulus to calculate the number of days since then, and the current time of day in hours, minutes, and seconds.
# ----------

seconds = int(now)
days = seconds // 60 // 60 // 24    # current seconds divided by number of seconds in a minute, minutes in an hour, and hours in a day
second = seconds % 60
minute = seconds // 60 % 60
hour = seconds // (60 * 60) % 24

print("Days:", days, "\nTime is", hour, ":", minute, ":", second)



# EXERCISE 2
# Write a function named "is_triangle" that takes 3 integers as arguments
# and prints either "Yes" or "No" depending on if it is possible to form a triangle with sticks of the given lengths
# ----------

def is_triangle(a, b, c):
    if (a > b+c or b > a+c or c > a+b):
        print("No")
    else:
        print("Yes")

is_triangle(12, 1, 1)
is_triangle(4, 5, 6)



# EXERCISE 3
# Draw the stack diagram of the following program:

def recurse(n, s):
    if (n == 0):
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
# ------------

# recurse   n --> 3
#           s --> 0
#
# recurse   n --> 2
#           s --> 3
#
# recurse   n --> 1
#           s --> 5
#
# recurse   n --> 0
#           s --> 6



# EXERCISE 4
# Guess what the function below does

from turtle import forward, left, right, back, clear, penup, pendown, home

def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)

draw(100)
# -----------
# My guess: draws a branching shape recursively as long as the length of a branch is greater than 5
#           starts with the leftmost branches and moves to the right
#
# What it does: as I guessed, though I didn't mention how the factor impacts the execution



# EXERCISE 5
# Write a function to draw a Koch curve
# -----------

# cleanup
clear()
penup()
home()
pendown()

def koch(x):
    if x < 5:
        forward(x)
    else:
        koch(x / 3)
        left(60)
        koch(x / 3)
        right(120)
        koch(x / 3)
        left(60)
        koch(x / 3)

koch(120)



# EXERCISE 6
# Use a chatbot to create a function that draws a Sierpinski triangle.
# ----------

# cleanup
clear()
penup()
home()
pendown()

from turtle import *

def sierpinski(length, depth):
    def triangle(l, d):
        if d == 0:
            for _ in range(3):
                forward(l)
                left(120)
        else:
            triangle(l / 2, d - 1)
            forward(l / 2)
            triangle(l / 2, d - 1)
            back(l / 2)
            left(60)
            forward(l / 2)
            right(60)
            triangle(l / 2, d - 1)
            left(60)
            back(l / 2)
            right(60)

    # Setup
    speed(0)
    penup()
    goto(-length / 2, -length / 2**0.5)
    pendown()
    triangle(length, depth)
    done()

sierpinski(400, 4)

