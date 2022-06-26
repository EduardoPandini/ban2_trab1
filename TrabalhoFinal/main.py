import funcoes

def menu():
    print("--------------------------------------------------------------------------------------------")
    print("menu legal")
    print("para inserir selecione 1")
    print("para deletar selecione 2")
    print("para alterar selecione 3")
    print("para consultar selecione 4")
    print("para encerrar o programa selecione 0")
    print("---------------------------------------------------------------------------------------------")
    opcao = int(input())
    funcoes.seleciona(opcao)


if __name__ == '__main__':
    menu()