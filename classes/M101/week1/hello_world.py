import bottle

@bottle.route('/')
def home_page():
	return "<html><head></head><body>Hello World!</body></html>"

@bottle.route('/testpage')
def test_page():
	return "this is test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)	
