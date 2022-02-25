# https://www.codewars.com/kata/55a243393fb3e87021000198/train/python
# My solution
def remember(text):
    counter = {}
    result = []
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
        if counter[ch] == 2:
            result.append(ch)
    return result

# ...
def remember(str_):
    seen = set()
    res = []
    for i in str_: 
        res.append(i) if i in seen and i not in res else seen.add(i)
    return res
