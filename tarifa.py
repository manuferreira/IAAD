from tkinter import *
from tkinter import messagebox
from db import *

# TABELA TARIFA 
def tabela_tarifa():
    tarifa = Tk()
    tarifa.title("Tarifa")
    tarifa.geometry("700x350")

    def populate_list():
        lista_tarifa.delete(0, END)
        popular = mydb.mostrar_tarifas()
        for linha in popular:
            lista_tarifa.insert(END, linha)

    def add_tarifa():
        if add_numero_voo_tarifa.get() == '' or add_codigo_tarifa.get() == '' or add_quantidade.get() == '' or add_restricoes.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return
        mydb.inserir_tarifa(add_numero_voo_tarifa.get(), add_codigo_tarifa.get(), add_quantidade.get(
        ), add_restricoes.get())  
        lista_tarifa.delete(0, END)  
        lista_tarifa.insert(END, (add_numero_voo_tarifa.get(), add_codigo_tarifa.get(), add_quantidade.get(
        ), add_restricoes.get())) 
        limpar_tarifa()
        populate_list()
        
    def remove_tarifa():
        mydb.remover_tarifa(item_selecionado[1])
        limpar_tarifa()
        populate_list()


    def update_tarifa():
        mydb.atualizar_tarifa(
            item_selecionado[0], item_selecionado[1], add_quantidade.get(), add_restricoes.get())
        populate_list()


    def limpar_tarifa():
        add_numero_voo_tarifa.delete(0, END)
        add_codigo_tarifa.delete(0, END)
        add_quantidade.delete(0, END)
        add_restricoes.delete(0, END)


    #botões pra tela tarifa:
    adicionar_tarifa = Button(
        tarifa, text="Adicionar tarifa", command=add_tarifa)
    adicionar_tarifa.grid(row=8, column=0, padx=10, pady=10)

    remover_tarifa = Button(
        tarifa, text="Remover tarifa", command=remove_tarifa)
    remover_tarifa.grid(row=8, column=1, padx=10, pady=10)

    atualizar_tarifa = Button(
        tarifa, text="Atualizar tarifa", command=update_tarifa)
    atualizar_tarifa.grid(row=8, column=2, padx=10, pady=10)

    limpar_campo_tarifa = Button(
        tarifa, text="Limpar campos", command=limpar_tarifa)
    limpar_campo_tarifa.grid(row=8, column=3, padx=10, pady=10)


    #caixas de texto:
    add_numero_voo_tarifa = Entry(tarifa, width=30)
    add_numero_voo_tarifa.grid(row=0, column=1, padx=20)

    add_codigo_tarifa = Entry(tarifa, width=30)
    add_codigo_tarifa.grid(row=1, column=1, padx=20)

    add_quantidade = Entry(tarifa, width=30)
    add_quantidade.grid(row=2, column=1, padx=20)

    add_restricoes = Entry(tarifa, width=30)
    add_restricoes.grid(row=3, column=1, padx=20)


    #labels pras caixas de texto
    add_numero_voo_tarifa_label = Label(tarifa, text="Numero voo")
    add_numero_voo_tarifa_label.grid(row=0, column=0)

    add_codigo_tarifa_label = Label(tarifa, text="Código Tarifa")
    add_codigo_tarifa_label.grid(row=1, column=0)

    add_quantidade_label = Label(tarifa, text="Quantidade")
    add_quantidade_label.grid(row=2, column=0)

    add_restricoes_label = Label(tarifa, text="Restrições")
    add_restricoes_label.grid(row=3, column=0)


    #lista
    lista_tarifa = Listbox(tarifa, height=8, width=50)
    lista_tarifa.grid(row=25, column=0, columnspan=3,
                         rowspan=5, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(tarifa)
    scrollbar.grid(row=25, column=3)

    #colocar a scroll na lista
    lista_tarifa.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_tarifa.yview)

    #ligar a lista ao select
    lista_tarifa.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
