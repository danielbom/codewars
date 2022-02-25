# https://www.codewars.com/kata/regex-validate-pin-code/train/python
# My solution
def validate_pin(pin):
    return (len(pin) in (4,6)) and pin.isdigit()

# ...
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# ...
import re
def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))

# ...
import re
def validate_pin(pin):
  return re.search('^(\d{4}|\d{6})$', pin) != None 