from logging import DEBUG
from flask import Flask
from flask.templating import render_template



app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1>Hello, Flask!</h1>"

@app.route("/nome/<nome>")
def nome(nome):
    return f"<h1>Hello, {nome}!!!!!!</h1>"


@app.route("/")
def home():
    return render_template("index.html", conteudo="Hello Jinja2", x=4)

if __name__ == "__main__":
    app.run(debug=True)

