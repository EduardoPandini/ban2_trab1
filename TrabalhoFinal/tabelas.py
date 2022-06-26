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
        matricula = str(input())
        nome = str(input())
        t_curso = str(input())
        idade = str(input())
        dep = str(input())
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
        numero = str(input())
        escritorio = str(input())
        nome = str(input())
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
        participante = str(input())
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
        matricula = str(input())
        idade = str(input())
        nome = str(input())
        sala = str(input())
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
        numero = str(input())
        orcamento = str(input())
        data_inicio = str(input())
        data_fim = str(input())
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
        dnum = str(input())
        pmat = str(input())
        tempo = str(input())
        ctrabalha = trabalha(dnum,pmat,tempo)
        out = trabalha.__str__(ctrabalha)
        return out
        
    def __str__(self) -> str:
        return (str(self.dnum), str(self.pmat), str(self.tempo))   
        
     
     