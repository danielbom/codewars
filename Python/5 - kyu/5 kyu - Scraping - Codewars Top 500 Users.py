# https://www.codewars.com/kata/scraping-codewars-top-500-users/train/python
# My solution
import requests
from bs4 import BeautifulSoup

URL = 'https://www.codewars.com/users/leaderboard'

class User(object):
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan
        self.honor = honor

class Leaderboard(object):
    def __init__(self, pos={}):
        self.position = pos

def create_user(text):
    elem = list(text.children)
    name = list(elem[1].children)[1].text
    clan = elem[2].text
    honor = int(elem[3].get_text().replace(',',""))
    return User(name, clan, honor)
    
def solution():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find_all('tr')[1:]
    return Leaderboard({i+1: create_user(u) for i, u in enumerate(table)})