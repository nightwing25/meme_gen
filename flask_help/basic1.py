from flask import render_template,request,url_redirect
from flask import Flask

#create initializer 
app = Flask(__name__)

#create route 
@app.route("/")
def index():
    return 
#in the retturn we can hard code html here or just text


if __name__ == "__main__":
    app.run(debug=True)
#app.run(host,port,debug,options)
