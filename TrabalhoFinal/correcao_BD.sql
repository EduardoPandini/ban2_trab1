create table professor (
matricula SERIAL not null,
idade INTEGER not null,
nome VARCHAR(50) not null,
sala VARCHAR(20) not null,
especialidade VARCHAR(20) not null,
primary key (matricula)
);

create table departamento (
numero SERIAL not null,
escritorio VARCHAR(20) not null,
nome VARCHAR(50) not null,
lider SERIAL not null,
primary key (numero),
foreign key (lider) references professor on update cascade
);

create table aluno (
matricula SERIAL not null,
nome VARCHAR(50) not null,
t_curso VARCHAR(20) not null,
idade INTEGER not null,
dep SERIAL not null,
conselheiro SERIAL,
primary key (matricula),
foreign key (dep) references departamento on update cascade,
foreign key (conselheiro) references aluno on update cascade
);

create table projeto (
numero SERIAL not null,
orcamento DECIMAL not null,
data_inicio DATE not null,
data_fim DATE not null,
gerente SERIAL not null,
primary key (numero),
foreign key (gerente) references professor on update cascade
);

create table trabalha (
dnum SERIAL not null,
pmat SERIAL not null,
tempo integer not null,
constraint trabalha_pkey primary key(dnum, pmat),
foreign key (dnum) references departamento on update cascade,
foreign key (pmat) references professor on update cascade
);

create table participa (
participante SERIAL not null,
pnum SERIAL not null,
constraint participa_pkey primary key(participante, pnum),
foreign key (participante) references aluno on update cascade,
foreign key (pnum) references projeto on update cascade
);