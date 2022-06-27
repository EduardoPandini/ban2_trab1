from time import strftime
from tkinter import W
from unittest.util import strclass
import tabelas
import psycopg2
import sys
import conexao

def selecione_a_tabela():
    print("selecione a tabela:")
    print("1 = professor:")
    print("2 = aluno:")
    print("3 = departamento")
    print("4 = projeto")
    print("5 = participa")
    print("6 = trabalha")

def seleciona(valor): #inserts
    conn, cursor = conexao.connect()
    print(cursor,conn)
    if valor == 1:
        selecione_a_tabela()
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
        sinsert(conn,cursor,tnome,out) 

    if valor == 2:
        selecione_a_tabela()
        ntab = int(input())
        if ntab == 1:
            tnome = "professor"       
        if ntab == 2:
            tnome = "aluno"  
        if ntab == 3:
            tnome = "departamento"   
        if ntab == 4:
            tnome = "projeto"   
        if ntab == 5:
            tnome = "participa"   
        if ntab == 6:
            tnome = "trabalha"
        print("informe a condição da querry")
        condicao = str(input())
        delete(conn,cursor,tnome,condicao)
            
    if valor == 3:
        selecione_a_tabela()
        ntab = int(input())
        if ntab == 1:
            tnome = "professor" 
        if ntab == 2:
            tnome = "aluno"   
        if ntab == 3:
            tnome = "departamento"
        if ntab == 4:
            tnome = "projeto"
        if ntab == 5:
            tnome = "participa"
        if ntab == 6:
            tnome = "trabalha"
        update(conn, cursor ,tnome)

    if valor == 4: 
        selecione_a_tabela()
        ntab = int(input())
        if ntab == 1:
            tnome = "professor" 
        if ntab == 2:
            tnome = "aluno"   
        if ntab == 3:
            tnome = "departamento"
        if ntab == 4:
            tnome = "projeto"
        if ntab == 5:
            tnome = "participa"
        if ntab == 6:
            tnome = "trabalha"
        select(conn,cursor,tnome)

def select(conn, cursor, tnome):
    print("informe os campos que deseja consultar (* para todos)")
    campos = str(input())
    print("informe a condição de seleção, vazio para todos os campos da tabela")
    condicao = (input())
    if condicao == '':
        condicao = ''
    else:
        condicao = 'where ' + condicao
    querry = f"select {campos} from {tnome} {condicao}"
    dale(conn, cursor, querry, True)


def update(conn,cursor,tnome):
    print("defina os campos que deseja alterar e seus novos valores")
    sets = str(input())
    print("defina a condição de update")
    cond = str(input())
    querry = f"update {tnome} set {sets} where {cond}"
    dale(conn, cursor, querry, False)

def sinsert(conn,cursor,tnome,values:tuple):
    querry = f"INSERT into {tnome} values {values}"
    print(querry)
    dale(conn,cursor,querry,False)
    cursor.execute(querry)
    conn.commit()

def delete(conn,cursor,tnome,condicao):
    querry = f"DELETE FROM {tnome} WHERE {condicao}"
    print(querry)
    dale(conn, cursor,querry,False)
    cursor.execute(querry)
    conn.commit()

def dale(conn, cursor, querry:str, resposta:bool):

    try:
        cursor.execute(querry)
        conn.commit()

        if resposta:
            results = cursor.fetchall() 
            for item in results:
                print(item)
            return results
    except psycopg2.ProgrammingError: # Erro gerado caso a query de erro
        print("Erro ao executar a query",querry, file=sys.stderr)
        return None

    