# https://www.codewars.com/kata/design-a-simple-automaton-finite-state-machine/train/python
# My solution
class Automaton(object):
    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        state = 1
        for i in commands:
            if   state == 1: state = 2 if i == "1" else 1
            elif state == 2: state = 3 if i == "0" else 2
            else           : state = 2
        return state == 2
        
my_automaton = Automaton()

# ...
from functools import reduce
class Automaton(object):
    T = {1: {"0": 1, "1": 2},
         2: {"0": 3, "1": 2},
         3: {"0": 2, "1": 2}}

    def read_commands(self, commands):
        return reduce(lambda a,b: self.T[a][b], commands, 1) == 2

my_automaton = Automaton()

# ...
class State(object):

    def __init__(self, key, accept=False):
        self.key = key
        self.accept = accept
        
    def __str__(self):
        return str(self.key)
        
    def transition(self, symbol, transtable):
        try:
            return transtable[self.key][symbol]
        except:
            print "transtable is invalid!"
            return -1
            
    def isaccept(self):
        return self.accept

class Automaton(object):
    
    def __init__(self):
        self.states = []

    def setup(self, states, start, transtable):
        self.states = states
        self.start = start
        self.transtable = transtable

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        self.cur_state = self.start 
        for c in commands:
            self.cur_state = self.cur_state.transition(c, self.transtable)
        return self.cur_state.isaccept()
            
my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.
states = [State('q1'), State('q2', accept=True), State('q3')]
transtable = {'q1':{'0':states[0], '1':states[1]}, 'q2':{'0':states[2], '1':states[1]}, 'q3':{'0':states[1], '1':states[1]}}
my_automaton.setup(states, states[0], transtable)