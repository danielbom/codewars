# https://www.codewars.com/kata/kebabize/train/python
# My solution
import re

def kebabize(string):
    return "-".join(
        map(lambda x: x.lower(), 
            re.findall("[A-Z][a-z]+|[a-z]+|[A-Z]",
            re.sub("\d", "", string)) ) )

# And
import re

def kebabize(string):
    return "-".join(
        re.findall("[A-Z][a-z]+|[a-z]+|[A-Z]",
        re.sub("\d", "", string))).lower()

# ...
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

# ...
import re
def kebabize(s):
    s = ''.join([i for i in s if not i.isdigit()])
    kebablist = filter(None, re.split("([A-Z][^A-Z]*)", s))
    return "-".join(x.lower() for x in kebablist)

# ...
import re
def kebabize(string):
    return re.sub(r'(?!^)([A-Z])', r'-\1', re.sub('\d', '', string)).lower()

# ...
import re
def kebabize(string):
    return re.sub(r'\B([A-Z])', r'-\1', re.sub('\d', '', string)).lower()

# ...
import re

def kebabize(string):
    return re.sub(
        '[0-9]',
        '',
        re.sub('[A-Z]', lambda m: '-' + m.group().lower(), string)
    ).lstrip('-')