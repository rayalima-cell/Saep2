create database empresa;
use empresa;

create table clientes(
	id_cliente int auto_increment primary key,
    nome varchar(45) not null,
    email varchar(45) not null,
    telefone varchar(45)
);

insert into clientes(nome, email, telefone)
values
("Ray Aryel", "rayaryel@gmail", "85 86958637"),
("Arthur", "arthurmainardi@gmail", "47 88904293"),
("Layla", "laylasaraiva@gmail", "47 89129694"),
("Lia", "liaribeiro@gmail", "47 84915783");

select * from clientes