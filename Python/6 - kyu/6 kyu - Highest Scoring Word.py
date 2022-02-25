# https://www.codewars.com/kata/highest-scoring-word/train/python
# My solution
def high(x):
    m,string = 0, ""
    for s in x.split():
        calc = sum(ord(ch.lower()) - 96 for ch in s)
        if calc > m:
            m = calc
            string = s
    return string

# ...
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# ...
def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))

# ...
def high(s):
    return max( (sum(ord(c) - 96 for c in x), x) for x in s.split() )[1]

# ...
