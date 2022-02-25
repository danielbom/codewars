# https://www.codewars.com/kata/pete-the-baker/train/python
# My solution
def cakes(r, a):
    '''
        input
        r : recipe,
        a : available
    ''' 
    return min([ a[k] // r[k] if k in a.keys() else 0 for k in r.keys()])

# ...
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)
