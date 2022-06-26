import datetime

class aluno: 
    def __init__(self, matricula, nome, t_curso, idade, dep, conselheiro):
        self.matricula = matricula 
        self.nome = nome
        self.t_curso = t_curso
        self.idade = idade
        self.dep = dep
        self.conselheiro = conselheiro
        
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

class participa:
    def __init__(self, participante, pnum):
        self.participante = participante
        self.pnum = pnum
    def __str__(self) -> str:
        return (str(self.participante), str(self.pnum))
        
class professor: 
        #matricula = int(input())
        #idade = int(input())
        #nome = str(input())
        #sala = str(input())
    def __init__(self, matricula,idade, nome, sala, especialidade):
        self.matricula = matricula
        self.idade = idade 
        self.nome = nome
        self.sala = sala
        self.especialidade = especialidade
    def __str__(self) -> str:
        return (str(self.matricula), str(self.idade), str(self.nome), str(self.sala), str(self.especialidade))

class projeto:
    def __init__(self, numero, orcamento, data_inicio, data_fim, gerente):
        self.numero = numero
        self.orcamento = orcamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.gerente = gerente
    def __str__(self) -> str:
        return (str(self.numero), str(self.orcamento), str(self.data_inicio), str(self.data_fim), str(self.gerente))

class trabalha: 
    def __init__(self, dnum, pmat, tempo):
        self.dnum = dnum
        self.pmat = pmat
        self.tempo = tempo
    def __str__(self) -> str:
        return (str(self.dnum), str(self.pmat), str(self.tempo))   
        
     
     