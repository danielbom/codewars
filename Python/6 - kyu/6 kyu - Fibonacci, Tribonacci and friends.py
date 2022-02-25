# https://www.codewars.com/kata/fibonacci-tribonacci-and-friends/train/python
# My solution
class CircularList(object):
    def __init__(self, listx):
        self.list = listx[:]
        self.i = 0
        self.n = len(listx)
    
    def add(self, x):
        self.list[self.i] = x
        self.i = (self.i + 1) % self.n

    def __iter__(self):
        return iter(self.list)

def Xbonacci(signature, n):
    xbonacci_list = list(signature)
    circular_list = CircularList(xbonacci_list)
    xn = circular_list.n
    
    while xn < n:
        next_sum = sum(circular_list)
        circular_list.add(next_sum)
        xbonacci_list.append(next_sum)
        xn += 1
    
    return xbonacci_list[:n]

# ...
def Xbonacci(signature,n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output

# ...
def Xbonacci(signature, n):
    result = []
    for i in range(n):
        signature.append(sum(signature))
        result.append(signature.pop(0))
    return result

# ...
def Xbonacci(signature,n):
    def gen_bonacci(signature):
        yield from signature
        from collections import deque
        signature = deque(signature)
        while 1:
            signature.append(sum(signature))
            signature.popleft()
            yield signature[-1]
    from itertools import islice
    return [i for i in islice(gen_bonacci(signature), n)]