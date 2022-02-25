# https://www.codewars.com/kata/transformation-of-a-number-through-prime-factorization/train/python
# My solution
import functools, math

def is_prime(n):
    if n % 2 == 0 and n > 2: return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

def primes_gen():
    """ Generate an infinite sequence of prime numbers."""
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
    
def f(n):
    if is_prime(n): return 1
    numbers = {}
    primes = primes_gen()
    while n > 1:
        p = next(primes)
        while n % p == 0:
            numbers[p] = numbers.get(p, 0) + 1
            n //= p
            if is_prime(n):
                numbers[n] = numbers.get(n, 0) + 1
                n //= n
    
    return functools.reduce(lambda x,y: x*y, (value * math.pow(key, value-1) for key,value in numbers.items()) )

# ...
def f(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n / i
            factors.append(i)
        else:
            i += 1
            
    from collections import Counter
    from numpy import prod
    return prod([occurences * factor ** (occurences - 1)
                for factor, occurences in Counter(factors).items()])

# ...
def f(n):
    p, n_, m = 2, 1, int(n ** .5)
    while n > 1 and p <= m:
        k = 0
        while not n % p:
            k += 1
            n //= p
        if k:
            n_ *= k * p ** (k - 1)
        p += 1
    return n_

