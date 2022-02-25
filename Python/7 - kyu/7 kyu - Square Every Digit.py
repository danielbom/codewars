# https://www.codewars.com/kata/square-every-digit/train/python
# My solution
def square_digits(num):
    return int(''.join(map(lambda c: str(int(c)**2),str(num))))

# Other ways
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
    