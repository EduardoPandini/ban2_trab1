# Aqui vamos fazer a lógica de negócios, isto é, trabalhar sobre os dados recuperados do BD na camada de conectividade

import Conexao, Dados

# TODO: Tratar o retorno das funções start_connection e end_connection

# attributes = [attr for attr in (vars(myObject)).keys() if attr != 'tableName']
# pega todos os atributos do objeto myObject, exceto o nomeado tableName, pois esse não está na base de dados

def start_connection() -> tuple:
    """
    Função que inicia a conexão com o banco de dados
    Retorna False caso tenha dado um erro, True se não deu
    """
    connection, cursor = Conexao.init_connection()

    if not connection and not cursor:
        return False
    
    return (connection, cursor)

def end_connection(connection, cursor) -> bool:
    """
    Função que termina a conexão com o banco de dados
    Retorna False caso tenha dado um erro, True se não deu
    """
    return Conexao.close_conection(connection, cursor)
    
def database_operation(cursor, opcode:int, myObject, userQuery:str=None, fields:list=None, values:tuple=None, wherecond:str=None):

    # TODO: Criar um caso para operação de select 
    
    """
    Função que realiza uma operação sobre a base de dados
    Recebe um objeto referente à tabela que será manipulada, assim como atributos opcionais que podem ser usados na operações a serem realizadas
    Retorna uma string com o resultado da operação
    Significado dos opcode:
        0: Operação de inserção
        1: Operação de atualização
        2: Operação de deleção
    """

    if userQuery != None:
        return user_operation(cursor, userQuery)

    if opcode == 0:

        if values == None:
            return "É necessário fornecer valores para inserir"

        return insert_operation(cursor, myObject, values)

    elif opcode == 1:

        error     = "Na atualização é necessário fornecer "
        errorFlag = False

        if fields == None:
            error     += "campos que serão atualizados"
            errorFlag = True

        if values == None:
            error = error + "valores para os campos" if error == "É necessário fornecer " else error + " e valores para os campos"
            errorFlag = True

        if wherecond == None:
            error = error + "condição para atualização" if error == "É necessário fornecer " else error + " e condição para atualização"
            errorFlag = True

        if errorFlag:
            return error

        return update_operation(cursor, myObject, fields, values, wherecond)

    elif opcode == 2:

        if wherecond == None:
            return "É necessário fornecer condição para deleção"

        return delete_operation(cursor, myObject, wherecond)

    else:
        return "Operação inválida"

def insert_operation(cursor, myObject, values:tuple) -> str:
    """
    Função que realiza uma operação de inserção na base de dados
    Retorna uma string que contém uma descrição do resultado da operação
    """
    tableName = myObject.tableName

    result = Conexao.insert(cursor, tableName, values)

    if result == None:
        return "Erro ao executar a inserção, nenhuma linha afetada"
    else:
        return f"Inserção realizada com sucesso, {result} linhas inseridas na tabela {tableName}"

def update_operation(cursor, myObject, fields:list, values:tuple, wherecond:str) -> str:
    """
    Função que realiza uma operação de atualização na base de dados
    Retorna uma string que contém uma descrição do resultado da operação
    """
    tableName  = myObject.tableName

    result = Conexao.update(cursor, tableName, fields, values, wherecond)

    if result == None:
        return "Erro ao executar a atualização, nenhuma linha afetada"
    else:
        return f"Atualização realizada com sucesso, {result} linhas da tabela {tableName} foram modificadas"

def delete_operation(cursor, myObject, wherecond:str) -> str:
    """
    Função que realiza uma operação de deletar na base de dados
    Retorna uma string que contém uma descrição do resultado da operação
    """
    tableName  = myObject.tableName

    result = Conexao.delete(cursor, tableName, wherecond)

    if result == None:
        return "Erro ao executar a deleção, nenhuma linha afetada"
    else:
        return f"Deleção realizada com sucesso, {result} linhas da tabela {tableName} foram removidas"

def user_operation(cursor, userQuery:str):
    """
    Função que realiza uma operação fornecida pelo usuário na base de dados
    Retorna uma string que contém uma descrição do resultado da operação 
        ou um objeto contendo uma lista de tuplas que representa a tabela de retorno da operação
    """

    if "select".casefold() in userQuery.casefold():
        result = Conexao.user_query_select(cursor, userQuery)
        if result == None: # Caso a query tenha dado erro
            return f"Erro ao executar a query {userQuery}"

        return Dados.Select(result)

    result = Conexao.user_query_other(cursor, userQuery)
    if result == None: # Caso a query tenha dado erro
        return f"Erro ao executar a query {userQuery}"

    return f"Operação realizada com sucesso, {result} linhas foram afetadas"

def select_operation():
    pass