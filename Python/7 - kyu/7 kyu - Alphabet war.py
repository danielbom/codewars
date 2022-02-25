# https://www.codewars.com/kata/alphabet-war/train/python
# My solution
def alphabet_war(fight):
    p = dict(zip("sbpwzdqm", [1,2,3,4,-1,-2,-3,-4]))
    r = sum(p.get(i, 0) for i in fight)
    return "Right side wins!" if r < 0 else "Left side wins!" if r > 0 else "Let's fight again!"

# ...
def alphabet_war(fight):
    result = sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    return "{} side wins!".format("Left" if result < 0 else "Right") if result else "Let's fight again!"

# ...
alphabet_war=lambda s,f=(lambda x,y:sum(y.find(e)+1 for e in x)):(lambda a,b:"Let's fight again!" if a==b else '{} side wins!'.format(['Left','Right'][b>a]))(f(s,'sbpw'),f(s,'zdqm'))

