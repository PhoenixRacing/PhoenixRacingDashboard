import random
import time
import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)

class Time(object):
	'''A Class that handles and formats time that I totally stole
	from Allen Downey's book... '''
	def __init__(self, minute=0, second=0):
		self.minute = minute
		self.second = second
	def __str__(self):
		return '%.2d:%.2d' % (self.minute, self.second)

def int_to_time(seconds):
	'''More stuff that I took from Allen Downey's book'''
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/competition')
def competition():
	return render_template('competition.html', speed = 0)

@app.route('/asyncSpeed')
def asyncSpeed():
	#dummy_speed = 12
	#return str(dummy_speed)
	return str(random.randint(0,25))

format = '%M:%S';

@app.route('/curr_time')
def curr_time():
	'''This function returns the current minutes and seconds. 
	Later we will feed it dummy data'''
	curr_t = datetime.datetime.now()
	return curr_t.strftime(format)

@app.route('/prev_time')
def prev_time():
	'''This function assumes that the previous time is stored as an integer 
	number of seconds'''
	prev_t = int_to_time(134)
	return str(prev_t)

if __name__ == '__main__':
    app.run(debug=True)