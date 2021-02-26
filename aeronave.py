from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *
from tkinter.ttk import *

mydb = Database()

#TABELA AERONAVE
def tabela_aeronave():
    aeronave = Tk()
    aeronave.title("Aeronave")
    aeronave.geometry("760x350")
    style = ttk.Style(aeronave)
    aeronave.configure(bg='#FDFFFF')
    style.configure('TButton', font=('calibri', 11),
                    padding=5, width=20)


    def populate_list():
        lista_aeronave.delete(0, END)
        popular = mydb.mostrar_aeronave()
        for linha in popular:
            lista_aeronave.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_aeronave.curselection()[0]
            item_selecionado = lista_aeronave.get(indice)
            add_codigo_aeronave.delete(0, END)
            add_codigo_aeronave.insert(END, item_selecionado[0])
            add_numero_t_assentos.delete(0, END)
            add_numero_t_assentos.insert(END, item_selecionado[1])
            combo_tipo_aeronave.delete(0, END)
            combo_tipo_aeronave.insert(END, item_selecionado[2])
        except IndexError:
            pass


    def add_aeronave():
        if add_codigo_aeronave.get() == '' or add_numero_t_assentos.get() == '' or combo_tipo_aeronave.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return

        mydb.inserir_aeronave(add_codigo_aeronave.get(), add_numero_t_assentos.get(), combo_tipo_aeronave.get()) #apenas adiciona ao database, não insere na lista

        lista_aeronave.delete(0, END) #limpa os dados da lista
        lista_aeronave.insert(END, (add_codigo_aeronave.get(), add_numero_t_assentos.get(), combo_tipo_aeronave.get())) #insere na lista o dado que foi adicionado
        limpar_aeronave()
        populate_list()


    def remove_aeronave():
        mydb.remover_aeronave(item_selecionado[0])
        limpar_aeronave()
        populate_list()


    def update_aeronave():
        mydb.atualizar_aeronave(item_selecionado[0], add_numero_t_assentos.get(), combo_tipo_aeronave.get())
        populate_list()


    def limpar_aeronave():
        add_codigo_aeronave.delete(0, END)
        add_numero_t_assentos.delete(0, END)
        combo_tipo_aeronave.delete(0, END)



    #Botões pra tela voo
    adicionar_aeronave = Button(aeronave, text="Adicionar aeronave", command=add_aeronave)
    adicionar_aeronave.grid(row=8, column=0, padx=10, pady=10)

    remover_aeronave = Button(aeronave, text="Remover Aeronave", command=remove_aeronave)
    remover_aeronave.grid(row=8, column=1, padx=10, pady=10)

    atualizar_aeronave = Button(aeronave, text="Atualizar Aeronave", command=update_aeronave)
    atualizar_aeronave.grid(row=8, column=2, padx=10, pady=10)

    limpar_campo_aeronave = Button(aeronave, text="Limpar campos", command=limpar_aeronave)
    limpar_campo_aeronave.grid(row=8, column=3, padx=10, pady=10)


    #caixas de texto:

    add_codigo_aeronave = Entry(aeronave, width=30)
    add_codigo_aeronave.grid(row=0, column=1, padx=20)

    add_numero_t_assentos = Entry(aeronave, width=30)
    add_numero_t_assentos.grid(row=1, column=1, padx=20)


    results = mydb.mostrar_primary_key_tipo_aeronave()
    results_for_combobox = [result for result in results]
    combo_tipo_aeronave = ttk.Combobox(
        aeronave, values=results_for_combobox, width=27)
    combo_tipo_aeronave.grid(row=2, column=1, padx=20)

    # add_tipo_aeronave = Entry(aeronave, width=30)
    # add_tipo_aeronave.grid(row=2, column=1, padx=20)


    #labels pras caixas de texto
    codigo_aeronave_label = Label(aeronave, text="Codigo Aeronave")
    codigo_aeronave_label.grid(row=0, column=0)
    
    numero_t_assentos_label = Label(aeronave, text="Numero Total de Assentos")
    numero_t_assentos_label.grid(row=1, column=0)

    tipo_aeronave_label = Label(aeronave, text="Tipo de Aeronave")
    tipo_aeronave_label.grid(row=2, column=0)
    
    #lista
    lista_aeronave = Listbox(aeronave, height=8, width=80)
    lista_aeronave.grid(row=25, column=0, columnspan=3, rowspan=5, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(aeronave)
    scrollbar.grid(row=25, column=3)

    #colocar a scroll na lista
    lista_aeronave.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_aeronave.yview)

    #ligar a lista ao select
    lista_aeronave.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
    aeronave.mainloop()
