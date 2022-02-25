# https://www.codewars.com/kata/two-to-one/train/python
# My solution
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))
    