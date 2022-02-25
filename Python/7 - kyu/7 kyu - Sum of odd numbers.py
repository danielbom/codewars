# https://www.codewars.com/kata/sum-of-odd-numbers/train/python
# My solution
def row_sum_odd_numbers(n):
    return n**3

# ...
row_sum_odd_numbers=(3).__rpow__

# ...
import numpy as np
def row_sum_odd_numbers(n):
    return sum(np.linspace(n**2-(n-1),(n**2+n-1),n))