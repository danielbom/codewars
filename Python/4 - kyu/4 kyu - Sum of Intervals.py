# https://www.codewars.com/kata/sum-of-intervals/train/python
# My solution
def sum_of_intervals(intervals):
    return len(set(j for i in intervals for j in range(i[0],i[1])))

# ...
def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

# ...
from itertools import chain

def sum_of_intervals(intervals):
    return len(set(chain.from_iterable(range(*i) for i in intervals)))

    