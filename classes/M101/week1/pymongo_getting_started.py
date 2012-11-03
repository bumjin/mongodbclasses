import pymongo 
from pymongo import Connection

connection = Connection('localhost', 27017)

db = connection.test

names = db.names

user = names.find_one()

print user['name']

