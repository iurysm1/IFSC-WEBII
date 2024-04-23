from flask import Flask, request, redirect, flash, jsonify
from flask import Flask, render_template
from flask.helpers import url_for
import json

from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, current_user, \
    logout_user

app = Flask(__name__)

DB_NAME = "database.db"

from models import User, Task, Fornecedor, Produto

app.config['SECRET_KEY'] = 'IFSC@TUB'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

#configurar o login_manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))

with app.app_context():
    db.create_all()

### Rotas ###

@app.route("/", methods=['GET', 'POST', 'PUT'])
@login_required
def home():
    
    if request.method == 'POST':
        if request.form.get("save"):
            for task in current_user.tasks:
                if request.form.get("c" + str(task.id)) == "clicked":
                    task.complete = True
                else:
                    task.complete = False
                db.session.commit()
        elif request.form.get("newTask"):
            name = request.form.get("nova")
            if len(name) > 2:
                current_user.tasks.append(Task(name=name, complete=False))  
                db.session.commit()
            else:
                flash("Nome da tarefa tem que ter mais de 2 letras!")
        elif request.form.get("edit"):
            fornecedores=Fornecedor.query.all()
            print("edit")
            id = request.form.get("productIdEdit")
            produto = db.session.get(Produto, id)
            produto.nome = request.form.get("productNameEdit")
            produto.preco = request.form.get("productPriceEdit")
            produto.estoque = request.form.get("productEstoqueEdit")
            for fornecedorAtual in fornecedores:
                if request.form.get("f"+str(fornecedorAtual.id))=="clicked":
                    produto.fornecedor_id=fornecedorAtual.id
                    print('entrou')
            print(produto.fornecedor_id)
            db.session.commit()
            flash("Produto Alterado.")
        elif request.form.get("newProduct"):
            nome=request.form.get("productName")
            preco=request.form.get("productPrice")
            estoque=request.form.get("productEstoque")
            fornecedor_id=None
            for fornecedorFor in Fornecedor.query.all():
                if request.form.get("f" + str(fornecedorFor.id)) == "clicked":
                    fornecedor_id=fornecedorFor.id

            if fornecedor_id is not None:  # Verifica se um fornecedor foi selecionado
                novo_produto = Produto(nome=nome, estoque=estoque, preco=preco, fornecedor_id=fornecedor_id)
                if not verificaProduto(novo_produto.nome):
                    db.session.add(novo_produto)
                    db.session.commit()
                    flash("Produto cadastrado.")
                else:
                    flash("O produto já existe!")
            else:
                flash("Selecione um fornecedor.")
        
            

    return render_template("home.html", user=current_user, produtos=Produto.query.all(), get_fornecedor_nome=get_fornecedor_nome, fornecedores=Fornecedor.query.all(), verificaProduto=verificaProduto, countFornecedores=Fornecedor.query.count())
    # "produtos=Produto.query.all()" -> para usar como uma variavel que pega todos os produtos e faz o laço FOR na pagina HOME
    # "get_fornecedor_nome=get_fornecedor_nome" passei a função para o template como uma variavel global

def get_fornecedor_nome(fornecedor_id):
        fornecedor = db.session.get(Fornecedor, fornecedor_id)
        
        if fornecedor:
            return fornecedor.razao_social
        else:
            return "Fornecedor não encontrado"
        #passa o parametro de um numero e retorna o fornecedor pelo parametro
def verificaProduto(produto):
    if Produto.query.filter_by(nome=produto).first():
        return True
    else:
        return False
    

  
    

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, senha):
                flash('Login feito com sucesso', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home'))
        else:
            flash('Email não existe.', category='error')

    return render_template("login.html", user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/signup", methods=['GET','POST'])
def signup():
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        login = request.form.get('login')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')

        if senha1 != senha2:
            flash('Senhas diferentes!', category='error')
        elif len(login) <3:
            flash('Login deve ter mais que 3 caracteres', category='error')
        else:
            senha_hash = generate_password_hash(senha1)
            user = User(name=nome, email=email, login = login,
                password=senha_hash)
            db.session.add(user)
            db.session.commit()
            flash('Conta criada com sucesso!', category='success')
            return redirect(url_for('login'))


    return render_template("signup.html", form=request.form)


@app.route("/delete-task", methods=['POST'])
def delete_task():
    task = json.loads(request.data)
    task_id = task['taskId']
    task = db.session.get(Task, task_id)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)

