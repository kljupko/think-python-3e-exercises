# Testing the funcitons requires the following

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)





# EXERCISE 1
# Ask a chatbot to figure out what's wrong with this funciton.
def uses_any_incorrect(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT!
# ------------

# The chatbot correctly identifies the incorrect control flow, recognising that the loop completes after only one iteration.
# It offers the solution: remove the else statement and have the return False statement run only if the loop completes without finding a letter.





# EXERCISE 2
# Write a function namde "uses_none" that takes a word and a string of forbidden letters and returns True if the word uses none of them.
# Add at least one more doctest to the ones provided.
# -----------

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('peanut', 'BRI')
    True
    """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True

run_doctests(uses_none)





# EXERCISE 3
# Do the same for the "uses_only" function.
# ------------

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('cat', 'actually')
    True
    """
    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True

run_doctests(uses_only)





# EXERCISE 4
# Do the same for the "uses_all" function.
# -----------

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('bonobo', 'BONA')
    False
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

run_doctests(uses_all)





# EXERCISE 5
# Write some functions for the NYT Spelling Bee game.
# -----------

# 1. Write a function that checks if a word is acceptable.

def check_word(word, available, required):
    """Check whether a word is acceptable.
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4:
        return False
    if required.lower() not in word.lower():
        return False
    if not uses_only(word, available):
        return False
    return True

run_doctests(check_word)



# 2. Write a function to score the word. You can assume the word is acceptable.

def word_score(word, available):
    """Compute the score for an acceptable word.
    
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    if uses_all(word, available):
        return 15
    if len(word) > 4:
        return len(word)
    return 1

run_doctests(word_score)





# EXERCISE 6
# Write a version of the "uses_all" function that uses "uses_only".
# -----------

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('bonobo', 'BONA')
    False
    """
    return uses_only(required, word)

run_doctests(uses_all)





# EXERCISE 7
# Nah, the previous exercise was easy, no need to ask for help.





# EXERCISE 8
# Have a chatbot do exercise 6.
# ----------

# This is what ChatGPT 4o gave me on July 9, 2025.

def uses_all(word, required_letters):
    for letter in required_letters:
        if not uses_any(word, letter):
            return False
    return True

# It's essentially the same as the one from the book.
# ... mine's more elegant though :)
