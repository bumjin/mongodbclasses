import pymongo
import sys

def main():
	connection = pymongo.Connection("mongodb://localhost", safe=True)

	db = connection.m101
	funnynumbers = db.funnynumbers

	number = {
		'num' : [3,6,9]
	}
	
	funnynumbers.insert(number)

	hw1 = db.hw1

	homework = {
		'mission' : 'using restore'
	}
	
	hw1.insert(homework)


main()