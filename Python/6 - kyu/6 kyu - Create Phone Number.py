# https://www.codewars.com/kata/create-phone-number/train/python
# My solution
def create_phone_number(n):
    n = list(map(str,n))
    return '(' + ''.join(n[:3]) + ') ' + ''.join(n[3:6]) + '-' + ''.join(n[6:])

# ...
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# ...
def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

