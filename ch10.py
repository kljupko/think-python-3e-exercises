# EXERCISE 1
# Ask a chatbot to answer some questions.
# -----------





# EXERCISE 2
# Use "get" to write a version of "value_counts" and eliminate the "if" statement.
# -----------

def value_counts(string):
    string = string.lower()
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, string.count(letter))
    return counter

print(value_counts('brontosaurus'))





# EXERCISE 3
# See if there is a word longer than "unpredictably" that has no repeating letters.
# Write a "has_duplicates" function that returns True if the sequence in the argument has any duplicate elements.
# -----------

def has_duplicates(sequence):
    counter = value_counts(sequence)
    for value in counter.values():
        if value > 1:
            return True
    return False

word_dict = {}
reader = open("resources/words.txt")
for word in reader:
    word_dict[word.strip().lower()] = 1
reader.close()

target_length = len("unpredictably")
for word in word_dict:
    if len(word) > target_length and not has_duplicates(word):
        print(word)





# EXERCISE 4
# Write a "find_repeats" function that takes a dictionary like the one from "value_counts" and returns a list of the keys of repeat values.
# ----------

def find_repeats(dictionary):
    repeats = []
    for key, value in dictionary.items():
        if value > 1:
            repeats.append(key)
    return repeats

print(find_repeats(value_counts("banana")))





# EXERCISE 5
# Write an "add_dictionaries" function that takes two dictionaries like from "value_counts" and adds them up.
# -----------

def add_dictionaries(d1, d2):
    added = dict(d1)
    for key, value in d2.items():
        if key not in added:
            added[key] = value
        else:
            added[key] += value
    return added

counter1 = value_counts("brontosaurus")
counter2 = value_counts("apatosaurus")

print(add_dictionaries(counter1, counter2))

# The chatbot also recommends using collections.Counter or defaultdict
# but we haven't covererd those yet.





# EXERCISE 6
# Write an "is_interlocking" function that takes a word as an argument and returns True if it can be split into two interlocking words.
# -----------

def is_interlocking(word):
    word = word.lower()
    w1 = word[0::2]
    w2 = word[1::2]

    word_dict = {}
    reader = open("resources/words.txt")
    for line in reader:
        word_dict[line.strip().lower()] = 1
    reader.close()

    return w1 in word_dict and w2 in word_dict

print(is_interlocking("schooled"))
