# https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
# My solution
def namelist(names):
    return ' & '.join(', '.join(i['name'] for i in names).rsplit(', ', 1))

# Other
def namelist(names):
    if not names: return ''
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        return ' & '.join([i['name'] for i in names])
    return names[0]['name'] + ', ' + namelist(names[1:])