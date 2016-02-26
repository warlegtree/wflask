#!/usr/bin/env python
#import render
from flask import Flask, render_template
# import request
from flask import request
#import redirect
from flask import redirect
#import abort
from flask import abort
#import response
from flask import make_response
# use the flask-scripit 
from flask.ext.script import Manager
# import bootstrap
from flask.ext.bootstrap import Bootstrap



app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

#index
@app.route('/')
def index():
    return render_template('index.html')

#request and response
@app.route('/request')
def req():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

#User, dynamic
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

#redirect
@app.route('/rd')
def rd():
    return redirect('http://www.baidu.com')

#abort
@app.route('/user/<id>')
def get_usr(id):
    user = load_user(id)
    if not user:
 	 abort(404)
    return '<h1> Hello, %s</h1>' % user.name

#make_response
@app.route('/ck')
def makere():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
   manager.run()


