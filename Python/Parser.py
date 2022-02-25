import re

class Token:
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"Token({self.tag},{self.value})"

class Lexer:
    TOKEN_TYPES = [
        (r'[1-9]+[_0-9]+[0_9]|[0-9+]', 'INTEGER'),
        (r'[0-9]+e[0-9]+', "EXP_INTEGER"),
        (r'[0_9]+\.[0-9]+', "REAL"),
    ]

    def __init__(self):
        pass

class Laxer:
    def __init__(self):
        pass

class ElementNode:
    def __init__(self):
        pass

class GroupingNode:
    def __init__(self):
        pass
