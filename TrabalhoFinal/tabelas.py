import datetime

class aluno: 
    def __init__(self, matricula, nome, t_curso, idade, dep, conselheiro):
        self.matricula = matricula 
        self.nome = nome
        self.t_curso = t_curso
        self.idade = idade
        self.dep = dep
        self.conselheiro = conselheiro

class departamento:
    def __init__(self, numero, escritorio, nome, lider):
        self.numero = numero
        self.escritorio = escritorio
        self.nome = nome
        self.lider = lider

class participa:
    def __init__(self, participante, pnum):
        self.participante = participante
        self.pnum = pnum

class professor: 
    def __init__(self, matricula,idade, nome, sala, especialidade):
        self.matricula = matricula 
        self.nome = nome
        self.idade = idade
        self.sala = sala
        self.especialidade = especialidade

class projeto:
    def __init__(self, numero, orcamento, data_inicio, data_fim, gerente):
        self.numero = numero
        self.orcamento = orcamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.gerente = gerente

class trabalha: 
    def __init__(self, dnum, pmat, tempo):
        self.dnum = dnum
        self.pmat = pmat
        self.tempo = tempo
        
        
     
     