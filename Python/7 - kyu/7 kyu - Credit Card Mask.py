# https://www.codewars.com/kata/credit-card-mask/train/python
# My solution
def maskify(cc):
    return '#' * (len(cc) - 4) + cc[-4:]

# ...
def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))

# ...
def maskify(cc):
    width = len(cc)
    return cc[-4:].rjust(width, '#')