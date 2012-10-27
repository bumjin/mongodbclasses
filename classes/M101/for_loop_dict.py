

person = {'name':'bumjin','favorite_color':'blue',
		'hair':'black','interests' : 
			['cycling', 'running', 'biking']}

for key in person:	#iterate

	if (key == 'interests'):
		print "interests...."
		for interest in person[key]:
			print "\tinterest is "+interest

	else:
		print "key is "+key+" value is "+person[key]
