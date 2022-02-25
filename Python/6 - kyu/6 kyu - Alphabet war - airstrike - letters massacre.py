# https://www.codewars.com/kata/alphabet-war-airstrike-letters-massacre/train/python
# My solution
import re
def alphabet_war(fight):
    fight = re.sub("[a-z]?\*[a-z]?", "", fight)
    powers = dict(zip("wpbs_zdqm", range(-4, 5)))
    points = sum(powers.get(l, 0) for l in fight)
    if points > 0: return "Right side wins!"
    if points < 0: return "Left side wins!"
    return "Let's fight again!"

# ...
import re
powers = {
    'w': -4, 'p': -3, 'b': -2, 's': -1,
    'm': +4, 'q': +3, 'd': +2, 'z': +1,
}
def alphabet_war(fight):
    fight = re.sub('.(?=\*)|(?<=\*).', '', fight)
    result = sum(powers.get(c, 0) for c in fight)
    if result < 0:
        return 'Left side wins!'
    elif result > 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"

# ...
import re
alphabet_war = lambda s:["Let's fight again!","Left side wins!","Right side wins!"][
cmp(sum(i*n for i,n in enumerate(map(re.sub('.?\*+.?','',s).count,'mqdz*sbpw'),-4)),0)]

# ...
import re
def alphabet_war(fight):
    pattern = re.compile(r"(\w)?\*+(\w)?")
    powers = pattern.sub("", fight)
    scores = "mqdz*sbpw" 
    score = sum(i * powers.count(p) for i, p in enumerate(scores, -4))
    return ["Let's fight again!", "Left side wins!", "Right side wins!"][(score>0)-(score<0)]

# ...
import re
powers = {'w':4,'p':3,'b':2,'s':1,'m':-4,'q':-3,'d':-2,'z':-1}
def alphabet_war(fight):
    battle = sum(powers[x] for x in re.sub(r"[^wpbsmqdz]","",re.sub(r"[a-z]?[*]+[a-z]?","",fight)))
    return "Left side wins!" if battle > 0 else "Right side wins!" if battle < 0 else "Let's fight again!"