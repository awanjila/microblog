from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Wanjila'} #fake user
	posts=[
	{
		'author':{'nickname':'Wanjila'},
		'body':'Beautiful Day in portland'
	},
	{

        'author': {'nickname': 'Susan'}, 
        'body': 'The Avengers movie was so cool!'
	},
	{

        'author': {'nickname': 'Babu'}, 
        'body': 'You have to stop watching porn!'
	}
	]

	return render_template('index.html', 
							title='Home',
							user=user,
							posts=posts)