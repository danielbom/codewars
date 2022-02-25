# https://www.codewars.com/kata/is-he-gonna-survive/train/python
# My solution
def hero(bullets, dragons):
    return bullets - (dragons * 2) >= 0
# ...
def hero(bullets, dragons):
    return bullets >= dragons * 2

