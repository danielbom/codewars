#
# My solution
def toJadenCase(string):
    return ' '.join(map(str.capitalize,string.split()))

# Other ways
import string
def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)

# ...
import string
toJadenCase = string.capwords

# ...
from string import capwords as toJadenCase