# https://www.codewars.com/kata/binary-addition/train/python
# My solution
def add_binary(a,b):
    return str(bin(a+b))[2:]

# ...
def add_binary(a,b):
    return '{0:b}'.format(a + b)

# ...
def add_binary(a, b):
    return format(a + b, 'b')

# ...
def find_highest_power_2(num):
    n=0
    while 2**n <= num:
        n += 1
    return n-1    

def add_binary(a,b):
    sum = a + b
    number = 0
    while sum != 0:
        place_holder = find_highest_power_2(sum)
        number += 10**place_holder
        sum = sum - 2**place_holder
    return str(number)

# ...
def add_binary(a,b):
    n = a + b
    binList = []
    while (n > 0):
        binList.append(n % 2)
        n = n // 2
    return ''.join(map(str, reversed(binList)))