from flask import Flask, request, redirect, flash
from flask import Flask, render_template
from flask.helpers import url_for
from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, current_user, LoginManager, logout_user


app = Flask(__name__)

DB_NAME = "database.db"

from models import User, Task

app.config['SECRET_KEY'] = 'IFSC@TUB'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

#configurar o login manager - se a rota tem o login_required ele redireciona para a pagina de login
login_manager = LoginManager()
login_manager.login_view='login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

with app.app_context():
    db.create_all()

### Rotas ###

@app.route("/" , methods=["POST", "GET"])
@login_required
def home():
    if request.method == "POST":
        if request.form.get("save"):
            for task in current_user.tasks:
                if request.form.get("c"+ str(task.id))=="clicked":
                    task.complete = True
                else:
                    task.complete = False
                db.session.commit()
        elif request.form.get("newTask"):
            nameTask = request.form.get("nova")
            if len(nameTask)>2:
                current_user.tasks.append(Task(name=nameTask, complete=False))
                db.session.commit()
                flash('Nova tarefa adicionada', category='sucess')
            else:
                flash('Nome da tarefa tem que ter mais de 2 digitos', category='error')
    return render_template("home.html", user=current_user, form=request.form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email= request.form.get('email')
        senha= request.form.get('senha')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, senha):
                flash('Login efetuado com sucesso', category='sucess')
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                flash('Senha incorreta', category='error')
        else:
            flash('Usuário não cadastrado', category='error')

    return render_template("login.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

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
        
    return render_template("signup.html", form=request.form)

if __name__ == "__main__":
    app.run(debug=True)