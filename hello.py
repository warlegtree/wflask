#!/usr/bin/env python

from flask import Flask
# import request
from flask import request

app = Flask(__name__)

#index
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#request and response
@app.route('/request')
def req():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

#User, dynamic
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__=='__main__':
    app.run(debug=True)
