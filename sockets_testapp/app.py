from flask import Flask, render_template, session
from flask.ext.socketio import SocketIO, emit
import random

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update', namespace='/test')
def test_message(message):
    emit('updateRes', {'speed': random.randint(0,100), 'laptime' : random.randint(0,1000)})


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
