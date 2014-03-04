import random
import time
import datetime

from flask import Flask, render_template, session
from flask.ext.socketio import SocketIO, emit
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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

@socketio.on('update', namespace='/test')
def test_message(message):
	emit('updateSpeed', {'speed': random.randint(0, 25)})

format = '%M:%S';

@socketio.on('update ptime', namespace='/test')
def test_ptime(message):
	prev_t = datetime.datetime.now();
	emit('updatePtime', {'prev': str(prev_t.strftime(format))})

@socketio.on('current time', namespace='/test')
def test_ctime(message):
	curr_t = datetime.datetime.now();
	emit('updateCtime', {'curr': str(curr_t.strftime(format))})


#@app.route('/curr_time')
#def curr_time():
#	'''This function returns the current minutes and seconds. 
#	Later we will feed it dummy data'''
#	curr_t = datetime.datetime.now()
#	return curr_t.strftime(format)


if __name__ == '__main__':
    socketio.run(app)