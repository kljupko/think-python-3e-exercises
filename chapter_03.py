# EXERCISE 1
# Ask a chatbot to write some functions.
# -----------

# 1. The repeat function.

def repeat(text, times):
    for _ in range(times):
        print(text)



# 2. Without a for loop.

def repeat(text, times):
    print((text + '\n') * times, end='')



# 3. "Write a Python function that takes two strings as arguments, concatenates them, and prints them twice."

def print_concatenated_twice(str1: str, str2: str):
    """
    Concatenates two strings and prints the result twice.
    
    Parameters:
    - str1 (str): The first string.
    - str2 (str): The second string.
    """
    result = str1 + str2
    print(result)
    print(result)



# 4. The chatbot recognises the issue that "cat" is not provided in the header.





# EXERCISE 2
# Write a function print_right that takes a string as an argument and prints it with enough leading spaces so that the last character in the word is the 40th character.
# ----------

def print_right(text):
    lead = 40 - len(text)
    print(" " * lead + text)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")





# EXERCISE 3
# Write a function that takes a string and an integer, and prints out a triangle of the given height made out of copies of the string.
# ----------

def triangle(string, height):
    for i in range(height):
        print(string * (i + 1))

triangle("L", 5)





# EXERCISE 4
# Write a function that takes a string and two ingegers and draws a rectangle of a given width and height wiht the string.
# ----------

def rectangle(string, width, height):
    for i in range(height):
        print(string * width)

rectangle("H", 5, 4)





# EXERCISE 5
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

