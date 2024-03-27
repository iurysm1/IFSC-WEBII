from flask import Flask
from flask.templating import render_template


app = Flask(__name__)



### Rotas ###
@app.route("/")
def home():
    return render_template("home.html")



@app.route("/login")
def login():
    return render_template("login.html")

if __name__== "__main__":
    app.run(debug=True)