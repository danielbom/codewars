# https://www.codewars.com/kata/primes-in-numbers/train/python
# My solution
import math

def prime_factorize(n):
    factors = []
    number = int(n)
    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number /= factor
    return tuple(factors)

def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2
    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x
    return int(n)

def primeFactors(n):
    primes = prime_factorize(n)
    unique = sorted(list(set(primes)))
    return ''.join('(%d' % q + ('**%d' % primes.count(q)) * (primes.count(q) > 1) + ')' for q in unique)

# ...
def primeFactors(n):
    ret = ''
    for i in xrange(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret

# ...
def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)

# ...
from collections import Counter

def fac(n):
    maxq = int(n ** .5)
    d, q = 1, n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = 1 + d*4 - d//2*2
        d += 1
    res = Counter()
    if q <= maxq:
        res += fac(n//q)
        res += fac(q)
    else: res[n] = 1
    return res

def primeFactors(n):
    return ''.join(('({})' if m == 1 else '({}**{})')
        .format(p, m) for p, m in sorted(fac(n).items()))