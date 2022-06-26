from time import strftime
from unittest.util import strclass
import tabelas
import psycopg2
import sys


        
    

def insert(table,instr:str):
    connection=psycopg2.connect("dbname=Faculdade user=postgres password=udesc")
    cursor=connection.cursor()
    if table== 1: #professor

        #matricula = int(input())
        #idade = int(input())
        #nome = str(input())
        #sala = str(input())
        #especialidade = str(input())
        cursor.execute("INSERT INTO professor VALUES(%s)", (instr)) ##injetar os valores na tabela
        connection.commit()
        connection.close()

    if table == 2: #aluno
        matricula = int(input())
        nome = str(input())
        t_curso = str(input())
        idade = int(input())
        dep = int(input())
        conselheiro = int(input())
        cursor.execute("INSERT INTO aluno VALUES(%s,%s,%s,%s,%s,%s)", (matricula,nome,t_curso,idade,dep,conselheiro)) ##injetar os valores na tabela
        connection.commit()
        connection.close()

    if table == 3: #departamento
        numero = int(input())
        escritorio = str(input())
        nome = str(input())
        lider = int(input())
        cursor.execute("INSERT INTO departamento VALUES(%s,%s,%s,%s)", (numero,escritorio,nome,lider)) ##injetar os valores na tabela
        connection.commit()
        connection.close()

    if table == 4: #projeto
        numero = int(input())
        orcamento = int(input())
        data_inicio = strftime(input())
        data_fim = strftime(input())
        gerente = int(input())
        cursor.execute("INSERT INTO projeto VALUES(%s,%s,%s,%s,%s)", (numero,orcamento,data_inicio,data_fim,gerente))
        connection.commit()
        connection.close()

    if table == 5: #trabalha
        dnum = int(input())
        pmat = int(input())
        tempo = int(input())
        cursor.execute("INSERT INTO trabalha VALUES(%s,%s,%s)", (dnum,pmat,tempo))
        connection.commit()
        connection.close()

    if table == 6: #participa
        participante = int(input())
        pnum = int(input())
        cursor.execute("INSERT INTO participa VALUES(%s,%s)", (participante,pnum))
        connection.commit()
        connection.close()

    if table == 7: #selects
        print("insira a tabela que deseja selecionar")
        tabela = str(input())
        print("o que deseja selecionar, separado por virgulas (* para tudo)")
        colunas = str(input())
        print("insira a condicao de selecao")
        querry= str(input())
        cursor.execute("select " + colunas + " from " + tabela + " where " + querry)
        connection.commit()
        rows=cursor.fetchall()
        for item in rows:
            print(item)
        connection.close()

def sinsert(tablename:str, values:tuple):
        connection=psycopg2.connect("dbname=Faculdade user=postgres password=udesc")
        cursor=connection.cursor()
        tablename = 'professor'
        execString = f"insert into {tablename} values {values}"
        print(execString)
        cursor.execute(execString)
        connection.commit()

def dale(cursor:psycopg2.extensions.cursor, execString:str, returnsTable:bool):
    """
    Função para executar uma query 
        Já que praticamente todas as funções acima lidam com a execução de uma 
        query de praticamente a mesma forma, é mais conveniente colocar isso 
        numa função separada
    execString é a query a ser executada
    returnsTable indica se essa query deveria retornar tabelas ou não, i.e.:
        True:  Retorna tabelas     (usa o método fetchall())
        False: Não retorna tabelas (usa o método rowcount())
    """

    try:
        cursor.execute(execString)
        cursor.commit()

        if returnsTable:
            results = cursor.fetchall() # retorna uma lista de tuplas
        else:
            results = cursor.rowcount()

    except psycopg2.ProgrammingError: # Erro gerado caso a query de erro
        print("Erro ao executar a query",execString, file=sys.stderr)
        return None

    return results
if __name__ == '__main__':

    linha =  tabelas.professor(4,22,'ze','salaze','zethings')
    linhain = tabelas.professor.__str__(linha)
    print(linhain)
    sinsert(1,linhain)
    