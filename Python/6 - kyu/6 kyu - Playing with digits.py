# https://www.codewars.com/kata/playing-with-digits/train/python
# My solution
def dig_pow(n, p):
    div, mod = divmod(sum(int(l) ** (i + p) for i,l in enumerate(str(n))), n)
    return div if mod == 0 else -1

# ...
def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1

# ...
def dig_pow(n, p):
    t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)) )
    return t//n if t%n==0 else -1
