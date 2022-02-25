# https://www.codewars.com/kata/vasya-clerk/train/python
# My solution
def tickets(people):
    notes = {25: 0, 50: 0, 100: 0}
    for note in people:
        note_record = note
        while notes[50] > 0 and note > 50:
            note -= 50
            notes[50] -= 1
        while notes[25] > 0 and note > 25:
            note -= 25
            notes[25] -= 1
        if note > 25:
            return "NO"
        notes[note_record] += 1
    return "YES"
# ...
def tickets(people):
    till = {100.0: 0, 50.0: 0, 25.0: 0}

    for paid in people:
        till[paid] += 1
        change = paid-25.0

        for bill in (50, 25):
            while (bill <= change and till[bill] > 0):
                till[bill] -= 1
                change -= bill

        if change != 0:
            return 'NO'

    return 'YES'
# ...
def tickets(people, cost=25, bills=[100, 50, 25]):
    count = dict.fromkeys(bills, 0)
    for change in people:
        count[change] += 1
        change -= cost
        for bill in bills:
            if change >= bill:
                c = min(change // bill, count[bill])
                count[bill] -= c
                change -= c * bill
        if change:
            return "NO"
    return "YES"
# ...
from collections import Counter

def tickets(people):

    bills = Counter({ 25 : 0, 50 : 0, 100 : 0 })
    required = {
        50  : [ Counter({ 25 : 1 }) ],
        100 : [ Counter({ 25 : 1, 50 : 1 }), Counter({ 25 : 3 }) ],
    }
    
    def check_required(person):
        for require in required[person]:
            if bills & require == require:
                bills.subtract(require)
                return True
        return False

    for person in people:
        bills[person] += 1
        if person > 25 and not check_required(person):
            return "NO"
    
    return "YES"
# ...
def tickets(people):
    a = people.count(25)
    b = people.count(50)
    c = people.count(100)
    if (b-a <= 0) and ((a-b-min(b,a-b))/3 + min(b,a-b) >= c):
        return 'YES'
    else:
        return 'NO'