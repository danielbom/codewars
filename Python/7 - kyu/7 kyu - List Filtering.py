# https://www.codewars.com/kata/list-filtering/train/python
# My solution
def filter_list(l):
    return [i for i in l if type(i) != type("")]

# ...
def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]

# ...
def filter_list(l):
    return filter(lambda x: not type(x) is str, l)

# ...
def filter_list(l):
    'return a new list with the strings filtered out'
    return [e for e in l if isinstance(e, int)]