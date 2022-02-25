# https://www.codewars.com/kata/molecule-to-atoms/train/python
# My solution
import re

def parse_molecule(formula):
    # Algumas expressoes regulares
    elem = r"[A-Z][a-z]?"
    elem_num = r"[A-Z][a-z]?[1-9]*"

    # Altero a formula
    i = 0
    form = formula[:]
    while i < len(form):
        if form[i] in ['(', '[', '{']:
            count = 1
            inicio = i
            while count:
                i += 1
                if form[i] in ['(', '[', '{']:
                    count += 1
                elif form[i] in [')', ']', '}']:
                    count -= 1
            fim = i
            if form[fim+1].isdigit():
                form = form.replace(
                    form[inicio:fim+2], form[inicio+1:fim]*int(form[fim+1]))
            else:
                form = form.replace(form[inicio:fim+1], form[inicio+1:fim])
            i = inicio - 1
        i += 1

    # Crio o dicionario
    dic_elem = {}
    for i in set(re.findall(elem, form)):
        dic_elem[i] = 0

    for i in re.findall(elem_num, form):
        if i[-1].isdigit():
            num = ''.join(list(filter(str.isdigit, i)))
            dic_elem[i[:-len(num)]] += int(num)
        else:
            dic_elem[i] += 1

    return dic_elem

# ...
from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts

# ...
import re

#
# There's probably simpler ways to do this, but I thought this would be a cool
# way for me to learn about how to make a lexer and parser from scratch.
#

class Token(object):
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value
        
    def __repr__(self):
        return "Token({}, {})".format(self.tag, self.value)
    
    def __str__(self):
        return "{}: {}".format(self.tag, self.value)

class ChemicalLexer(object):
    TOKEN_TYPES = [
        (r'[A-Z][a-z]?', 'ELEMENT'),
        (r'[0-9]+',      'QUANTITY'),
        (r'\[|\(|\{',    'LEFT_GROUPING'),
        (r'\]|\)|\}',    'RIGHT_GROUPING'),
    ]
    def __init__(self, formula):
        self.formula = formula
        self.pos = 0
        self.token_types = [(re.compile(pattern), tag) for pattern, tag in self.TOKEN_TYPES]
    
    def token_gen(self):
        while self.pos < len(self.formula):
            error = True
            for regex, tag in self.token_types:
                match = regex.match(self.formula, self.pos)
                if match:
                    error = False
                    yield Token(tag, match.group(0))
                    self.pos = match.end(0)
                    break
                else:
                    continue
            if error:
                raise Exception("Syntax Error")

def add_dicts(dict1, dict2):
    totals = {}
    for key in dict1:
        totals.setdefault(key, 0)
        totals[key] += dict1[key]
    for key in dict2:
        totals.setdefault(key, 0)
        totals[key] += dict2[key]
    return totals

def scale_dict(d, scalar):
    return {k: scalar * v for k, v in d.items()}

class ElementNode(object):
    def __init__(self, element):
        self.type = 'element'
        self.element = element
        self.quantity = 1
        
    def __str__(self):
        num = '' if self.quantity == 1 else self.quantity
        return "{}{}".format(self.element, num)
        
class GroupingNode(object):
    def __init__(self, symbol = ''):
        self.type = 'grouping'
        self.symbol = symbol
        self.quantity = 1
        self.children = []
    
    def add(self, element):
        self.children.append(element)
        
    def last(self):
        try:
            return self.children[-1]
        except IndexError:
            return None
    
    def add_quantity(self, quantity):
        self.children[-1].quantity = quantity
    
    def closing_symbol(self):
        if self.symbol == '':
            return ''
        if self.symbol == '(':
            return ')'
        if self.symbol == '[':
            return ']'
        if self.symbol == '{':
            return '}'
    
    def get_atoms_dict(self):
        atoms = {}
        for child in self.children:
            if child.type == 'element':
                atoms.setdefault(child.element, 0)
                atoms[child.element] += child.quantity * self.quantity
            elif child.type == 'grouping':
                child_atoms = child.get_atoms_dict()
                atoms = add_dicts(atoms, scale_dict(child_atoms, self.quantity))
        return atoms                
    
    def __str__(self):
        num = '' if self.quantity == 1 else self.quantity
        return "{}{}{}{}".format(self.symbol, ''.join(str(child) for child in self.children), self.closing_symbol(), num)

