# https://www.codewars.com/kata/the-highest-profit-wins/train/python
# My solution
def min_max(lst):
    minimo = lst[0]
    maximo = lst[0]
    for i in lst:
        if i < minimo:
            minimo = i
        elif i > maximo:
            maximo = i
    return [minimo, maximo]

# ...
def min_max(lst):
  return [min(lst), max(lst)]

