# EXERCISE 1
# Ask a chatbot.
# -----------

# 1. The chatbot can spot the errors and fix the functions. Not relevant here.



# 2. Have a chatbot write a function that takes coordinates of two points and computes the distance between them.
# See if the result resembles the one from the chapter.

import math

def distance_between_points(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).

    Parameters:
        x1, y1: Coordinates of the first point
        x2, y2: Coordinates of the second point

    Returns:
        float: Distance between the two points
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Example usage:
d = distance_between_points(1, 2, 4, 6)
print(f"Distance: {d}")

# Conclusion: it works the same, but this function does all the calculations in the return statement instead of breaking the procedure into multiple lines.





# EXERCISE 2
# Write a boolean function "is_between(x, y, z)" that returns True if x<y<z or z<y<x, and False otherwise
# -----------

def is_between(x, y, z):
    return x < y < z or z < y < x

print(is_between(1, 2, 3))
print(is_between(6, 3, 1))
print(is_between(4, 1, 17))





# EXERCISE 3
# Write an Ackermann function. What happens if you call ackermann(5, 5)?
# -----------

def ackermann(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

print(ackermann(2, 3))
#print(ackermann(5, 5)) # calling this function causes a recursion error because the call stack is too large.





# EXERCISE 4
# Write a recursive function that finds the greatest common divisor of two given numbers.
# ----------

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

print(gcd(3, 4))
print(gcd(4, 0))
print(gcd(12, 18))
