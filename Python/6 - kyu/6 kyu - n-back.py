# https://www.codewars.com/kata/n-back/train/python
# My solution
def count_targets(n, sequence):
    return sum(y == x for x, y in zip(sequence, sequence[n:]))

# ...
def count_targets(n, sequence):
    return sum(1 for a, b in zip(sequence, sequence[n:]) if a == b)
