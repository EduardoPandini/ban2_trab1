from time import strftime
from unittest.util import strclass
import tabelas
import psycopg2
import sys


        
def seleciona(valor): #inserts
    conexao,cursor = conexao.connect()
    if valor == 1:
        print("selecione a tabela:")
        print("1 = professor:")
        print("2 = aluno:")
        print("3 = departamento")
        print("4 = projeto")
        print("5 = participa")
        print("6 = trabalha")
        ntab = int(input())

        if ntab == 1:
            tnome = "professor"
            out = tabelas.professor.proget()
        if ntab == 2:
            tnome = "aluno"
            out = tabelas.aluno.proget()    
        if ntab == 3:
            tnome = "departamento"
            out = tabelas.departamento.proget()
        if ntab == 4:
            tnome = "projeto"
            out = tabelas.projeto.proget()
        if ntab == 5:
            tnome = "participa"
            out = tabelas.participa.proget()
        if ntab == 6:
            tnome = "trabalha"
            out = tabelas.trabalha.proget()
        sinsert(conexao,cursor,tnome,out) 


def sinsert(conexao,cursor,tnome,values:tuple):
        querry = f"INSERT into {tnome} values {values}"
        print(querry)
        resposta:False
        dale(cursor,querry,resposta)
        cursor.execute(querry)
        conexao.commit()

def dale(cursor:psycopg2.extensions.cursor, querry:str, resposta:bool):

    try:
        cursor.execute(querry)
        cursor.commit()

        if resposta:
            results = cursor.fetchall() # retorna uma lista de tuplas

    except psycopg2.ProgrammingError: # Erro gerado caso a query de erro
        print("Erro ao executar a query",querry, file=sys.stderr)
        return None

    return results
if __name__ == '__main__':

    linha =  tabelas.professor(4,22,'ze','salaze','zethings')
    linhain = tabelas.professor.__str__(linha)
    print(linhain)
    sinsert(1,linhain)
    