# https://www.codewars.com/kata/weight-for-weight/train/python
# My solution
def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda x: sum(map(int, x))))

# Refactory
def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: (sum(map(int, x)),x)))

# Other ways
def weight_key(s):
    return (sum(int(c) for c in s), s)
def order_weight(s):
    return ' '.join(sorted(s.split(' '), key=weight_key))