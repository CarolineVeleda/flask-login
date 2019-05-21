Departamento (id, nome, idGerente)
 idGerente referencia Funcionario
Funcionario (id, nome, email, idDepartamento)
 idDepartamento referencia Departamento
Projeto (id, nome, dataPrevista)
FuncProj (idProjeto, idFuncionario)
 idFuncionario referencia Funcionario
 idProjeto referencia Projeto

 CREATE TABLE Departamento (
	idDepartamento serial,
	nome VARCHAR (150) NOT NULL,
	idGerente int,
	CONSTRAINT "idGerenteFK" FOREIGN KEY(idGerente)
		REFERENCES Funcionario(idFuncionario),
	CONSTRAINT "idDepartamentoPK" PRIMARY KEY (idDepartamento)
 )

CREATE TABLE Funcionario (
	idFuncionario serial,
	nome VARCHAR(150) NOT NULL,
	email VARCHAR(150) NOT NULL,
	idDepartamento int,
	senha VARCHAR(150) NOT NULL,
	admin BOOLEAN NOT NULL,
	login VARCHAR(150) NOT NULL, 	
	CONSTRAINT "idFuncionarioPK" PRIMARY KEY(IdFuncionario)
	/*CONSTRAINT "idDepartamentoFK" FOREIGN KEY(idDepartamento)
		REFERENCES Departamento(idDepartamento)*/
);

CREATE TABLE Projeto (
	idProjeto serial,
	nome VARCHAR(150) NOT NULL,
	dtPrevista date,
	CONSTRAINT "idProjeto" PRIMARY KEY(idProjeto)

)

CREATE TABLE FuncProj(
	idProjetoFK int,
	idFuncionarioFK int,
	CONSTRAINT "idProjetoFK" FOREIGN KEY(idProjetoFK)
		REFERENCES Projeto(idProjeto),

	CONSTRAINT "idFuncionarioFK" FOREIGN KEY(idFuncionarioFK)
		REFERENCES Funcionario(idFuncionario)
	
);

ALTER TABLE Funcionario ADD CONSTRAINT "idDepartamentoFK"
FOREIGN KEY(idDepartamento) REFERENCES Departamento (idDepartamento);


-- DROP TABLE if exists users cascade;

select * from Funcionario;
select * from Departamento;
select * from Projeto;
select * from FuncProj;

insert into departamento (nome) values ('departamento generico');
insert into funcionario (nome,email,login,senha,admin,idDepartamento) VALUES ('ademir','admin@gmail','adm','123',TRUE,1);
insert into funcionario (nome,email,login,senha,admin,idDepartamento) VALUES ('funcionario 1','funcionario1@gmail','f1','f1',FALSE,1);
insert into funcionario (nome,email,login,senha,admin,idDepartamento) VALUES ('funcionario 2','funcionario2@gmail','f2','f2',FALSE,1);
insert into funcionario (nome,email,login,senha,admin,idDepartamento) VALUES ('funcionario 3','funcionario3@gmail','f3','f3',FALSE,1);

SELECT * FROM Funcionario WHERE login = 'f1' and senha= 'f1';