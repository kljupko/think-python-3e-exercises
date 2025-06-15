# Exercise 1
# What does the round function do if a number ends in 0.5?
# ----------
# No code.
# The round function rounds to the nearest even integer when the number ends in 0.5.



# Exercise 2
# Run the following expressions to see what happens.
# ----------
# 1.
-2      # output: -2
+2      # output: 2
2++2    # output: 4

# 2.
4 2     # output: SyntaxError: invalid syntax

# 3.
round(42.5  # output: SyntaxError: '(' was never closed     /cannot run in terminal environment: keeps breaking into new line
round42.5)  # output: SyntaxError: unmatched ')'
round42.5   # output: SyntaxError: invalid syntax



# Exercise 3
# Guess what type the values below are.
# ----------
type(765)       # guess: int        type: int
type(2.718)     # guess: float      type: float
type('2 pi')    # guess: str        type: str
type(abs(-7))   # guess: int        type: int
type(abs(-7.0)) # guess: float      type: float
type(abs)       # guess: function   type: built-in function or method
type(int)       # guess: type       type: type
type(type)      # guess: function   type: type



# Exercise 4
# Practice arithmetic expressions with the questions below.
# ----------
# done without using variables
# 1. How many seconds are there in 42 minutes 42 seconds?
42 * 60 + 42    # output: 2562

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
10 / 1.61       # output: 6.211180124223602

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
# 42 minutes and 42 seconds is 2562 seconds
# 10 km is 6.2 miles
# so what is the pace in seconds per mile?
2562 / 6.211180124223602    # output: 412.482
# roughly 412.5 seconds per mile

# 4. What is your average pace in minutes and seconds per mile?
412.482 // 60       # output: 6.0
412.482 % 60        # output: 52.48200000000003
# roughly 6 minutes and 52.5 seconds per mile

# 5. What is your average speed in miles per hour?
# 6.2 miles in 2562 seconds is 6.2 miles in...
2562 / (60 * 60)    # output: 0.7116666666666667
# roughly 0.7 hours
# meaning the speed is...
6.211180124223602 / 0.7116666666666667  # output: 8.727653570337614
# roughly 8.73 miles per hour

