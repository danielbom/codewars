# https://www.codewars.com/kata/simpsons-rule-approximate-integration/train/python
# My solution
import math

def simpson(n):
    a, b = 0, math.pi
    f = lambda x: (3/2) * (math.sin(x) ** 3)
    h = (b - a) / n
    res = f(a)
    res += 4 * sum(f(a + i*h) for i in range(1, n, 2))
    res += 2 * sum(f(a + i*h) for i in range(2, n, 2))
    res += f(b)
    return (h / 3) * res
# ...
def simpson(n):
    from math import sin, pi
    
    a = 0
    b = pi
    h = (b - a)/n
    
    f = lambda x: (3/2) * sin(x)**3
    
    integral = 0
    integral += f(a) + f(b)
    integral += 4*sum(f(a +(2*i - 1)*h) for i in range(1, n//2 + 1))
    integral += 2*sum(f(a + 2*i*h) for i in range(1, n//2))
    integral *= h/3
    
    return integral
# ...
from math import pi, sin

def simpson(n):
    f = lambda x : (3/2) * (sin(x) ** 3)
    
    b = pi
    a = 0
    
    h = (b-a)/n
    coeff = 1/3*h
    sum_a = 4 * sum([f(a + (2*i - 1)*h) for i in range(1, n//2 + 1)])
    sum_b = 2 * sum([f(a + 2*i * h) for i in range(1, n//2)])
    
    return coeff * (f(a) + f(b) + sum_a + sum_b)
# ...
