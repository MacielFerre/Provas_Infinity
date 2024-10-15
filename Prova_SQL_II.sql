-- [PYIA-A16]
create database empresa;
use empresa;
create table Produtos(
	ProdutoID int primary key,
    NomeProduto varchar(50) not null,
    Quantidade decimal(10,2) not null,
    Preco decimal(10,2) not null
    );

insert into produtos(ProdutoID, NomeProduto, Quantidade, Preco) values
	(101, "Café", 2, 5.50),
    (102, "Leite", 6.5, 6),
    (103, "Feijão", 3, 8.35);