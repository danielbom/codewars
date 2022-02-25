# https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python
# My solution
def digitize(n):
    return list(map(int, str(n)[::-1]))

