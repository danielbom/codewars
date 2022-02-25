# https://www.codewars.com/kata/youre-a-square/train/python
# My solution
def is_square(n):    
    return (n ** 0.5).is_integer() if n >= 0 else False
# ...
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0
# ...
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

