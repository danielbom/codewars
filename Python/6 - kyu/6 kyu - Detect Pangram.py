# https://www.codewars.com/kata/detect-pangram/train/python
# My solution
import string
def is_pangram(text):
    return len( {letter.lower() for letter in text if letter.isalpha()} ) == 26

# ...
import string
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

# ...
import string
def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.lowercase)

