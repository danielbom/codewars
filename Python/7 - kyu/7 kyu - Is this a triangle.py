# https://www.codewars.com/kata/is-this-a-triangle/train/python
# My solution
def is_triangle(a, b, c):
    return a+b > c and a+c > b and b+c > a

# ...
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

# ...
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

# ...
def is_triangle(a, b, c):
    return 2 * max(a, b, c) < a + b + c