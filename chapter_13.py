# The exercises require the content below.

import shelve
import os
import hashlib

def md5_digest(filename):
    data = open(filename, "rb").read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

def same_contents(path1, path2):
    reader = open(path1, "rb")
    data1 = reader.read()
    reader. close()

    reader = open(path2, "rb")
    data2 = reader.read()
    reader.close()

    return data1 == data2


# EXERCISE 0 -- FROM THE "STORING DATA STRUCTURES" SECTION
# Finish the example from the section by reading the word list and storing all of the anagrams in a shelf.
# The existing code is below.

def sort_word(word):
    return "".join(sorted(word))

db = shelve.open("resources/anagram_map", "n")

# -------------

word_dict = {}

reader = open("resources/words.txt")
for line in reader:
    word_dict[line.strip().lower()] = 1
reader.close()

for word in word_dict:
    key = sort_word(word)

    if key in db:
        value = db[key]
        value.append(word)
        db[key] = value
    else:
        db[key] = [word]

print(f"Number of keys in anagram_map: {len(db)}.")
print(f"Anagrams of 'post': {db['opst']}")
db.close()





# EXERCISE 1
# Ask a chatbot. No code. Not needed here.
# -----------





# EXERCISE 2
# Write a "replace_all" function that takes two strings as arguments, and two filenames.
# It should read the first file and write its contents into the second file, creating it if needed.
# If the pattern of the first string appears anywhere in the second file, it should be replaced with the second string.
# -----------

# If working wiht txt files, I assume we need to use the file object, not a shelf.
def replace_all(pattern, replacement, source_file, output_file):
    reader = open(source_file)
    content = reader.read()
    reader.close()
    
    content = content.replace(pattern, replacement)

    writer = open(output_file, "w")
    writer.write(content)
    writer.close()

replace_all("photos", "images", "resources/photos/notes.txt", "resources/photos/new_notes.txt")





# EXERCISE 3
# Whoops, I misunderstood exercise 0 and did it early... kind of.
# Write an "add_word" function that takes as arguments a string and a shelf object.
# Sort the letters to make a key, check if it is already in the shelf.
# If not, make a list with the word in it, and add it.
# If yes, append it to the list. Maybe also check if it's already there.
# ------------

def add_word(word, shelf):
    word = word.lower()
    key = sort_word(word)

    if key not in shelf:
        shelf[key] = [word]
    elif word not in shelf[key]:
        value = shelf[key]
        value.append(word)
        shelf[key] = value

db = shelve.open("resources/anagram_map", "c")
word = "kLjupko"
print(f"Anagrams for {word}: {db.get(sort_word(word.lower()), 'none')}")
#add_word(word, db)
print(f"Anagrams for {word}: {db.get(sort_word(word.lower()), 'none')}")
db.close()





# EXERCISE 4
# Write the function to check for duplicate files, as instructed.
# -----------

# need to rewrite the walk function
def walk_image_dir(dirname, visit_func, shelf):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            visit_func(path, shelf)
        else:
            walk_image_dir(path, visit_func, shelf)

def is_image(path, extension_list):
    return os.path.splitext(path.lower())[-1] in extension_list

def add_path(path, shelf):
    digest = md5_digest(path)

    if digest in shelf:
        value = shelf[digest]
        value.append(path)
        shelf[digest] = value
    else:
        shelf[digest] = [path]

def process_path(path, shelf):
    if is_image(path, [".png", ".jpg", ".jpeg", ".webp"]):
        add_path(path, shelf)

db = shelve.open("resources/photos/digests", "n")
walk_image_dir("resources/photos", process_path, db)

for digest, paths in db.items():
    if len(paths) > 1:
        print(paths)
        if same_contents(paths[0], paths[1]):
            print("The files share not only the same digest, but also the same contents.")

