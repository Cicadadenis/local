from bottle import route, run

@route('/first-page')
def first_page():
	return '<H1 align="centre">Cicada_3301 !</H1>'
	
run(host='git@github.com:bednakovdenis/local.git', port=8080, debug=True)
