# https://www.codewars.com/kata/remove-the-minimum/train/python
# My solution
def remove_smallest(numbers):
    if numbers:
        r = numbers[:]
        r.remove(min(numbers))
        return r
    return []

# ...
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

# ...
def remove_smallest(numbers):
    if len(numbers) < 1: 
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx+1:]

# ...
def remove_smallest(numbers):
    #    raise NotImplementedError("TODO: remove_smallest")
    return [numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]