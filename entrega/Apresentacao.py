# Aqui vai ficar a interface gráfica

# pip install tk
# https://docs.python.org/3/library/tkinter.html

from tkinter import *
from tkinter import ttk

###################################################################################################
# Criando a janela + coisas frufru

janela = Tk()
janela.title('Aeroporto')
# janela.inconphoto(False, 'viao')
janela.geometry("800x800")

caderno = ttk.Notebook(janela)
caderno.pack(pady=15)

# viao = PhotoImage(file = "/viao.png")

###################################################################################################
# Definindo as abas

modelo          = Frame(caderno, width = 800, height = 800, bg = "gray")
aviao           = Frame(caderno, width = 800, height = 800, bg = "gray")
teste           = Frame(caderno, width = 800, height = 800, bg = "gray")
sindicato       = Frame(caderno, width = 800, height = 800, bg = "gray")
controlador     = Frame(caderno, width = 800, height = 800, bg = "gray")
tecnico         = Frame(caderno, width = 800, height = 800, bg = "gray")

modelo.pack     (fill="both", expand = 1)
aviao.pack      (fill="both", expand = 1)
teste.pack      (fill="both", expand = 1)
sindicato.pack  (fill="both", expand = 1)
controlador.pack(fill="both", expand = 1)
tecnico.pack    (fill="both", expand = 1)

caderno.add(modelo,      text="Modelos", font=("Arial", 25))
caderno.add(aviao,       text="Aviões")
caderno.add(teste,       text="Testes")
caderno.add(sindicato,   text="Sindicatos")
caderno.add(controlador, text="Controladores")
caderno.add(tecnico,     text="Técnicos")

###################################################################################################

 #######################################
 # Apresentando tabela de modelos
 #######################################

arvore_modelo = ttk.Treeview(modelo)

# Definindo as colunas
arvore_modelo['column'] = ("Codm", "Nome", "Capacidade", "Peso", "Limite")


# Formatar as colunas
arvore_modelo.column("#0",           width=0,        stretch=NO)
arvore_modelo.column("Codm",         anchor=CENTER,  width=50)
arvore_modelo.column("Nome",         anchor=W,       width=120)
arvore_modelo.column("Capacidade",   anchor=CENTER,  width=100)
arvore_modelo.column("Peso",         anchor=CENTER,  width=50)
arvore_modelo.column("Limite",       anchor=CENTER,  width=70)

# Criando os Headings
arvore_modelo.heading("#0",          text="",            anchor=W)
arvore_modelo.heading("Codm",        text="CODM",        anchor=CENTER)
arvore_modelo.heading("Nome",        text="Nome",        anchor=CENTER)
arvore_modelo.heading("Capacidade",  text="Capacidade",  anchor=CENTER)
arvore_modelo.heading("Peso",        text="Peso",        anchor=CENTER)
arvore_modelo.heading("Limite",      text="Limite",      anchor=CENTER)

# Adicionando dados
# arvore_modelo.insert(parent='', index='end', iid=0, text='', values=())
    # iid precisam ser sempre diferentes
arvore_modelo.insert(parent='', index='end', iid=0, text='', values=(0, 'asda', 100, 200, 300))
arvore_modelo.insert(parent='', index='end', iid=1, text='', values=(1, 'kkkkkkk', 800, 500, 1000))




arvore_modelo.pack(pady=30)















###################################################################################################

# Loop para fazer a janela ficar rodando pra sempre

janela.mainloop()