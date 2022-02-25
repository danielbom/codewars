# https://www.codewars.com/kata/salesmans-travel/train/python
# My solution
def travel(r, zipcode):
    addresses = [a.split()[:-2] for a in r.split(",") if zipcode.split() == a.split()[-2:]]
    return "%s:%s/%s" % (zipcode,
        ",".join(" ".join(a[1:]) for a in addresses),
        ",".join(i[0] for i in addresses))

# ...
import re
def travel(r, zipcode):
    res = [(m.group(2), m.group(1)) for m in re.finditer(r'(\d+) ([^,]+) ([A-Z][A-Z] \d{5})', r) if zipcode == m.group(3)]
    return '{}:{}/{}'.format(zipcode, ','.join(a[0] for a in res), ','.join(a[1] for a in res))

# ...
from collections import defaultdict
from re import compile, match

REGEX = compile(r'(?P<num>\d+) (?P<adr>.+) (?P<st_zip>[A-Z]{2} \d{5})')

def travel(addresses, zipcode):
    by_zipcode = defaultdict(lambda: defaultdict(list))
    for address in addresses.split(','):
        m = match(REGEX, address).groupdict()
        by_zipcode[m['st_zip']]['adr'].append(m['adr'])
        by_zipcode[m['st_zip']]['num'].append(m['num'])
    result = by_zipcode[zipcode]
    return '{}:{}/{}'\
        .format(zipcode, ','.join(result['adr']), ','.join(result['num']))

