from flask import Flask, request, redirect, flash
from flask import Flask, render_template
from flask.helpers import url_for
from config import db
from werkzeug.security import generate_password_hash


app = Flask(__name__)

DB_NAME = "database.db"

from models import User

app.config['SECRET_KEY'] = 'IFSC@TUB'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

with app.app_context():
    db.create_all()

### Rotas ###

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=='POST':
        nome=request.form.get('nome')
        email=request.form.get('email')
        login=request.form.get('login')
        senha1=request.form.get('senha1')
        senha2=request.form.get('senha2')

        if senha1 != senha2:
            flash('senhas diferentes', category='error')
        elif len(login)<3:
            flash('login deve ter mais de  3 caracteres', category='error')
        else:
            senha_hash = generate_password_hash(senha1)
            user = User(name=nome, email=email, login=login, password=senha_hash)
            db.session.add(user)
            db.session.commit()
            flash('Usuario cadastrado', category='sucess')
            return redirect(url_for('login'))
        
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)