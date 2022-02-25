# https://www.codewars.com/kata/playing-with-passphrases/train/python
# My solution
import string

def play_pass(s, n):
    a = string.ascii_uppercase
    s = s.upper().translate(str.maketrans(a[-n:] + a[:-n], a))
    s = "".join(str(9 - int(ch)) if ch.isdigit() else ch for ch in s)
    return "".join(reversed([ch.lower() if i % 2 == 1 else ch for i, ch in enumerate(s)]))
# ...
import re
from string import ascii_lowercase as s
from string import ascii_uppercase as S

def play_pass(st, n):
    j = s + S
    st = re.sub(r'[0-9]',lambda i:str(9-int(i.group())) ,st.translate(str.maketrans(j, j[n:]+j[:n])))
    return "".join(j.upper() if i%2==0 else j.lower() for i,j in enumerate(st))[::-1]

# ...
from collections import deque

def play_pass(s, n):
    d = deque( chr(ord('A')+x) for x in range(26) )
    d.rotate(-n)
    return ''.join( d[ord(c)-ord('A')].lower() if c.isalpha() and i%2
                    else d[ord(c)-ord('A')] if c.isalpha()
                    else str(9-int(c)) if c.isdigit()
                    else c for i,c in enumerate(s) )[::-1]