from time import strftime
from unittest.util import strclass
from tabelas import *
import psycopg2

def insert(table):
    connection=psycopg2.connect("dbname=Faculdade user=postgres password=udesc")
    cursor=connection.cursor()
    if table== 1: #professor
        matricula = int(input())
        idade = int(input())
        nome = str(input())
        sala = str(input())
        especialidade = str(input())
        cursor.execute("INSERT INTO professor VALUES(%s,%s,%s,%s,%s)", (matricula,idade,nome,sala,especialidade)) ##injetar os valores na tabela
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
        
        
if __name__ == '__main__':
    select = int(input())
    print(select)
    insert(select)
    