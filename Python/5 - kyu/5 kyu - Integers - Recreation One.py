# https://www.codewars.com/kata/integers-recreation-one/train/python
# My solution
CACHE = {}

def soma_divisores_quadrado(x):
    if x in CACHE:
        return CACHE[x]
    divisores = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisores.append(i)
            if x % (x // i) == 0:
                divisores.append(x // i)
    soma_quadrados = sum([i**2 for i in sorted(list(set(divisores)))])
    if soma_quadrados == int(soma_quadrados**0.5)**2:
        CACHE[x] = [x, soma_quadrados]
        return [x, soma_quadrados]
    CACHE[x] = None
    return None

def list_squared(m, n):
    resultado = [soma_divisores_quadrado(i) for i in range(m,n+1)]
    return [i for i in resultado if i is not None]

# ...
CACHE = {}

def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret

# ...
WOAH = [1, 42, 246, 287, 728, 1434, 1673, 1880, 
        4264, 6237, 9799, 9855, 18330, 21352, 21385, 
        24856, 36531, 39990, 46655, 57270, 66815, 
        92664, 125255, 156570, 182665, 208182, 212949, 
        242879, 273265, 380511, 391345, 411558, 539560, 
        627215, 693160, 730145, 741096]

list_squared = lambda HUH, YEAH: [[YES, DUH(YES)] for YES in WOAH if YES >= HUH and YES <= YEAH]
DUH = lambda YEP: sum(WOW**2 for WOW in range(1, YEP + 1) if YEP % WOW == 0)

# ...
from itertools import chain
from functools import reduce


def factors(n):
    return set(chain.from_iterable(
        [d, n // d] for d in range(1, int(n**0.5) + 1) if n % d == 0))


def square_factors(n):
    return reduce(lambda s, d: s + d**2, factors(n), 0)


def list_squared(m, n):
    l = []
    for x in range(m, n + 1):
        s = square_factors(x)
        if (s**0.5).is_integer():
            l.append([x, s])
    return l

