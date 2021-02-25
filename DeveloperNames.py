# developer Names by using flask
#import flask

from flask import Flask,request,render_template,jsonify,escape
from rich import print
app=Flask(__name__)

developerName=('Sathish','Suresh')

@app.route('/')
def Index():
    return "Hi Hello"
@app.route('/Developer/')
@app.route('/Developer/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

