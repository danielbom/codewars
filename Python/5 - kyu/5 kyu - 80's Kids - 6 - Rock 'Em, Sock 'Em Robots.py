# https://www.codewars.com/kata/80-s-kids-number-6-rock-em-sock-em-robots/train/python
# My solution
def fight(robot_1, robot_2, tactics):
    if robot_1["speed"] < robot_2["speed"]:
        robot_1, robot_2 = robot_2, robot_1      
    MSG = "{} has won the fight."
    n1, n2 = len(robot_1["tactics"]), len(robot_2["tactics"])

    for i in range(max(n1, n2)):
        if i < n1:
            robot_2["health"] -= tactics[robot_1["tactics"][i]]
            if robot_2["health"] <= 0: return MSG.format(robot_1["name"])
        if i < n2:
            robot_1["health"] -= tactics[robot_2["tactics"][i]]
            if robot_1["health"] <= 0: return MSG.format(robot_2["name"])
    
    return "The fight was a draw." if robot_1["health"] == robot_2["health"] else \
            MSG.format(robot_1["name"] if robot_1["health"] > robot_2["health"] else robot_2["name"])

# ...
from operator import itemgetter

def fight(r1, r2, tactics):
    
    i, bots = 0, sorted((r2,r1), key=itemgetter('speed'))                    # Get the bots in reversed order!
    for r in bots: r['tactics'] = r['tactics'][::-1]                         # Reverse the tactics to use pop()
    
    while 1:
        i ^= 1                                                               # Swapper
        if bots[i]['tactics']:
            bots[i^1]['health'] -= tactics[ bots[i]['tactics'].pop() ]       # Hit
        
        if bots[i^1]['health'] <= 0 or all(not r['tactics'] for r in bots):  # other bot is dead or no tactics for both of them
            break
    
    a,b = bots
    cmp = (a['health'] < b['health']) - (a['health'] > b['health'])          # 1: b wins / -1: a wins / 0: tie
    
    return "The fight was a draw." if not cmp else f"{bots[max(cmp,0)]['name']} has won the fight."

# ...
def fight(A, B, damage):
    if B['speed'] > A['speed']: A, B = B, A

    while A['tactics'] or B['tactics']:
        for attack, defend in [(A, B), (B, A)]:
            if attack['tactics']:
                defend['health'] -= damage[attack['tactics'][0]]
                attack['tactics'] = attack['tactics'][1:]
                if defend['health'] <= 0: return attack['name'] + ' has won the fight.'
                
    return 'The fight was a draw.' if A['health'] == B['health'] else [B, A][A['health'] > B['health']]['name'] + ' has won the fight.'