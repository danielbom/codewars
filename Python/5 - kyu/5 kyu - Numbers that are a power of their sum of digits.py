# https://www.codewars.com/kata/numbers-that-are-a-power-of-their-sum-of-digits/train/python
# My solution
def power_sum_digs(x): # Calculando as potencias da soma sem transformar o numero em string
        n = r = 0
        while x: r, x, n = r + x % 10, x // 10, n + 1
        return [r ** i for i in range(2, n + 1)]

CACHE = [i**j for i in range(2, 100) for j in range(2, 20)]
CACHE = [i for i in set(CACHE) if i in power_sum_digs(i)]
CACHE.sort()

def power_sumDigTerm(n):
    return CACHE[n-1]

# ...
series = [0]
for a in range(2, 99):
    for b in range(2, 42):
        c = a**b
        if a == sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__

# ...
def dig_sum(n):
    return sum(map(int, str(n)))

terms = []
for b in range(2, 400):
    for p in range(2, 50):
        if dig_sum(b ** p) == b:
            terms.append(b ** p)
terms.sort()

def power_sumDigTerm(n):
    return terms[n - 1]

# ...
sum_dig = lambda n : reduce(lambda x,y : x + int(y),str(n),0)

memo = []

for i in xrange(2,100):
    for j in xrange(1,100):
        p = i ** j
        if p > 10 and sum_dig(p) == i:memo += [p]

memo.sort()

def power_sumDigTerm(n):
    return memo[n - 1]