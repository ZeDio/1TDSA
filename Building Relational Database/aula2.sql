Create table curso(
    id_curso number primary key,
    nome varchar2(100) not null
)

create table aluno(
    id_aluno number primary key,
    nome varchar2(100) not null
)

-- ALTER TABLE -- add colulas manualmente

alter table aluno add data_nascimento date;

alter table aluno add (
    email varchar2(150),
    telefone varchar2(20)
)

-- ALTER TABLE -- adicionar constraints
-- Adicionando chave estrangeira FK na tablela aluno

alter table aluno add id_curso number

alter table aluno add constraint fk_curso FOREIGN key (id_curso) references curso(id_curso)

-- alter table -- removendo colunas

alter table aluno drop column telefone

-- alter table -- aumentar/diminuir o tamanho de um campo ou modificar o tipo de tado

alter table aluno MODIFY nome varchar2(200)
alter table aluno RENAME COLUMN nome to nm_aluno
RENAME aluno to estudant;

-- Drop -- remover objetos
Drop table estudant;
alter table estudant drop column email;




create table aluno(
    id_aluno number primary key,
    nome varchar2(200)
)

insert into aluno values(1, 'José Diogo');
insert into aluno values(2, 'Andre Rosa');
insert into aluno values(3, 'Pedro Miranda');

select * from aluno;

truncate table aluno;