import re

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
        return "{}-{}".format(self.element, num)     
    def __repr__(self):
        return str(self)
        
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
        return str(self.children)
        # return "{}{}{}{}".format(self.symbol, ''.join(str(child) for child in self.children), self.closing_symbol(), num)
    def __repr__(self):
        return str(self)

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
        print("\n\tParsed end")
        print(self.formula)
        res = self.formula.get_atoms_dict()
        print(self.formula)
        return res

def parse_molecule (formula):
    parser = ChemicalParser(formula)
    return parser.parse()


molecula = "H2O(AlC)5{D(H2[BrCl]8)2}3"
print(parse_molecule(molecula))