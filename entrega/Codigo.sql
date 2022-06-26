create table modelo (
	codm serial primary key not null,
 	nome varchar(40) default 'SEM NOME REGISTRADO',
 	capacidade integer not null,
 	peso decimal not null,
 	limite integer default 1
);

create table aviao(
 	coda serial primary key not null,
 	codm serial,
	pontuacao int,
 	foreign key (codm) references modelo
 		on update cascade
 		on delete set null
);

create table teste(
	codt int not null,
	coda serial,
	data date not null,
	duracao int,
	pontuacaoMaxima integer not null,
	constraint teste_pkey primary key(codt, coda),
	foreign key (coda) references aviao
		on update cascade
		on delete set null	
);

create table sindicato(
	cods serial primary key not null,
	nome varchar(30)
);

create table controlador(	
	matricula serial primary key not null,
	nro_membro integer not null,
	cods serial,
	dataUltimoExame date,
	nome varchar(30),
	foreign key (cods) references sindicato
		on update cascade
		on delete set null
);

create table tecnico(
	matricula serial primary key not null,
	nro_membro integer not null,
	codm serial,
	cods serial,
	endereco varchar(50),
	telefone varchar(15),
	salario decimal,
	nome varchar(30),
	foreign key (cods) references sindicato
		on update cascade
		on delete set null,
	foreign key (codm) references modelo
		on update cascade
		on delete set null
);
