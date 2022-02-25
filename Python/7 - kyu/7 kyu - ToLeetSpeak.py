# https://www.codewars.com/kata/toleetspeak/train/python
# My solution
T = {
  'A' : '@',
  'B' : '8',
  'C' : '(',
  'E' : '3',
  'G' : '6',
  'H' : '#',
  'I' : '!',
  'L' : '1',
  'O' : '0',
  'S' : '$',
  'T' : '7',
  'Z' : '2', 
}
def to_leet_speak(str):
    return ''.join(map(lambda x: T.get(x, x), str))

def to_leet_speak(str):
    return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))