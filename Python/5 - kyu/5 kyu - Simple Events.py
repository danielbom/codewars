# https://www.codewars.com/kata/simple-events/train/python
# My solution
class Event():
    handlers = set()
        
    def subscribe(self, function):
        self.handlers.add(function)
    
    def unsubscribe(self, function):
        self.handlers.remove(function)
    
    def emit(self, *args, **kargs):
        for f in self.handlers: f(*args, **kargs)


