from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import *
from tkinter.ttk import *

mydb = Database()

# TABELA TARIFA 
def tabela_tarifa():
    tarifa = Tk()
    tarifa.title("Tarifa")
    tarifa.geometry("755x350")
    style = ttk.Style(tarifa)
    tarifa.configure(bg='#FDFFFF')
    style.configure('TButton', font=('calibri', 11),
                    padding=5, width=20)


    def populate_list():
        lista_tarifa.delete(0, END)
        popular = mydb.mostrar_tarifas()
        for linha in popular:
            lista_tarifa.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_tarifa.curselection()[0]
            item_selecionado = lista_tarifa.get(indice)
            #colocar os dados selecionados dentro das entries, primeiro deleta dos campos e depois adiciona
            combotarifa.delete(0, END)
            combotarifa.insert(END, item_selecionado[0])
            # add_numero_voo_tarifa.delete(0, END)
            # add_numero_voo_tarifa.insert(END, item_selecionado[0])
            add_codigo_tarifa.delete(0, END)
            add_codigo_tarifa.insert(END, item_selecionado[1])
            add_quantidade.delete(0, END)
            add_quantidade.insert(END, item_selecionado[2])
            add_restricoes.delete(0, END)
            add_restricoes.insert(END, item_selecionado[3])
        except IndexError:
            pass


    def add_tarifa():
        if combotarifa.get() == '' or add_codigo_tarifa.get() == '' or add_quantidade.get() == '' or add_restricoes.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return
        mydb.inserir_tarifa(combotarifa.get(), add_codigo_tarifa.get(), add_quantidade.get(
        ), add_restricoes.get())  
        lista_tarifa.delete(0, END)  
        lista_tarifa.insert(END, (combotarifa.get(), add_codigo_tarifa.get(), add_quantidade.get(
        ), add_restricoes.get())) 
        limpar_tarifa()
        populate_list()

        
    def remove_tarifa():
        mydb.remover_tarifa(item_selecionado[0], item_selecionado[1])
        limpar_tarifa()
        populate_list()


    def update_tarifa():
        mydb.atualizar_tarifa(
            item_selecionado[0], item_selecionado[1], add_quantidade.get(), add_restricoes.get())
        populate_list()


    def limpar_tarifa():
        combotarifa.delete(0, END)
        # add_numero_voo_tarifa.delete(0, END)
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

    results = mydb.mostrar_primary_key_voo()
    results_for_combobox = [result for result in results]
    combotarifa = ttk.Combobox(tarifa, values=results_for_combobox, width=27)
    combotarifa.grid(row=0, column=1)

    # add_numero_voo_tarifa = Entry(tarifa, width=30)
    # add_numero_voo_tarifa.grid(row=0, column=1, padx=20)

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
    lista_tarifa = Listbox(tarifa, height=8, width=60)
    lista_tarifa.grid(row=25, column=0, columnspan=2,
                         rowspan=5, pady=10, padx=10)

    #criando scrollbar
    scrollbar = Scrollbar(tarifa)
    scrollbar.grid(row=25, column=2)

    #colocar a scroll na lista
    lista_tarifa.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_tarifa.yview)

    #ligar a lista ao select
    lista_tarifa.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
    tarifa.mainloop()
