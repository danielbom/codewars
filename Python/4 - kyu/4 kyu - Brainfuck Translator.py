# https://www.codewars.com/kata/brainfuck-translator/train/python
# My solution
import re

DICT_TRANSLATOR = {
    ",": "*p = getchar();\n",
    ".": "putchar(*p);\n",
    "[": "if (*p) do {\n",
    "]": "} while (*p);\n"
}
PLUS_MINUS = ['+', '-']
BIG_SMALL = [">", "<"]
VALUE = "*p %c= %d;\n"
POINTER = "p %c= %d;\n"

def simplify_code(code):
    # remove comments
    code = re.sub(r'[^+-<>,.\[\]]', '', code)
    # remove redundant code
    before = ''
    while code != before:
        before = code
        code = re.sub(r'\+-|-\+|<>|><|\[\]', '', code)
    return code

def sum_signals(code, i, n, signals):
    sum_ = 0
    while i < n and code[i] in signals:
        sum_ += 1 if code[i] == signals[0] else -1
        i += 1
    return sum_, i-1

def count_signal(code, i, n, signal):
    sum_ = 0
    while i < n and code[i] == signal:
        sum_ += 1
        i += 1
    return sum_, i-1

def translate(code):
    code_t = ""
    i = 0
    n = len(code)
    absl = abs
    while i < n:
        if code[i] in PLUS_MINUS:
            sum_, i = sum_signals(code, i, n, PLUS_MINUS)
            if sum_ != 0: code_t += VALUE % ('+' if sum_ > 0 else '-', absl(sum_))
        elif code[i] in BIG_SMALL:
            sum_, i = sum_signals(code, i, n, BIG_SMALL)
            if sum_ != 0: code_t += POINTER % ('+' if sum_ > 0 else '-', absl(sum_))
        elif code[i] in DICT_TRANSLATOR.keys():
            sum_, i = count_signal(code, i, n, code[i])
            code_t += DICT_TRANSLATOR[code[i]] * sum_
        i += 1
    return code_t

def indent(code):
    i_spaces = 0
    code = code.split("\n")
    for i in range(len(code)):
        if "}" in code[i]: i_spaces -= 1
        code[i] = "  " * i_spaces + code[i]
        if "{" in code[i]: i_spaces += 1
    return "\n".join(code)

def test_brackets(code):
    # check braces status
    braces = re.sub('[^\[\]]', '', code)
    while braces.count('[]'):
        braces = braces.replace('[]', '')
    return braces
    
def brainfuck_to_c(source_code):
    return "Error!" if test_brackets(source_code) else indent(translate(simplify_code(source_code)))

# ...
import re
def brainfuck_to_c(source):
    # remove comments
    source = re.sub('[^+-<>,.\[\]]', '', source)
    
    # remove redundant code
    before = ''
    while source != before:
        before = source
        source = re.sub('\+-|-\+|<>|><|\[\]', '', source)
    
    # check braces status
    braces = re.sub('[^\[\]]', '', source)
    while braces.count('[]'):
        braces = braces.replace('[]', '')
    if braces:
        return 'Error!'
    
    # split code into commands
    commands = re.findall('\++|-+|>+|<+|[.,\[\]]', source)
    
    # translate to C
    output = []
    indent = 0
    for cmd in commands:
        if cmd[0] in '+-<>':
            line = ('%sp %s= %s;\n' %
                ('*' if cmd[0] in '+-' else '',
                 '+' if cmd[0] in '+>' else '-',
                 len(cmd)))
        elif cmd == '.':
            line = 'putchar(*p);\n'
        elif cmd == ',':
            line = '*p = getchar();\n'
        elif cmd == '[':
            line = 'if (*p) do {\n'
        elif cmd == ']':
            line = '} while (*p);\n'
            indent -= 1
        output.append('  ' * indent + line)
        if cmd == '[':
            indent += 1
    
    return ''.join(output)

# ...
def brainfuck_to_c(s):
    s = ''.join(c for c in s if c in '.,<>[]-+')

    pairs = '<> >< -+ +- []'.split()
    while any(p in s for p in pairs):
        for w in pairs: s = s.replace(w, '')
        
    r, depth, l, i = '', 0, ' ', 1
    for c in s:
        if c == l and c in '<>+-': 
            i += 1
            continue
        if l in '<>+-': r += cmd(depth, l, i)
        if c == ']': depth -= 2
        if c in '.,[]': r += cmd(depth, c)
        if c == '[': depth += 2
        if depth < 0: break
        i, l = 1, c
            
    return 'Error!' if depth else r + (cmd(depth, l, i) if l in '<>+-' else '')

def cmd(depth, c, i=None):
    return ' ' * depth + {'<':'p -=', '>':'p +=', '+':'*p +=', '-':'*p -=', 
                          '.':'putchar(*p);', ',':'*p = getchar();', 
                          '[':'if (*p) do {', ']':'} while (*p);'}[c]  + (' {};'.format(i) if i else '') +'\n'