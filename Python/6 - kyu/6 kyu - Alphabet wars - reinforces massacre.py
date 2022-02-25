# https://www.codewars.com/kata/alphabet-wars-reinforces-massacre/train/python
# My solution
def alphabet_war(reinforces, airstrikes):
    call_reinforces = [list(r) for r in reinforces]
    battlefield = call_reinforces.pop(0)
    n = len(battlefield)
    reinforces_avaliable = {i: [first] for i, first in enumerate(
        call_reinforces.pop(0) if call_reinforces else [])}
    
    for attack in airstrikes:
        # Airstrike attack
        for i, bomb in enumerate(attack):
            if bomb == '*':
                if i > 0:      battlefield[i-1] = '_'
                if i+1 <= n-1: battlefield[i+1] = '_'
                battlefield[i] = '_'
        # Recovering reinforces
        for i, survival in enumerate(battlefield):
            if survival == '_' and reinforces_avaliable.get(i):
                battlefield[i] = reinforces_avaliable.get(i).pop(0)
        # Update reinforces list
        for i, reinforce in enumerate(call_reinforces.pop(0) if call_reinforces else []):
            reinforces_avaliable[i].append(reinforce)
            
    return ''.join(battlefield)
# ...
from itertools import chain, repeat

def alphabet_war(reinforces, airstrikes):
    its = [chain(rs, repeat('_')) for rs in zip(*reinforces)]
    result = [next(it) for it in its]
    for strike in airstrikes:
        boom = set(chain.from_iterable([i-1, i, i+1] for i, x in enumerate(strike) if x == '*'))
        result = [next(it) if i in boom else x for i, (x, it) in enumerate(zip(result, its))]
    return ''.join(result)
# ...
def alphabet_war(r, airstrikes):
    rIdx = [0] * (len(r[0]) + 2)
    for a in airstrikes:
        massacre = {i+d for i,c in enumerate(a,1) for d in range(-1,2) if c == '*'}
        for i in massacre: rIdx[i] += 1
    return ''.join(r[row][i] if row < len(r) else "_" for i,row in enumerate(rIdx[1:-1]))
# ...
def alphabet_war(reinforces, airstrikes):
    # Convert rows into columns of reinforcements
    reups = list(map(list, zip(*reinforces[1:]))) if len(reinforces) > 1 else [list() for _ in range(len(reinforces[0]))]
    # Initialise the fort line
    front_line = list(reinforces[0])
    for strike in airstrikes:
        # Identify bombed location indices
        hits = [i for i, c in enumerate(strike) if c == "*"]
        hits = set(hits + [i - 1 for i in hits] + [i + 1 for i in hits])
        # Remove casualties
        front_line = [c if i not in hits else "_" for i, c in enumerate(front_line)]
        # Promote head of queue for each gap where possible
        front_line = [reups[i].pop(0) if c == "_" and reups[i] else c for i, c in enumerate(front_line)]
    return "".join(front_line)
# ...
bomb = '*'
dead = '_'

def alphabet_war(reinforces, airstrikes):
    # Initialise the front line
    front_line = list(reinforces.pop(0))
    
    # Convert rows into columns of reinforcements
    reups = list(map(list, zip(*reinforces))) if reinforces else [None] * len(front_line)
    
    # Airstrike! Run for cover!
    for strike in airstrikes:
        # Identify bombed locations
        hits = set()
        for location, dropped in enumerate(strike):
            if dropped == bomb:
                hits |= set([location-1, location, location+1])
        
        # Remove casualties
        front_line = [dead if location in hits else soldier for location, soldier in enumerate(front_line)]
        
        # Get new reinforcements where possible
        front_line = [reups[location].pop(0) if soldier == dead and reups[location] else soldier for location, soldier in enumerate(front_line)]
    
    return "".join(front_line)
# ...
def alphabet_war(reinforces, airstrikes):
    ll = len(reinforces[0])
    R = [[r[i] for r in reinforces[::-1]] for i in range(ll)]
    battle = ''.join(R[i].pop() for i in range(ll))

    for a in airstrikes:
        battle = ''.join((R[i].pop() if R[i] else '_') if '*' in a[max(0, i-1):i+2] else battle[i] for i in range(ll))
    return battle
# ...
def alphabet_war (reinforces, airstrikes):
    def devastation(airstrike):
        return {i+a for i, v in enumerate(airstrike) for a in range(-1,2) if v == '*'}
        
    # flatten list of strike indices.
    bombindex = [item for sublist in map(devastation, airstrikes) for item in sublist
                 if (item >= 0 & item <= len(reinforces[0]))] # clean dirty bomb ;)

    # frequency of explosions at index position
    frequency = [bombindex.count(i) for i in range(len(reinforces[0]))]

    # create result letter by letter with frequency as index on reinforcement
    result = [reinforces[v][i] if (v < len(reinforces)) else '_'
              for i, v in enumerate(frequency)]

    return ''.join(result)
# ...
def alphabet_war(reinforces, airstrikes):
    reinforcement_arr = []
    for each_str in reinforces:
        reinforcement_arr.append([each_char for each_char in each_str])
    battle_field = reinforcement_arr.pop(0)

    for each_strike in airstrikes:
        for index_inner, strike_param in enumerate(each_strike):
            if strike_param == '*':
                battle_field[index_inner] = '_'
                if (index_inner + 1) < len(battle_field):
                    battle_field[index_inner + 1] = '_'
                if (index_inner - 1) > -1:
                    battle_field[index_inner - 1] = '_'

        for bat_idx in range(0, len(battle_field)):
            if battle_field[bat_idx] == '_':
                for reinf_idx in range(0, len(reinforcement_arr)):
                    if reinforcement_arr[reinf_idx][bat_idx] != '':
                        battle_field[bat_idx] = reinforcement_arr[reinf_idx][bat_idx]
                        reinforcement_arr[reinf_idx][bat_idx] = ''
                        break

    return "".join(battle_field)