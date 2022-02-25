# https://www.codewars.com/kata/rot13-1/train/python
# My solution
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    l = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    u = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    trans = dict(zip(string.ascii_letters, l + u))
    return "".join(trans.get(l, l) for l in message)

# And
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    l = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    u = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    return message.translate(string.maketrans(string.ascii_letters, l + u))

# ...
import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)

# ...
import string

def rot13(message):
    return message.encode("rot13")
    #oh snap

# ...
import string
from string import maketrans, lowercase as lc, uppercase as uc

def rot13(message):
    tran = maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
    return message.translate(tran)
# ...