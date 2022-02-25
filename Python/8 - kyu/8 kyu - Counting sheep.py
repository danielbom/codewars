# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
# My solution
def count_sheeps(arrayOfSheeps):
    return sum(1 for i in arrayOfSheeps if i)

# Other ways
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)