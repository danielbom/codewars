# https://www.codewars.com/kata/count-the-smiley-faces/train/python
# My solution
def count_smileys(arr):
    return len(list(filter(lambda x: x[-1] in ")D" and (x[-2] in '-~'+x[0]), arr)))

# Other ways
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

# ...
def count_smileys(arr):
    import re
    smiley = re.compile(r"[:;][-~]?[)D]")
    return sum(bool(re.match(smiley, el)) for el in arr)