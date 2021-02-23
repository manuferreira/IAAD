from tkinter import *
from tkinter import messagebox
from db import *
from trecho import tabela_trecho
from instancia import tabela_instancia_trecho
from aeronave import tabela_aeronave
from voo import tabela_voo
from reserva_assento import tabela_reserva_assento
from aeroporto import tabela_aeroporto
from tarifa import tabela_tarifa
from pode_pousar import tabela_pode_pousar
from tipo_aeronave import tabela_tipo_aeronave

mydb = Database()

root = Tk() #janela principal
root.title('Companhia Aérea')
root.geometry("700x350")


#Botões pra tela principal
aeroporto = Button(root, text="Dados aeroporto", command=tabela_aeroporto)
aeroporto.grid(row=20, column=0, padx=10)

voo = Button(root, text="Dados voo", command=tabela_voo)
voo.grid(row=20, column=1, padx=10)

trecho = Button(root, text="Dados dos Trechos", command=tabela_trecho)
trecho.grid(row=20, column=2, padx=10)


tarifa = Button(root, text="Dados tarifa", command=tabela_tarifa)
tarifa.grid(row=20, column=3, padx=10)

tipo_aeronave = Button(root, text="Dados do tipo de aeronave", command=tabela_tipo_aeronave)
tipo_aeronave.grid(row=20, column=4, padx=10)

pode_pousar = Button(root, text="Dados sobre o pouso", command=tabela_pode_pousar)
pode_pousar.grid(row=20, column=5, padx=10)

instancia_trecho = Button(root, text="Dados das Instancias dos Trechos", command=tabela_instancia_trecho)
instancia_trecho.grid(row=20, column=3, padx=10)

aeronave = Button(root, text="Dados das Aeronaves", command=tabela_aeronave)
aeronave.grid(row=21, column=0, padx=10, pady=10)

reserva_assento = Button(root, text="Dados das Reserva dos Assentos", command=tabela_reserva_assento)
reserva_assento.grid(row=21, column=1, padx=10, pady=10)

root.mainloop()
mydb.encerrar_conexao()




