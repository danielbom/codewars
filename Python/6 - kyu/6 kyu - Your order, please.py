# https://www.codewars.com/kata/your-order-please/train/python
# My solution
def order(sentence):
    return ' '.join(sorted(sentence.split(), key = min ))

# ...
from functools import reduce
def order(sentence):
  return reduce(lambda x,y: x+' '+y, sorted(sentence.split(), key = lambda x: ''.join(filter(str.isdigit, x)) )) if sentence != '' else ''

# ...
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# ...
order = lambda xs: ' '.join(sorted(xs.split(), key=min))

