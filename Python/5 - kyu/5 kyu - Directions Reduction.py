# https://www.codewars.com/kata/directions-reduction/train/python
# My solution
import re

def dirReduc(arr):
    card = {"NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}
    arr = "".join(map(lambda elem: card[elem], arr))
    while "NS" in arr or "SN" in arr or "EW" in arr or "WE" in arr:
        arr = re.sub("NS|SN|EW|WE", "", arr)
    cardr = {v: k for k,v in card.items()}
    return list(map(lambda elem: cardr[elem], list(arr)))

# ...
def dirReduc(arr):
    ix = 0
    while ix < len(arr)-1:
        if arr[ix][0] + arr[ix+1][0] in ["NS", "SN", "EW", "WE"]:
            arr[ix:ix+2] = []
            if ix: ix -= 1
        else:
            ix += 1
    return arr
# ...
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
# ...
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3
# ...
def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr
# ...
def dirReduc(arr):
    s = ''.join([d[0] for d in arr])
    while True:
        o = s
        s = s.replace('NS', '')
        s = s.replace('SN', '')
        s = s.replace('EW', '')
        s = s.replace('WE', '')
        if o == s:
            break
    lookup = {'N': 'NORTH', 'S': 'SOUTH', 'E': 'EAST', 'W': 'WEST'}
    return [lookup[c] for c in s]