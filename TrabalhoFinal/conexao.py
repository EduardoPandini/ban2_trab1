import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conexao = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conexao = psycopg2.connect(**params)
		
        # create a cursor
        cursor = conexao.cursor()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return(conexao,cursor)

if __name__ == '__main__':
    connect()