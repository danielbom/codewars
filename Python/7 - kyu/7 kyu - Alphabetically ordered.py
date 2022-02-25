# https://www.codewars.com/kata/alphabetically-ordered/train/python
# My solution
def alphabetic(s):
    return sorted(s) == list(s)

# def alphabetic(s):
    return all(a<=b for a,b in zip(s, s[1:]))
