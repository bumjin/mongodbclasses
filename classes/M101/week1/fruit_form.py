import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple', 'banana', 'grape', 'peach', 'pear']
#	return bottle.template('hello_world', username='bumjin', things=mythings)
	return bottle.template('hello_world', {'username':'bumjin',
										 'things':mythings})

@bottle.post('/favorite_fruit')
def favorite_fruit():
	fruit = bottle.request.forms.get('fruit')
	
	if( fruit == None or fruit == ""):
		fruit = "No Fruit Selected"

	bottle.response.set_cookie('fruit', fruit)
	bottle.redirect('/show_fruit')

@bottle.route('/show_fruit')
def show_fruit():
	fruit = bottle.request.get_cookie('fruit')
	#return bottle.template('fruit_selection', fruit=fruit)
	return bottle.template('fruit_selection.tpl', {'fruit': fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8080)