# https://www.codewars.com/kata/find-the-next-perfect-square/train/python
# My solution
find_next_square = lambda sq : -1 if int(sq**0.5)**2 != sq else int(sq**0.5+1)**2
    # Return the next square if sq is a square, -1 otherwise

# ...
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

# ...
import math
def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1

# ...
from math import sqrt
def find_next_square(sq):
    return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1
