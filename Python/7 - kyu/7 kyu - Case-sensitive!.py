# https://www.codewars.com/kata/case-sensitive-1/train/python
# My solution
def case_sensitive(s):
    uppers = [ch for ch in s if ch.isupper()]
    return [len(uppers) == 0, uppers]

# ...
def case_sensitive(s):
    return [s.islower() or not s, [c for c in s if c.isupper()]]

# ...
def case_sensitive(s):
    result = [char for char in s if char.isupper()]
    return [ result == [], result ]

# ...
def case_sensitive(s):
    l = list(filter(str.isupper,s))
    return[not l,l]
