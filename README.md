PhoenixRacingDashboard
======================

The driver interface for the Olin College MiniBaja car.

This app contains both the dashboard for competition and for test driving. 

The app uses Flask with a virtual environment (Note: this implementation of Flask requires python 2.x) and FlaskSocketIO for socket management. 

For further info on Flask, visit the [Flask Documentation](http://flask.pocoo.org/docs/).

For further info on FlaskSocketIO visit the [Tutorial](http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent) and the [Documentation](http://flask-socketio.readthedocs.org/en/latest/).

First Time Use
--------------

Install dependencies (Flask, FlaskSocketIO, etc.) on Ubuntu:

```
pip install -r requirements.txt
```

To Run the Application on Local Server
-------------
Assuming default version of python is 2.x:
```
python run.py
```