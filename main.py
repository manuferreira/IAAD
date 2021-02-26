from tkinter import *
from tkinter import messagebox
from db import *
from tkinter import ttk
from tkinter.ttk import *
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
style = ttk.Style(root)
root.configure(bg='#FDFFFF')
style.configure('TButton', font=('calibri', 11),
                padding=5, width=20)

#Botões pra tela principal
aeroporto = ttk.Button(root, text="Aeroporto",
                       command=tabela_aeroporto)
aeroporto.grid(row=20, column=0, padx=[50, 0], pady=10)

voo = ttk.Button(root, text="Vôo", command=tabela_voo)
voo.grid(row=20, column=1, padx=[50, 0], pady=10)

trecho = ttk.Button(root, text="Trecho dos Vôos", command=tabela_trecho)
trecho.grid(row=20, column=2, padx=[50, 0], pady=10)

tarifa = ttk.Button(root, text="Tarifa", command=tabela_tarifa)
tarifa.grid(row=21, column=0, padx=[50, 0], pady=10)

tipo_aeronave = ttk.Button(root, text="Tipos de aeronave", command=tabela_tipo_aeronave)
tipo_aeronave.grid(row=21, column=1, padx=[50, 0], pady=10)

pode_pousar = ttk.Button(root, text="Pouso", command=tabela_pode_pousar)
pode_pousar.grid(row=21, column=2, padx=[50, 0], pady=10)

instancia_trecho = ttk.Button(root, text="Instância dos trechos", command=tabela_instancia_trecho)
instancia_trecho.grid(row=22, column=0, padx=[50, 0], pady=10)

aeronave = ttk.Button(root, text="Aeronaves", command=tabela_aeronave)
aeronave.grid(row=22, column=1, padx=[50, 0], pady=10)

reserva_assento = ttk.Button(root, text="Reservas", command=tabela_reserva_assento)
reserva_assento.grid(row=22, column=2, padx=[50, 0], pady=10)

root.mainloop()
mydb.encerrar_conexao()




