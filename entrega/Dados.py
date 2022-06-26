# Aqui vão ficar as classes e seus respectivos métodos

from datetime import date

###########################

class Estudante:
    def __init__(self, matricula: int, nome: str, t_curso:str, dep: int, conselheiro: int) -> None:
        self.matricula      = matricula
        self.nome      = nome
        self.t_curso = t_curso
        self.dep = dep
        self.conselheiro = conselheiro
        self.tableName = 'aluno'

    def __str__(self) -> str:
        return (str(self.matricula), str(self.nome), str(self.t_curso), str(self.dep), str(self.conselheiro))

###########################

class Controlador:
    def __init__(self, matricula:int, nroMembro:int, cods:int, dataExame:date, nome:str) -> None:
        self.matricula  = matricula
        self.nroMembro = nroMembro
        self.cods       = cods
        self.dataExame  = dataExame
        self.nome       = nome
        self.tableName  = 'controlador'

    def __str__(self) -> str:
        return (str(self.matricula), str(self.nroMembro), str(self.cods), str(self.dataExame), self.nome)

###########################

class Modelo:
    def __init__(self, codm:int, nome:str, capacidade:int, peso:float, limite:int) -> None:
        self.codm       = codm
        self.nome       = nome
        self.capacidade = capacidade
        self.peso       = peso
        self.limite     = limite
        self.tableName  = 'modelo'

    def __str__(self) -> str:
        return (str(self.codm), self.nome, str(self.capacidade), str(self.peso), str(self.limite))

###########################

class Teste:
    def __init__(self, codt:int, coda:int, data:date, duracao:int, pontuacaoMax:int) -> None:
        self.codt         = codt # codt == numero do teste
        self.coda         = coda
        self.data         = data
        self.duracao      = duracao
        self.pontuacaoMax = pontuacaoMax
        self.tableName    = 'teste'
    
    def __str__(self) -> str:
        return (str(self.codt), str(self.coda), str(self.data), str(self.duracao), str(self.pontuacaoMax))

###########################

class Tecnico:
    def __init__(self, matricula:int, nroMembro:int, cods:int, codModelo:int, endereco:str, telefone:str, salario:float, nome:str) -> None:
        self.matricula = matricula
        self.nroMembro = nroMembro
        self.codModelo = codModelo # Modelo que ele é perito
        self.cods      = cods
        self.endereco  = endereco
        self.telefone  = telefone
        self.salario   = salario
        self.nome      = nome
        self.tableName = 'tecnico'

    def __str__(self) -> str:
        return (str(self.matricula), str(self.nroMembro), str(self.cods), str(self.codModelo), 
                    self.endereco, self.telefone, str(self.salario), self.nome)

###########################

class Sindicato:
    def __init__(self, nome:str, codSindicato:int) -> None:
        self.nome         = nome
        self.codSindicato = codSindicato

    def __str__(self) -> str:
        return (self.nome, str(self.codSindicato))
###########################

class Select:
    
    def __init__(self, listOfTuples:list) -> None:
        self.result = listOfTuples

    def __str__(self) -> str:
        return [((str(x).replace('(','')).replace(')','')).replace(' ','') for x in self.result]
        # convertendo a lista de tupla tipo [(1, 2, 3), (4, 5, 6)] em ['(1, 2, 3)','(4, 5, 6)']
        # e então removendo os parenteseses e espaços, resultado numa lista tipo ['1,2,3','4,5,6']
        # que pode então ser transformada em uma lista de listas do tipo [['1','2','3'], ['4','5','6']]
        # com o método split de strings, em particular split(',')
