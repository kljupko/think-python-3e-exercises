# EXERCISE 1
# Consider asking a chatbot for help in the next exercises. Noted.
# -----------





# EXERCISE 2
# Create a dictionary that uses a mutable tuple as a key. Confirm that it results in a TypeError.
# Ask a chatbot why you can't do that.
# -----------

list0 = [1, 2, 3]
list1 = [4, 5]
t = (list0, list1)
print(t)
t[1].append(6)
print(t)

#d = {t: "the key is a tuple containing lists, which are mutable"}   # this results in a TypeError

# ChatGPT correctly notes, with examples, that hashability depends on the contents of the tuple.
# If the tuple, while itself immutable, contains mutable types like a list, it is no longer hashable.





# EXERCISE 3
# Write a "shift_word" function that takes a string and an integer, and shifts the word by the given number of places.
# -----------

def shift_word(word, n):
    word = word.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = range(len(letters))
    letter_map = dict(zip(letters, numbers))

    new = ""
    for letter in word:
        shift = (n + letter_map[letter]) % len(letters)
        new += letters[shift]

    return new

print(shift_word("cheer", 7))
print(shift_word("melon", 16))





# EXERCISE 4
# Write a "most_ferquent_letters" function that takes a string and prints the letters in decreasing order of frequency.
# -----------

def value_counts(string):
    d = {}
    for letter in string:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    
    return d

def second_element(t):
    return t[1]

def most_frequent_letters(string):
    frequencies = value_counts(string.lower())

    items = sorted(frequencies.items(), key = second_element, reverse = True)
    for item in items:
        print(item[0])

most_frequent_letters('banana')





# EXERCISE 5
# Write a function that takes a list of words and prints all the sets of words that are anagrams.
# -----------

def get_anagrams(words):
    d = {}

    for word in words:
        word = word.lower()
        srt = "".join(sorted(word))
        if srt in d:
            d[srt].append(word)
        else:
            d[srt] = [word]

    return d

words = "retainers generating slated smelters deltas salted staled resmelts greatening termless ternaries desalt lasted"
word_list = words.split()

for value in get_anagrams(word_list).values():
    print(value)





# EXERCISE 6
# Write a "word_distance" function that takes two words of the same length and returns the number of places where they differ.
# ------------

def word_distance(word1, word2):
    if len(word1) != len(word2):
        return None

    count = 0

    for letter1, letter2 in zip(word1.lower(), word2.lower()):
        if letter1 != letter2:
            count += 1

    return count

print(word_distance("test", "testing"))
print(word_distance("cat", "hat"))
print(word_distance("anchor", "harbor"))





# EXERCISE 7
# Write a program that gets all the metathesis pairs from the word list.
# ------------

def is_metathesis_pair(word1, word2):
    word1, word2 = word1.lower(), word2.lower()

    if word_distance(word1, word2) != 2:
        return False

    if sorted(word1) != sorted(word2):
        return False

    return True

# using anagrams from exercise 5
anagrams_list = get_anagrams(word_list).values()

for anagrams in anagrams_list:
    for i in range(len(anagrams) - 1):
        for j in range(i+1, len(anagrams)):
            w1 = anagrams[i]
            w2 = anagrams[j]
            if is_metathesis_pair(w1, w2):
                print(w1, "-", w2)










# BONUS
# ------

print()
print("BONUS: TESTING ON ALL WORDS")

word_list = []

reader = open("resources/words.txt")
for word in reader:
    word_list.append(word.strip().lower())
reader.close()

meta_pairs = []

anagrams_list = get_anagrams(word_list).values()
for anagrams in anagrams_list:
    for i in range(len(anagrams) - 1):
        for j in range(i+1, len(anagrams)):
            w1 = anagrams[i]
            w2 = anagrams[j]
            if is_metathesis_pair(w1, w2):
                pair = w1 + "-" + w2
                meta_pairs.append(pair)

print("Metathesis pairs in the words.txt file:", len(meta_pairs))
