import datetime

class aluno: 
    def __init__(self, matricula, nome, t_curso, idade, dep, conselheiro):
        self.matricula = matricula 
        self.nome = nome
        self.t_curso = t_curso
        self.idade = idade
        self.dep = dep
        self.conselheiro = conselheiro

    def proget():
        print("matricula")
        matricula = str(input())
        print("nome")
        nome = str(input())
        print("tipo do curso")
        t_curso = str(input())
        print("idade")
        idade = str(input())
        print("departamento")
        dep = str(input())
        print("conselheiro")
        conselheiro = str(input())
        caluno = aluno(matricula,nome,t_curso,idade,dep,conselheiro)
        out = aluno.__str__(caluno)
        return out
        
    def __str__(self) -> str:
        return (str(self.matricula), str(self.nome), str(self.t_curso), str(self.idade), str(self.dep), str(self.conselheiro))

class departamento:
    def __init__(self, numero, escritorio, nome, lider):
        self.numero = numero
        self.escritorio = escritorio
        self.nome = nome
        self.lider = lider
    def __str__(self) -> str:
        return (str(self.numero), str(self.escritorio), str(self.nome), str(self.lider))

    def proget():
        print("numero")
        numero = str(input())
        print("escritorio")
        escritorio = str(input())
        print("nome")
        nome = str(input())
        print("lider")
        lider = str(input())
        cdepartamento = departamento(numero,escritorio,nome,lider)
        out = departamento.__str__(cdepartamento)
        return out

    def __str__(self) -> str:
        return (str(self.numero), str(self.escritorio), str(self.nome), str(self.lider))

class participa:
    def __init__(self, participante, pnum):
        self.participante = participante
        self.pnum = pnum

    def proget():
        print("participante")
        participante = str(input())
        print("professor")
        pnum = str(input())
        cparticipa = participa(participante,pnum)
        out = participa.__str__(cparticipa)
        return out

    def __str__(self) -> str:
        return (str(self.participante), str(self.pnum))
        
class professor: 
    
    def __init__(self, matricula,idade, nome, sala, especialidade):
        self.matricula = matricula
        self.idade = idade 
        self.nome = nome
        self.sala = sala
        self.especialidade = especialidade

    def proget():
        print("matricula")
        matricula = str(input())
        print("idade")
        idade = str(input())
        print("nome")
        nome = str(input())
        print("sala")
        sala = str(input())
        print("especialidade")
        especialidade = str(input())
        cprofessor = professor(matricula,idade,nome,sala,especialidade)
        out = professor.__str__(cprofessor)
        return out

    def __str__(prof) -> str:
        return (str(prof.matricula), str(prof.idade), str(prof.nome), str(prof.sala), str(prof.especialidade))


class projeto:
    def __init__(self, numero, orcamento, data_inicio, data_fim, gerente):
        self.numero = numero
        self.orcamento = orcamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.gerente = gerente

    def proget():
        print("numero")
        numero = str(input())
        print("orçamento")
        orcamento = str(input())
        print("data inicio")
        data_inicio = str(input())
        print("data fim")
        data_fim = str(input())
        print("gerente")
        gerente = str(input())
        cprojeto = projeto(numero,orcamento,data_inicio,data_fim,gerente)
        out = projeto.__str__(cprojeto)
        return out

    def __str__(self) -> str:
        return (str(self.numero), str(self.orcamento), str(self.data_inicio), str(self.data_fim), str(self.gerente))

class trabalha: 
    def __init__(self, dnum, pmat, tempo):
        self.dnum = dnum
        self.pmat = pmat
        self.tempo = tempo

    def proget():
        print("departamento")
        dnum = str(input())
        print("professor")
        pmat = str(input())
        print("porcentagem horas")
        tempo = str(input())
        ctrabalha = trabalha(dnum,pmat,tempo)
        out = trabalha.__str__(ctrabalha)
        return out
        
    def __str__(self) -> str:
        return (str(self.dnum), str(self.pmat), str(self.tempo))   
        
     
     