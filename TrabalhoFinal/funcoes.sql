--idade minima para alunos

create function idade() returns trigger as
	$$
		declare
			
		begin
			if new.idade < 17 then
			
				RAISE EXCEPTION 'a idade do estudante deve ser ao menos 17 anos';
			else 
			
				return new;
			end if;
		end;
	$$
	language plpgsql;

create trigger idade_estudante before insert or update on aluno  
for each row execute procedure idade();

	
--aluno e aconselhador devem ter o mesmo curso	
create OR REPLACE function aconselhador() returns trigger as
	$$
		declare
			aconselhador varchar;
		begin
		aconselhador = (select t_curso from aluno where matricula = new.conselheiro);
		if new.t_curso = aconselhador then
			return new;
			else 
			
				RAISE EXCEPTION 'ACONSELHADOR E ALUNO DEVEM SER DO MESMO CURSO';
			end if;
		end;
	$$
	language plpgsql;

	create OR REPLACE trigger aconselhador before insert or update on aluno  
	for each row execute procedure aconselhador();

--Projeto necessita de verba minima por aluno

create OR REPLACE function verba() returns trigger as
	$$
		declare
			verbaD integer default 0;
			verbaR integer default 0;
		begin
		verbaD = (select count(participante) from participa where pnum = new.pnum) * 300;
		verbaR = (select orcamento from projeto where numero = new.pnum);
		if verbaR >= verbaD then
			return new;
			else 
				RAISE EXCEPTION 'projeto sem verba';
			end if;
		end;
	$$
	language plpgsql;

	create OR REPLACE trigger verba before insert or update on participa  
	for each row execute procedure verba();

--professor nao pode usar mais que 100% de seu tempo

create OR REPLACE function porcentagem() returns trigger as
	$$
		declare
			porcentagem integer default 0;
		begin
		porcentagem = (select count(tempo) from trabalha where pmat = new.pmat) + new.tempo;
		if porcentagem < 100 then
			return new;
			else 
				RAISE EXCEPTION 'trabalhando mais que 100 por cento?';
			end if;
		end;
	$$
	language plpgsql;

	create OR REPLACE trigger porcentagem before insert or update on trabalha  
	for each row execute procedure porcentagem();


--função para inserir aluno 

CREATE FUNCTION insert_aluno(matricula int, nome varchar, t_curso varchar, idade int, dep int, conselheiro int) RETURNS void AS
$$
BEGIN
INSERT INTO aluno (matricula, nome, t_curso, idade, dep, conselheiro)
values (matricula, nome, t_curso, idade, dep, conselheiro);
END;
$$
LANGUAGE plpgsql;

	
	
	