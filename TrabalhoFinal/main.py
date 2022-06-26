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
    opcao = 1
    
    if opcao == 1:
        #print("digite o nome da tabela??") 
        #tabela = str(input())
        #out = tabelas.professor.proget()
        #converte = tabelas.professor.__str__(prof)
       # prof = tabelas.professor(out)
        
        #print(converte)
        funcoes.seleciona(opcao)

if __name__ == '__main__':
    menu()