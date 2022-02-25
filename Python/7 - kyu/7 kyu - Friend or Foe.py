# https://www.codewars.com/kata/friend-or-foe/train/python
# My solution
def friend(x):
    return list(filter(lambda name: len(name) == 4,x))

# Other ways
def friend(x):
    return [f for f in x if len(f) == 4]