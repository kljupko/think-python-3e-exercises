from collections import Counter, defaultdict

# EXERCISE 1
# Ask a chatbot. No code. Not relevant here.
# -----------





# EXERCISE 2
# Use a set to rewrite the "uses_none" function.
# -----------

def uses_none(word, forbidden):
    intersection = set(word.lower()) & set(forbidden.lower())
    if len(intersection) > 0:
        return False
    return True

print("Exercise 2")
print(uses_none("word", "apple"))





# EXERCISE 3
# Write a function that takes a string of letters and a word, and checks if the letters can spell the word.
# Take into account how many times each letter appears.
# -----------

def can_spell(letters, word):
    cl = Counter(letters.lower())
    cw = Counter(word.lower())

    for letter in cw:
        if cw[letter] > cl[letter]:
            return False
    return True

print("\nExercise 3")
print(can_spell("table", "beet"))





# EXERCISE 4
# Write a simplified version of the "partition" function using a defaultdict.
# -----------

# No.

# In order for the rest of the program to work correctly, the return value must be a list of 4 PokerHand instances (0-3).
# defaultdict can’t help here because it only creates entries when keys are accessed,
# so if a suit doesn't appear in self.cards, it won’t be included and you’d end up with fewer than four hands.

# Meaning the exercise is poorly thought out.
# Why use defaultdict when the return values are known ahead of time... defaultdict is useless here.





# EXERCISE 5
# Rewrite fibonacci to use a single return statement with two conditional expressions, one nested.
# ----------

def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n-1) + fibonacci(n-2)

print("\nExercise 5")
print(fibonacci(7))





# EXERCISE 6
# Rewrite the function for the binomial coefficient to use nested conditional expressions.
# Also use memos.
# -----------

memo = {}
def binomial_coeff(n, k):
    res = memo[(n, k)] if (n, k) in memo else 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    memo[(n, k)] = res
    return res

print("\nExercise 6")
print(binomial_coeff(10, 4))
print(memo)





# EXERCISE 7
# Write a more concise Deck.__str__ method using a list comprehension or generator expression.
# -----------

def __str__(self):
    return "\n".join(str(card) for card in self.cards)

# Can't test without the class.
