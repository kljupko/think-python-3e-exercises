# As before, the files required for the exercises are found in the "resoureces" folder.





# EXERCISE 1
# Understand that a chatbot cannot always be reliable. Understood.
# -----------





# EXERCISE 2
# Write a function called "is_anagram" that takes two strings and returnes True if they are anagrams.
# Find all anagrams of the word "takes".
# -----------

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

word_list = []
reader = open('resources/words.txt')
for word in reader:
    word_list.append(word.strip())
reader.close()

for word in word_list:
    if is_anagram(word, 'takes'):
        print(word)





# EXERCISE 3
# Use the provided code to find all the palindromes longer than 6 letters...
# Write a function called "is_palindrome" that takes a string as an argument and returns True or False if it is a palindrome or not.
# -----------

def reverse_word(word):
    return ''.join(reversed(word))

def is_palindrome(word):
    return word == reverse_word(word)

for word in word_list:
    if len(word) >= 7 and is_palindrome(word):
        print(word)





# EXERCISE 4
# Write a "reverse_sentence" function that takes a string as an argument.
# It should return a new string that contains the same words in reverse order.
# You can use the "capitalize" method for the first word in the returned string.
# -----------

def reverse_sentence(sentence):
    words = sentence.lower().split()
    rev = list(reversed(words))
    rev[0] = rev[0].capitalize()
    return ' '.join(rev)

sentence = "Reverse this sentence"
print(reverse_sentence(sentence))





# EXERCISE 5
# Write a "total_length" function that takes a list of strings and riturns the total length of the strings.
# -----------

def total_length(words):
    length = 0
    for word in words:
        length += len(word)
    return length

#words = ['123', '1234', '12']      # total: 9 characters
#print(total_length(words))         # prints: 9

print(total_length(word_list))
