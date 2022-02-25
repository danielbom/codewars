# https://www.codewars.com/kata/where-my-anagrams-at/train/python
# My solution
def anagrams(word, words):
    word = sorted(word)
    return [i for i in words if sorted(i) == word]

# ...
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
