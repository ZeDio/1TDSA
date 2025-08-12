drop table Aluno

Create table Aluno(
    id_aluno varchar primary key,
    ra int unique,
    nome varchar(60) not null,
    dt_nascimento date,
    cep int references Endereco(cep)
);

create table professor(
    ra int,
    nome varchar2(60) not null,
    cpf int(11 unique),
    dt_nascimento date
);

create table professor2(
    ra int,
    nome varchar2(60) not null,
    cpf int(11) unique,
    dt_nascimento date
    constraint uk_cpf Unique(cpf)
);

create table endereco(
    cep int primary key,
    rua varchar2(60),
    cidade varchar2(100),
    uf char(2)
);
