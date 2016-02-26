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
#moment
from flask.ext.moment import Moment
#import datetime
from datetime import datetime




app = Flask(__name__)
moment = Moment(app)
manager = Manager(app)
bootstrap = Bootstrap(app)

#index
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

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

#error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#make_response
@app.route('/ck')
def makere():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
   manager.run()


