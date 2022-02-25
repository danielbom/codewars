# https://www.codewars.com/kata/driving-licence/train/python
# My solution
import datetime
def driver(data):
    dict_data = dict(zip("fname mname lname date sex".split(" "),data))
    if len(dict_data["date"].split("-")[1]) > 3:
        dict_data["date"] = datetime.datetime.strptime(dict_data["date"], '%d-%B-%Y').date()
    else:
        dict_data["date"] = datetime.datetime.strptime(dict_data["date"], '%d-%b-%Y').date()
    
    return "{:9<5s}{:s}{:02d}{:02d}{:s}{:9<2s}9AA".format(
        dict_data["lname"].upper()[:5],
        str(dict_data["date"].year)[-2],
        dict_data["date"].month + (50 if dict_data["sex"] == "F" else 0),
        dict_data["date"].day,
        str(dict_data["date"].year)[-1],
        dict_data["fname"][0] + (dict_data["mname"][0] if dict_data["mname"] else ""))
# And
import datetime

def driver(data):
    fname, mname, lname, date, sex = data
    if len(date.split("-")[1]) > 3:
        date = datetime.datetime.strptime(date, '%d-%B-%Y').date()
    else:
        date = datetime.datetime.strptime(date, '%d-%b-%Y').date()
    
    return "{:9<5s}{:s}{:02d}{:02d}{:s}{:9<2s}9AA".format(
        lname.upper()[:5],
        str(date.year)[-2],
        date.month + (50 if sex == "F" else 0),
        date.day,
        str(date.year)[-1],
        fname[0] + (mname[0] if mname else ""))
# ...
from datetime import datetime
def driver(data):
    first, middle, last, dob, gender = data
    try:
        d = datetime.strptime(dob, '%d-%b-%Y')
    except ValueError:
        d = datetime.strptime(dob, '%d-%B-%Y')

    return '{:9<5}{[2]}{:0>2}{:0>2}{[3]}{[0]}{[0]}9AA'.format(
        last[:5].upper(),
        str(d.year),
        d.month + (50 if gender == 'F' else 0),
        d.day,
        str(d.year),
        first,
        middle if middle else '9')
# ...
def driver(data):
    months = ['nul','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    name   = (data[2].upper() +'99999')[:5]
    decade = data[3][-2]
    month  =  months.index(data[-2][3:6]) +(50 if data[-1] == 'F' else 0)
    
    date   = data[-2][:2]
    year   = data[-2][-1]
    inits  = data[0][0] + (data[1][0] if data[1] else '9')
    
    return '{}{}{:02d}{}{}{}9AA'.format(name,decade,month,date,year,inits)