# https://www.codewars.com/kata/mexican-wave/train/python
# My solution
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
# ...
def wave(s):
    return [f'{s[:i]}{s[i].upper()}{s[i+1:]}' for i,x in enumerate(s) if x != ' ']
# ...
def wave(s):
    return [s[:i].lower() + s[i:].capitalize() for i in range(len(s)) if s[i] != " "]
