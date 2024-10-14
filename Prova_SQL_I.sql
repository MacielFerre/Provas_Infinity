-- [PYIA-A15] Crie uma tabela chamada Clientes com as colunas ID, Nome, Idade e Cidade. Defina a coluna ID como a chave primária e autoincrementável.
create database empresa;
use empresa;
create table Clientes(
	id int auto_increment primary key,
    nome varchar(50),
    idade int,
    cidade varchar(50)
    );
