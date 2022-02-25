# https://www.codewars.com/kata/persistent-bugger/train/python
# My solution
import functools
import operator

mul = lambda n: functools.reduce(operator.mul, map(int, str(n)))
leni = lambda n: len(str(n))

def persistence(n):
    return 1 + persistence(mul(n)) if leni(n) > 1 else 0 

# And
import functools
import operator

def persistence(n):
    mul = lambda n: functools.reduce(operator.mul, map(int, str(n)))
    return 1 + persistence(mul(n)) if n >= 10 else 0 

# ...
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i