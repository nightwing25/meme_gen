#build urls dynamically using vars apart of the rule
from flask import Flask
app Flask(__name__)

@app.route('/hello/<name>')#whats supplied to the <name> variable will be sent to the function 
def hello_name(name):
    return f" hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
