# https://www.codewars.com/kata/find-the-parity-outlier/train/python
# My solution
def find_outlier(Int):
    odd  = lambda x: x % 2
    even = lambda x: not x % 2
    f = even if sum(map(odd, Int[:3])) >= 2 else odd
    for i in Int:
        if f(i): return i

# ...
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

# ...
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

# ...
def find_outlier(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False

# ...
def find_outlier(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]