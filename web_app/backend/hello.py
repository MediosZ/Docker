import hug
import time

@hug.get('/birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())
    
@hug.get('/time')
def gettime():
    return time.asctime(time.localtime())