# The files for these exercises are located in a "resources" folder in the same directory as the script.





# EXERCISE 1
# Ask a chatbot to write some code. Pass.
# -------------





# EXERCISE 2
# Write a function that does the same thing as the shell command "head".
# Arguments: file name to read, number of lines to read, file name to write.
# If the third parameter is None, display the lines instead of writing.
# -------------

def head(read_file, n_lines, write_file):
    reader = open(read_file)
    lines = ""
    for _ in range(n_lines):
        lines += reader.readline()
    reader.close()
    
    if write_file:
        writer = open(write_file, 'w')
        writer.write(lines)
        writer.close()
    else:
        print(lines)

# writing to the "output" folder
head("resources/pg345_cleaned.txt", 100, "resources/pg345_output100.txt")
head("resources/pg345_cleaned.txt", 30, None)





# EXERCISE 3
# Write a function called "check_word" that takes a 5-letter word and checks if it is the solution to a Wordle puzzle if:
#   the letters E and R are in the word
#   the letter E is not the third or fifth letter
#   the word does not contain the letters S, P, A, D, C, L, K
# How many words could be the answer?
# ------------

def uses_all(word, required):
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def check_word(word):
    if len(word) != 5:
        return False

    word = word.lower()
    
    if not uses_all(word, "er"):
        return False

    if word[2] == "e" or word[4] == "e":
        return False
    
    if uses_any(word, "spadclk"):
        return False
    
    return True

reader = open("resources/words.txt")
counter = 0

for word in reader:
    word = word.strip()
    if check_word(word):
        counter += 1

reader.close()

print("Possible words:", counter)





# EXERCISE 4
# Same as above, but also ...
#   M is the fifth letter
#   T and O are also not used
# -----------

def check_word(word):
    if len(word) != 5:
        return False

    word = word.lower()

    if not uses_all(word, "erm"):
        return False

    if word[2] == "e" or word[4] != "m":
        return False

    if uses_any(word, "spadclkto"):
        return False

    return True

reader = open("resources/words.txt")
counter = 0

for word in reader:
    word = word.strip()
    if check_word(word):
        counter += 1

reader.close()

print("Possible words:", counter)





# EXERCISE 5
# Count the number of times the words are used: pale, pales, paled, paleness, pallor.
# Avoid other words like "impale".
# Use a regular expression. Have a chatbot help you.
# -----------

import re

def count_words(pattern):
    count = 0
    reader = open("resources/pg1184_cleaned.txt")
    for line in reader:
        line = line.strip().lower()
        result = re.search(pattern, line)
        if result != None:
            count += 1
    reader.close()
    return count

pattern = re.compile(r'\b(?:pale(?:s|d|ness)?|pallor)\b', re.IGNORECASE) # provided by ChatGPT 4o

count = count_words(pattern)
print("Times the words are used:", count)
