from tkinter import *
from tkinter import messagebox
from db import *

# TABELA TIPO_AERONAVE
def tabela_tipo_aeronave():
    tipo_aeronave = Tk()
    tipo_aeronave.title("Voo")
    tipo_aeronave.geometry("700x350")

    def populate_list():
        lista_tipo_aeronave.delete(0, END)
        popular = mydb.mostrar_tipo_aeronave()
        for linha in popular:
            lista_tipo_aeronave.insert(END, linha)


    def add_tipo_aeronave():
        if add_nome_tipo_aeronave.get() == '' or add_qtd_assentos.get() == '' or add_companhia.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return
        mydb.adicionar_tipo_aeronave(add_nome_tipo_aeronave.get(), add_qtd_assentos.get(), add_companhia.get(
        ))
        lista_tipo_aeronave.delete(0, END)
        lista_tipo_aeronave.insert(END, (add_nome_tipo_aeronave.get(), add_qtd_assentos.get(), add_companhia.get(
        )))
        limpar_tipo_aeronave()
        populate_list()

    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_tipo_aeronave.curselection()[0]
            item_selecionado = lista_tipo_aeronave.get(indice)
            add_nome_tipo_aeronave.delete(0, END)
            add_nome_tipo_aeronave.insert(END, item_selecionado[0])
            add_qtd_assentos.delete(0, END)
            add_qtd_assentos.insert(END, item_selecionado[1])
            add_companhia.delete(0, END)
            add_companhia.insert(END, item_selecionado[2])
        except IndexError:
            pass
        

    def remove_tipo_aeronave():
        mydb.remover_tipo_aeronave(item_selecionado[0])
        limpar_tipo_aeronave()
        populate_list()


    def update_tipo_aeronave():
        mydb.atualizar_tipo_aeronave(
            item_selecionado[0], add_qtd_assentos.get(), add_companhia.get())
        populate_list()


    def limpar_tipo_aeronave():
        add_nome_tipo_aeronave.delete(0, END)
        add_qtd_assentos.delete(0, END)
        add_companhia.delete(0, END)


    #botões pra tela tipo aeronave:
    adicionar_tipo_aeronave = Button(
        tipo_aeronave, text="Adicionar tipo de aeronave", command=add_tipo_aeronave)
    adicionar_tipo_aeronave.grid(row=8, column=0, padx=10, pady=10)

    remover_tipo_aeronave = Button(
        tipo_aeronave, text="Remover um tipo de aeronave", command=remove_tipo_aeronave)
    remover_tipo_aeronave.grid(row=8, column=1, padx=10, pady=10)

    atualizar_tipo_aeronave = Button(
        tipo_aeronave, text="Atualizar um tipo de aeronave", command=update_tipo_aeronave)
    atualizar_tipo_aeronave.grid(row=8, column=2, padx=10, pady=10)

    limpar_campo_tipo_aeronave = Button(
        tipo_aeronave, text="Limpar campos", command=limpar_tipo_aeronave)
    limpar_campo_tipo_aeronave.grid(row=8, column=3, padx=10, pady=10)

    #caixas de texto:
    add_nome_tipo_aeronave = Entry(tipo_aeronave, width=30)
    add_nome_tipo_aeronave.grid(row=0, column=1, padx=20)

    add_qtd_assentos = Entry(tipo_aeronave, width=30)
    add_qtd_assentos.grid(row=1, column=1, padx=20)

    add_companhia= Entry(tipo_aeronave, width=30)
    add_companhia.grid(row=2, column=1, padx=20)


    #labels pras caixas de texto
    add_nome_tipo_aeronave_label = Label(tipo_aeronave, text="Nome do tipo de aeronave")
    add_nome_tipo_aeronave_label.grid(row=0, column=0)

    add_qtd_assentos_label = Label(tipo_aeronave, text="Quantidade máxima de assentos")
    add_qtd_assentos_label.grid(row=1, column=0)

    add_companhia_label = Label(tipo_aeronave, text="Companhia")
    add_companhia_label.grid(row=2, column=0)


    #lista
    lista_tipo_aeronave = Listbox(tipo_aeronave, height=8, width=50)
    lista_tipo_aeronave.grid(row=25, column=0, columnspan=3,
                      rowspan=5, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(tipo_aeronave)
    scrollbar.grid(row=25, column=3)

    #colocar a scroll na lista
    lista_tipo_aeronave.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_tipo_aeronave.yview)

    #ligar a lista ao select
    lista_tipo_aeronave.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
