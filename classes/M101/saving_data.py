import pymongo
import sys

def main():
	connection = pymongo.Connection("mongodb://localhost", safe=True)

	db = connection.m101
	people = db.people

	person = {
		'name' : 'Barack Obama', 'role' : 'President',
		'address':{
			'address1' : 'The White House',
			'street'	: '1600 Penssylvania Avenue',
			'state'	: 'DC',
			'city'	:	'Washington'
		},
		'interests'	:	['govenment', 'basketball', 'the middle east'

		]

	}
	
	people.insert(person)


main()