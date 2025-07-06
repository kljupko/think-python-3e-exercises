# EXERCISE 1
# Write a function print_right that takes a string as an argument and prints it with enough leading spaces so that the last character in the word is the 40th character.
# ----------

def print_right(text):
    lead = 40 - len(text)
    print(" " * lead + text)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")



# EXERCISE 2
# Write a function that takes a string and an integer, and prints out a triangle of the given height made out of copies of the string.
# ----------

def triangle(string, height):
    for i in range(height):
        print(string * (i + 1))

triangle("L", 5)



# EXERCISE 3
# Write a function which prints the "99 Bottles of Beer" song.
# -----------

def print_line(n):
    print(n, "bottles of beer on the wall")

def bottle_verse(n):
    print_line(n)
    print(n, "bottles of beer")
    print("Take one down, pass it around")
    print_line(n-1)

for n in range(99, 0, -1):
    bottle_verse(n)
    print()

