# https://www.codewars.com/kata/replace-with-alphabet-position/train/python
# My solution
def alphabet_position(text):
    letters = filter(str.isalpha, text.lower())
    nth_letters = map(lambda ch: ord(ch) - ord('a') + 1, letters)
    return " ".join(map(str, nth_letters))

# ...
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())