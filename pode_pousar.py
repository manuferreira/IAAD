from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *
from tkinter.ttk import *

mydb = Database()

# TABELA PODE_POUSAR 
def tabela_pode_pousar():
    pode_pousar = Tk()
    pode_pousar.title("Pode pousar")
    pode_pousar.geometry("700x330")
    style = ttk.Style(pode_pousar)
    pode_pousar.configure(bg='#FDFFFF')
    style.configure('TButton', font=('calibri', 11),
                    padding=5, width=20)
        

    def populate_list():
        lista_pode_pousar.delete(0, END)
        popular = mydb.mostrar_pode_pousar()
        for linha in popular:
            lista_pode_pousar.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_pode_pousar.curselection()[0]
            item_selecionado = lista_pode_pousar.get(indice)
            combo_tipo_aeronave.delete(0, END)
            combo_tipo_aeronave.insert(END, item_selecionado[0])
            combo_codigo_aeroporto.delete(0, END)
            combo_codigo_aeroporto.insert(END, item_selecionado[1])
        except IndexError:
            pass


    def add_pouso():
        if combo_tipo_aeronave.get() == '' or combo_codigo_aeroporto.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return
        mydb.adicionar_pode_pousar(combo_tipo_aeronave.get(), combo_codigo_aeroporto.get())
        lista_pode_pousar.delete(0, END)
        lista_pode_pousar.insert(END, (combo_tipo_aeronave.get(), combo_codigo_aeroporto.get()))
        limpar_pode_pousar()
        populate_list()


    def remove_pouso():
        mydb.remover_pode_pousar(item_selecionado[0], item_selecionado[1])
        limpar_pode_pousar()
        populate_list()


    def limpar_pode_pousar():
        combo_tipo_aeronave.delete(0, END)
        combo_codigo_aeroporto.delete(0, END)


    adicionar_pouso = Button(
        pode_pousar, text="Adicionar pouso", command=add_pouso)
    adicionar_pouso.grid(row=8, column=0, padx=10, pady=10)

    remover_pouso = Button(
        pode_pousar, text="Remover um pouso", command=remove_pouso)
    remover_pouso.grid(row=8, column=1, padx=10, pady=10)

    limpar_campo_pode_pousar = Button(
        pode_pousar, text="Limpar campos", command=limpar_pode_pousar)
    limpar_campo_pode_pousar.grid(row=8, column=2, padx=10, pady=10)


    #caixas de texto:
    results = mydb.mostrar_primary_key_tipo_aeronave()
    results_for_combobox = [result for result in results]
    combo_tipo_aeronave = ttk.Combobox(
        pode_pousar, values=results_for_combobox, width=27)
    combo_tipo_aeronave.grid(row=0, column=1, padx=20)

    # add_nome_tipo_aeronave = Entry(pode_pousar, width=30)
    # add_nome_tipo_aeronave.grid(row=0, column=1, padx=20)

    results = mydb.mostrar_primary_key_aeroporto()
    results_for_combobox = [result for result in results]
    combo_codigo_aeroporto = ttk.Combobox(
        pode_pousar, values=results_for_combobox, width=27)
    combo_codigo_aeroporto.grid(row=1, column=1, padx=20)

    # add_codigo_aeroporto = Entry(pode_pousar, width=30)
    # add_codigo_aeroporto.grid(row=1, column=1, padx=20)


    #labels pras caixas de texto
    add_nome_tipo_aeronave_label = Label(
        pode_pousar, text="Nome do tipo de aeronave")
    add_nome_tipo_aeronave_label.grid(row=0, column=0)

    add_codigo_aeronave_label = Label(
        pode_pousar, text="Código do aeroporto")
    add_codigo_aeronave_label.grid(row=1, column=0)


    #lista
    lista_pode_pousar = Listbox(pode_pousar, height=8, width=60)
    lista_pode_pousar.grid(row=25, column=0, columnspan=2,
                             rowspan=5, pady=10, padx=10)

    #criando scrollbar
    scrollbar = Scrollbar(pode_pousar)
    scrollbar.grid(row=25, column=2)

    #colocar a scroll na lista
    lista_pode_pousar.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_pode_pousar.yview)

    #ligar a lista ao select
    lista_pode_pousar.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
