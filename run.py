import random
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/competition')
def competition():
	return render_template('competition.html', speed = 0)

@app.route('/speed')
def speed():
	return render_template('speed.html', speed = 0)

@app.route('/asyncSpeed')
def asyncSpeed():
	#dummy_speed = 12
	#return str(dummy_speed)
	return str(random.randint(0,25))

if __name__ == '__main__':
    app.run(debug=True)