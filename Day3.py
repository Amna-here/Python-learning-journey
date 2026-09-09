# Today's Focus:
# Practicing Python Strings, String Slicing,
# String Functions, and Escape Sequences.

#       Day3 mini Projects


# 1. Text Analyzer using Python String Functions

text = input("Enter a sentence: ")

print("\n===== TEXT ANALYZER =====")

# Original text
print("Original text:", text)

# Length of the text
print("Number of characters:", len(text))

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Capitalize first letter
print("Capitalized:", text.capitalize())

# Title case
print("Title Case:", text.title())

# Count a character
character = input("\nEnter a character to count: ")
print("Occurrences:", text.lower().count(character.lower()))

# Find a word
word = input("Enter a word to find: ")
position = text.lower().find(word.lower())
if position != -1:
    print("Word found at position:", position)
else:
    print("Word not found.")

# Check beginning and ending
print("\nDoes the sentence start with 'Hello'?",
      text.lower().startswith("hello"))
print("Does the sentence end with a period?",
      text.endswith("."))

# Replace a word
old_word = input("\nEnter a word you want to replace: ")
new_word = input("Enter the new word: ")
updated_text = text.replace(old_word, new_word)
print("\nUpdated sentence:", updated_text)

# ---------------------------------------------------

# 2. Personalized Letter Generator

name = input("Enter your name: ")
date = input("Enter today's date: ")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
Congratulations!
'''
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print("\n===== YOUR LETTER =====")
print(letter)

# ------------------------------------------------

# 3. Word Detective

sentence = input("Enter a sentence: ")
word = input("Enter a word to search for: ")
print("\n===== WORD DETECTIVE =====")
print("Word position:", sentence.find(word))
print("Number of occurrences:", sentence.count(word))
if sentence.find(word) != -1:
    print("The word was found!")
else:
    print("The word was not found.")
print("Does the sentence end with '.'?",
      sentence.endswith("."))

# Purpose:
# These mini projects apply the string concepts