# EXERCISE 1
# Ask a chatbot. Not relevant here.
# -----------





# EXERCISE 2
# Test the expressions below to see what they do.
# -----------

#17 = n # can't assign to a number
x = y = 1
print(x, y) # both are 1
n = 17; # runs fine





# EXERCISE 3
# Practise using the interpreter aas a calculator.
# -----------



# 1. Volume of a sphere with a radius r is 4/3*pi*r**3. What is the volume of a sphere with radius 5?

import math

radius = 5 # in cm
volume = 4/3 * math.pi * radius**3 # in cubic centimeters
print(volume)



# 2. For a value of x, the result of (cos x)**2 + (sin x)**2 is 1. Check if it is true for 42.

x = 42
result = math.cos(x)**2 + math.sin(x)**2
print(result)



# 3. Compute e squared in these ways:

print(math.e**2)
print(math.pow(math.e, 2))
print(math.exp(2))
