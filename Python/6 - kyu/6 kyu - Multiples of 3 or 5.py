# https://www.codewars.com/kata/multiples-of-3-or-5/train/python
# My solution
import math
def solution(n):
    soma = 0
    nn = (n//3)
    soma += 3*(nn*(nn+1))//2    
    
    nn = (n//5)-1
    soma += 5*(nn*(nn+1))//2

    nn = (n//15)
    soma -= 15*(nn*(nn+1))//2

    return soma

# ...
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# ...
def solution(number):
    threes = (number - 1) / 3
    fives = (number - 1) / 5
    fifteens = (number - 1) / 15
    return 3 * threes * (threes + 1) / 2 + 5 * fives * (fives + 1) / 2 - 15 * fifteens * (fifteens + 1) / 2

# ...
def solution(number):
    import itertools
    return sum(set(itertools.chain(range(0, number, 3), range(0, number, 5))))
