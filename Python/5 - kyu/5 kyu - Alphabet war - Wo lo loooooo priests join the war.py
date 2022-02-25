# https://www.codewars.com/kata/alphabet-war-wo-lo-loooooo-priests-join-the-war/train/python
# My solution
def alphabet_war(fight):
    priest_j = dict(zip("wpbs", "mqdz"))
    priest_t = dict(zip("mqdz", "wpbs"))
    fight = list(fight)
    n = len(fight)
    for i in range(n):
        if fight[i] in "jt":
            subs = priest_j if fight[i] == "j" else priest_t 
            if i > 0:
                fight[i-1] = subs.get(fight[i-1], fight[i-1])
            if i < n-1:
                fight[i+1] = subs.get(fight[i+1], fight[i+1])
    
    powers = dict(zip("wpbsPzdqm",range(-4,5)))
    damage = sum( powers.get(i,0) for i in fight)

    return "Let's fight again!" if damage == 0 \
          else "{:s} side wins!".format("Right" if damage > 0 else "Left")

# And
def alphabet_war(fight):
    priest = {"j": dict(zip("wpbs", "mqdz")), "t": dict(zip("mqdz", "wpbs")) }
    powers = dict(zip("wpbs_zdqm",range(-4,5)))
    def changed(l, c, r):
        if l + r not in "jtj":
            c = priest.get(l, {}).get(c, c)
            c = priest.get(r, {}).get(c, c)
        return c

    damage = sum(powers.get(changed(l,c,r),0) for l, c, r in zip(" " + fight, fight, fight[1:] + " "))

    return "Let's fight again!" if damage == 0 else \
        ("Right" if damage > 0 else "Left") + " side wins!"

# ...
def alphabet_war(fight):
    SWAP = {'j':{'w':'m','p':'q','b':'d','s':'z'}, 't':{'m':'w','q':'p','d':'b','z':'s'}}
    s = 0

    for l, c, r in zip(' ' + fight, fight, fight[1:] + ' '):
        if l + r not in 'tjt':
            c = SWAP.get(l, {}).get(c, c)
            c = SWAP.get(r, {}).get(c, c)
        s += {'w':4, 'p':3, 'b':2, 's':1, 'm':-4, 'q':-3, 'd':-2, 'z':-1}.get(c, 0)

    return ["Right side wins!", "Left side wins!"][s > 0] if s else "Let's fight again!"

