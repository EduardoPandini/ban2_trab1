import psycopg2
from config import config
import sys
def conexao():
    """ Connect to the PostgreSQL database server """
    conexao = None
    try:
        params = config()

        # conecta
        print('Connecting to the PostgreSQL database...')
        conexao = psycopg2.connect(**params)
	
        #cursor
        cursor = conexao.cursor("cursor")
        
	    #debug
        print('PostgreSQL version:')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
       
       #se deu ruim
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

        #retorna conexao e cursor
    finally:
        if conexao is not None:
             return(conexao, cursor)

def close_conection(conection:psycopg2.extensions.connection, cursor:psycopg2.extensions.cursor) -> bool:
    """
    Função que termina a conexão com o banco de dados
    Retorna True se conseguiu terminar, False se não conseguiu
    """
    try:
        cursor.close()
        conexao.close()
    except psycopg2.Error: 
        # Não sei se é necessário tentar capturar erros aqui, não lembro de ter visto algo
        # sobre erros ao fechar a conexão na documentação, mas vou deixar por via das duvidas
        print("Erro ao terminar a conexão", file=sys.stderr)
        return False

    return True

def select_simples()