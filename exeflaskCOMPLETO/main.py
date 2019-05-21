from flask import Flask,render_template, request
from funcionario import *
from datetime import datetime
import psycopg2
from flask import session


app = Flask(__name__) 

@app.route('/trataform',methods=["POST","GET"])
def trataform():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        depto = int(request.form["departamento"])
        cod=int(request.form["id"])

        f = Funcionario(nome,email)
        f.departamento = depto
        fdao = funcionarioDao()
        
        if (cod):
            f.id=cod
            
        fdao.salvar(f)

        return render_template('home.html')

    return render_template('form.html')



@app.route('/lista')
def lista():
    fdao = funcionarioDao().listar()

    return render_template('tela.html',flistar=fdao)


@app.route('/excluir/<id>')
def excluir(id):
    id=int(id)
    fdao = funcionarioDao()
    fdao.excluir(id)
    flistar = fdao.listar()
    return render_template('tela.html',flistar=flistar)



@app.route('/editar/<id>')

def editar(id):
    fdao = funcionarioDao()
    f = fdao.buscar(id)
    nome = f.nome
    email = f.email
    idDepartamento = f.departamento
    return render_template('editar.html',nome=nome,email=email,idDepartamento=idDepartamento,id=id)


@app.route('/login')
def login(): 
    
    
    session['nome']=



if __name__ == '__main__':
    app.run(debug = True)


"""
@app.before_first
def before_first_request(): 
    print('before_first_request')

@app.before_request
def before_request():
    print(request.path)
    print('before_request')

@app.after_request
def after_request(response):
    print('after_request')
    return response
"""

    
