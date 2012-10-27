import pymongo
import sys

def main():
	connection = pymongo.Connection("mongodb://localhost", safe=True)

	db = connection.test
	users = db.users

	j = [{'firstname':'bumjin', 'last_name': 'park'}]
	try:
		users.insert(j)
	except:
		print "insert failed:", sys.exc_info()[0]

	print j
	try:
		users.insert(j)
	except:
		print "insert failed:", sys.exc_info()[0]

main()		