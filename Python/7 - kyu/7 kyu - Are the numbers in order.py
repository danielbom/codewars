# https://www.codewars.com/kata/are-the-numbers-in-order/train/python
# My solution
def in_asc_order(l):
    return not any(l[i] > l[i+1] for i in range(len(l)-1))

# ...
def in_asc_order(arr):
    return arr == sorted(arr)

# ...
def in_asc_order(a):
    return all(x < y for x, y in zip(a, a[1:]))

