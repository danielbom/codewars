# https://www.codewars.com/kata/603a1f484222c3002b3fbf35/train/python
# My solution
primitives = [str, int, float, bool]

class Array(list):
    def __init__(self, typ, length=None):
        self.typ = typ
        self.length = length
        if length is not None:
            factory = typ if typ in primitives else lambda: None
            for _ in range(length):
                self.append(factory())
    
    def __getitem__(self, index):
        if self.length is None:
            return Array(self.typ, index)
        return super().__getitem__(index)
    
    def __setitem__(self, index, value):
        if type(value) is not self.typ:
            if self.typ in primitives:
                raise TypeError()
            if value is not None:
                raise TypeError()

        super().__setitem__(index, value)
