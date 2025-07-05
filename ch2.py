# EXERCISE 1
# Volume of a sphere with a radius r is 4/3*pi*r**3. What is the volume of a sphere with radius 5?
# ----------

import math

radius = 5 # in cm
volume = 4/3 * math.pi * radius**3 # in cubic centimeters
print(volume)



# EXERCISE 2
# For a value of x, the result of (cos x)**2 + (sin x)**2 is 1. Check if it is true for 42.
# ----------

x = 42
result = math.cos(x)**2 + math.sin(x)**2
print(result)



# EXERCISE 3
# Compute e squared in these ways:
# ----------

print(math.e**2)
print(math.pow(math.e, 2))
print(math.exp(2))

