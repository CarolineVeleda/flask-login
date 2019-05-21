import psycopg2

class Funcionario:
    def __init__(self,nome,email):

        self._nome = nome
        self._email = email

    def _get_nome(self):
        return self._nome
    
    def _get_email(self):
        return self._email

    def _get_id(self):
        return self._id
    
    def _get_departamento(self):
        return self._departamento
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_email(self, email):
        self._email = email
    
    def _set_id(self, id):
        self._id = id
    
    def _set_departamento(self, departamento):
        self._departamento = departamento

    nome = property(_get_nome,_set_nome)
    email = property(_get_email,_set_email)
    id = property(_get_id,_set_id)
    departamento = property(_get_departamento,_set_departamento)



class funcionarioDao:

    def __init__(self):
        self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from funcionario')
            for linha in cursor.fetchall():
                f = Funcionario(linha[1],linha[2])
                f.id=linha[0]
                v.append(f)
            
        cursor.close()
        return v
    

    
    def salvar(self, f):

        verifica=hasattr(f, 'id')

        if (verifica):
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('UPDATE Funcionario SET nome = %s, email = %s, idDepartamento = %s WHERE idFuncionario = %s',(f.nome,f.email,f.departamento,int(f.id)))
                con.commit()
                cursor.close()


        else:
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into Funcionario (nome,email,idDepartamento) values (%s,%s,%s) RETURNING idFuncionario', (f.nome,f.email,f.departamento))
                id = (cursor.fetchone())[0]
                con.commit()
                f.cod = int(id)
                cursor.close()



    def buscar(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Funcionario WHERE idFuncionario = %s',[cod])
        b = cursor.fetchone()
        f = Funcionario(b[1],b[2])
        f.departamento = b[3]
		
        f.id = int(b[0])
        cursor.close()
        return f


    def excluir(self,id):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM Funcionario WHERE idFuncionario = %s',[id])
        con.commit()
        cursor.close()


    def login(self,nome,email):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Funcionario WHERE login = %s and senha= %s ',(nome,email))
        l = cursor.fetchone()
        f = Funcionario(l['nome'],l['email'],l['senha'],l['admin'],l['login'])






#f.departamento=d
#d.funcionario=f

#print(fdao.listar())
#print(f.departamento.id)

f1 = funcionarioDao()
#f = f1.buscar(1)
#print(f.nome)
#print(f.email)
#print(f.departamento)

#depto nao precisa de gerente



 





