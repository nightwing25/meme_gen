from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape 
import requests
from bs4 import BeautifulSoup as bs 
import subprocess
import re
from datetime import datetime
import os

app = Flask(__name__)#initalize flask

#@app.route("/")#after the sumbit the form action is set to go here
#def Find_meme():#show template html
#    return render_template("frontpage.html")

@app.route("/",methods=["POST","GET"])
def Main_page():
    result = None
    if request.method == 'POST':
        user = request.form.get("nm")
        result = meme_funct(user)
    return render_template("frontpage.html",result=result)

def meme_funct(meme):
    url = f"https://api.apileague.com/search-memes?keywords={meme}&number=1"
    #api_key = os.getenv("SECRET_API_KEY")
    #if api_key is None:
    #    print("no api key was found")
    #else:
    headers = {
        'x-api-key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

