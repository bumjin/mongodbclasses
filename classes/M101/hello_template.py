import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple', 'banana', 'grape', 'peach', 'pear']
#	return bottle.template('hello_world', username='bumjin', things=mythings)
	return bottle.template('hello_world', {'username':'bumjin',
										 'things':mythings})

bottle.debug(True)
bottle.run(host='localhost', port=8080)