class ChemicalParser(object):
    def __init__(self, formula):
        self.lexer = ChemicalLexer(formula)
        self.formula = GroupingNode()
        self.group_stack = []
    
    def current_group(self):
        try:
            return self.group_stack[-1]
        except IndexError:
            return self.formula
        
    def element(self, token):
        node = ElementNode(token.value)
        group = self.current_group()
        group.add(node)
    
    def quantity(self, token):
        node = self.current_group().last()
        if node:
            node.quantity = int(token.value)
        else:
            raise Exception("Missing Atom before quantifier {}".format(token.value))
    
    def left_grouping(self, token):
        node = GroupingNode(token.value)
        self.group_stack.append(node)
    
    def right_grouping(self, token):
        group = self.current_group()
        if group.closing_symbol() == token.value:
            node = self.group_stack.pop()
            group = self.current_group()
            group.add(node)
        else:
            raise Exception("Missing Grouping Symbol {}".format(group.closing_symbol()))
    
    def parse(self):
        for token in self.lexer.token_gen():
            if token.tag == 'ELEMENT':
                self.element(token)
            elif token.tag == 'QUANTITY':
                self.quantity(token)
            elif token.tag == 'LEFT_GROUPING':
                self.left_grouping(token)
            elif token.tag == 'RIGHT_GROUPING':
                self.right_grouping(token)
            else:
                raise Exception("Invalid Token!")
        if self.group_stack:
            raise Exception("Missing Grouping Symbol {}".format(self.current_group().closing_symbol()))
        return self.formula.get_atoms_dict()

def parse_molecule (formula):
    parser = ChemicalParser(formula)
    return parser.parse()

# ...
import re
from collections import Counter

def expand_str(m):
    return m.group(1) * int(m.group(2))

def parse_molecule (formula):
    formula = re.sub(r'\(([^\)]+)\)(\d+)',expand_str,formula)
    formula = re.sub(r'\[([^\]]+)\](\d+)',expand_str,formula)
    formula = re.sub(r'\{([^\}]+)\}(\d+)',expand_str,formula)
    formula = re.sub(r'([A-Z][a-z]?)(\d+)',expand_str,formula)
    m = re.findall(r'[A-Z][a-z]?',formula)
    return Counter(m)

# ...
import re, collections

def parse_molecule(formula):
    while True:
        m = re.search("[\[({](\w+)[\])}](\d+)", formula)
        if not m:
            break
        formula = re.sub(re.escape(m.group(0)), m.group(1) * int(m.group(2)), formula)
    
    while True:
        m = re.search("([A-Z][a-z]?)(\d+)", formula)
        if not m:
            break
        formula = re.sub(m.group(0), m.group(1) * int(m.group(2)), formula)
    
    return collections.Counter(re.findall("[A-Z][a-z]?", formula))

# ...
import collections
import re

def parse_molecule (formula):
    while any(c in formula for c in "({["):
        formula = re.sub(r'[([{]([^()\[\]{}]*)[)\]}](\d*)', lambda m: m.group(1) * int(m.group(2) or 1), formula)
    formula = re.sub(r'([A-Z][a-z]*)(\d+)', lambda m: m.group(1) * int(m.group(2)), formula)
    return collections.Counter(m.group() for m in re.finditer('[A-Z][a-z]*', formula))

# ...
exec """\nfrom collections import Counter as C; import re; from re import findall as fa\ndef parse_molecule(f):\n    cnts = C()\n    for el, c in fa(r'([A-Z][a-z]?|\\([^(]+\\)|\\[[^[]+\\]|\\{[^}]+\\})(\\d*)', f):\n        c = int(c) if c else 1\n        if el[0] in '{[(':\n            for k, v in parse_molecule(el[1:-1]).items(): cnts[k] += c * v\n        else:\n            cnts[el] += c\n    return cnts\n"""

# ...
from collections import defaultdict
from re import compile as reCompile

PATTERN = reCompile(r'([A-Z][a-z]*)([0-9]*)|([\(\[\{])|([\)\]\}])([0-9]*)')

def calc(iterator):
    ret = defaultdict(lambda: 0)
    for (atom, number, openBrace, closeBrace, braceNumber) in iterator:
        if atom:
            ret[atom] += int(number or 1)
        elif openBrace:
            for (atom, number) in calc(iterator).iteritems():
                ret[atom] += number
        elif closeBrace:
            if braceNumber:
                braceNumber = int(braceNumber or 1)
                for (atom, number) in ret.iteritems():
                    ret[atom] *= braceNumber
            break
    return ret

def parse_molecule(formula):
    return calc(iter(PATTERN.findall(formula)))

# ...
import re

def parse_molecule (formula):
    s = formula
    s = s.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')').replace('(', '+(')
    s = re.sub(r'([A-Z][a-z]*)', '+["\\1"]', s)
    s = re.sub(r'([0-9]+)', '*\\1', s)
    s = s.replace('(+', '(')
    result = eval(s.lstrip('+'))
    return {el: result.count(el) for el in set(result)}

