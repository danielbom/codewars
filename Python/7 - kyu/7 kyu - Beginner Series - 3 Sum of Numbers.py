# https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python
# My solution
def get_sum(a,b):
    max_ = max(a,b)
    min_ = (a+b)-max_
    return sum(i for i in range(min_, max_+1))

# ...
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))

# Math
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2