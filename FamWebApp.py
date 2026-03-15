#https://www.tutorialspoint.com/flask/flask_routing.html
#file:///home/nightwing/app_dev/webdev/info.html
from flask import Flask,render_template,url_for,request,redirect
#from flask_sqlalchemy import SQLAlchemy#how to use again ....
from markupsafe import escape #whats this for again
import requests
from bs4 import BeautifulSoup as bs 
import subprocess
import re
from datetime import datetime

#flask --app (filename).py run 

#simple application document as you go
app = Flask(__name__) #always initialize app like so 

@app.route('/success/<name>')#when user goes to / part of the what should they see
def success(name):#what the user will see here 
    return 'success %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('succes',name = user))

if __name__ == '__main__':
    app.run(debug=True)#if its this file being ran do code
