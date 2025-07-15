# The exercises require some data and functions, provided below.

import unicodedata
import random

filename = "resources/dr_jekyll.txt"

def split_line(line):
	return line.replace('—', ' ').split()

def clean_word(word):
	return word.strip(punctuation).lower()

punc_marks = {}
reader = open(filename)
for line in reader:
	for char in line:
		category = unicodedata.category(char)
		if category.startswith("P"):
			punc_marks[char] = 1
reader.close()
punctuation = ''.join(punc_marks)

def second_element(t):
    return t[1]

def print_most_common(word_counter, num=5):
    items = sorted(word_counter.items(), key = second_element, reverse = True)

    for word, freq in items[:num]:
        print(freq, word, sep="\t")





# EXERCISE 1
# Ask a chatbot.
# -----------

# Ask a chatbot to rewrite the "add_bigram" functin using "setdefault". Written by ChatGPT 4o on July 15, 2025.

def add_bigram(bigram):
    first, second = bigram
    successor_map.setdefault(first, []).append(second)



# Ask what the differences are between LLMs and Markov chain text analysis.

# ChatGPT states that the difference is that Markov chains have very short memory (1 - 3 words) and work on probabilities of word sequences.
# LLMs on the other hand, they have a much larger memory/ context window, are more coherent, and work on neural networks.





# EXERCISE 2
# Write a function that counts the number of times each trigram appears.
# ----------

trigram_counter = {}
window = []

def count_trigram(trigram):
    key = tuple(trigram)
    if key not in trigram_counter:
        trigram_counter[key] = 1
    else:
        trigram_counter[key] += 1

def process_word_trigram(word):
    window.append(word)

    if len(window) == 3:
        count_trigram(window)
        window.pop(0)

reader = open(filename)
for line in reader:
    for word in split_line(line):
        word = clean_word(word)
        process_word_trigram(word)
reader.close()

print_most_common(trigram_counter)





# EXERCISE 3
# Implement Markov chain text analysis for trigrams.
# -----------

successor_map = {}
window = []

def add_trigram(trigram):
    first, second, third = trigram

    key = first, second
    if key not in successor_map:
        successor_map[key] = [third]
    else:
        successor_map[key].append(third)

def process_word_trigram(word):
    window.append(word)

    if len(window) == 3:
        add_trigram(window)
        window.pop(0)

reader = open(filename)
for line in reader:
    for word in split_line(line):
        word = clean_word(word)
        process_word_trigram(word)
reader.close()





# EXERCISE 4
# Generate text using the trigrams.
# -----------

successors = list(successor_map)
bigram = random.choice(successors)

for _ in range(50):
    successors = successor_map[bigram]
    successor = random.choice(successors)
    print(successor, end = " ")
    bigram = bigram[1], successor



# BONUS
# Modify the last two exercises to use trigrams as keys.
# I generalized the functions to use n-grams.
# --------

successor_map = {}
window = []
ngram_length = 4
sentence_length = 50

def add_ngram(ngram):
    key = tuple(ngram[:-1])
    word = ngram[-1]

    if key not in successor_map:
        successor_map[key] = [word]
    else:
        successor_map[key].append(word)

def process_word_ngram(word, n):
    window.append(word)

    if len(window) == n:
        add_ngram(window)
        window.pop(0)

reader = open(filename)
for line in reader:
    for word in split_line(line):
        word = clean_word(word)
        process_word_ngram(word, ngram_length)
reader.close()



successors = list(successor_map)
ngram = random.choice(successors)
print("\n\nBONUS\n\n")

for _ in range(sentence_length):
    successors = successor_map[ngram]
    successor = random.choice(successors)
    print(successor, end = " ")

    new_ngram = []
    for i in range(1, len(ngram)):
        new_ngram.append(ngram[i])
    new_ngram.append(successor)
    ngram = tuple(new_ngram)
