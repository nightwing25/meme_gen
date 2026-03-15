from flask import Flask
#create flask news web app using flask api 
#$ flask --app app_name_without_py run
# * Serving Flask app 'hello'
# * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

app = Flask(__name__)

@app.route("/")
@app.route("/main_page")
def news_app():
    return render_template("news_page.html")




