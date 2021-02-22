from tkinter import *
from tkinter import messagebox
from db import *

# TABELA VOO
def tabela_voo():
    voo = Tk()
    voo.title("Voo")
    voo.geometry("700x350")


    def populate_list():
        lista_voo.delete(0, END)
        popular = mydb.mostrar_voos()
        for linha in popular:
            lista_voo.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_voo.curselection()[0]
            item_selecionado = lista_voo.get(indice)
            add_numero_voo.delete(0, END)
            add_numero_voo.insert(END, item_selecionado[0])
            add_companhia_aerea.delete(0, END)
            add_companhia_aerea.insert(END, item_selecionado[1])
            add_dia.delete(0, END)
            add_dia.insert(END, item_selecionado[2])
        except IndexError:
            pass


    def add_voo():
        if add_numero_voo.get() == '' or add_companhia_aerea.get() == '' or add_dia.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return

        mydb.inserir_voo(add_numero_voo.get(), add_companhia_aerea.get(), add_dia.get()) #apenas adiciona ao database, não insere na lista

        lista_voo.delete(0, END) #limpa os dados da lista
        lista_voo.insert(END, (add_numero_voo.get(), add_companhia_aerea.get(), add_dia.get())) #insere na lista o dado que foi adicionado
        limpar_voo()
        populate_list()


    def remove_voo():
        mydb.remover_voo(item_selecionado[0])
        limpar_voo()
        populate_list()


    def update_voo():
        mydb.atualizar_voo(item_selecionado[0], add_companhia_aerea.get(), add_dia.get())
        populate_list()


    def limpar_voo():
        add_numero_voo.delete(0, END)
        add_companhia_aerea.delete(0, END)
        add_dia.delete(0, END)



    #Botões pra tela voo
    adicionar_voo = Button(voo, text="Adicionar voo", command=add_voo)
    adicionar_voo.grid(row=8, column=0, padx=10, pady=10)

    remover_voo = Button(voo, text="Remover voo", command=remove_voo)
    remover_voo.grid(row=8, column=1, padx=10, pady=10)

    atualizar_voo = Button(voo, text="Atualizar voo", command=update_voo)
    atualizar_voo.grid(row=8, column=2, padx=10, pady=10)

    limpar_campo_voo = Button(voo, text="Limpar campos", command=limpar_voo)
    limpar_campo_voo.grid(row=8, column=3, padx=10, pady=10)


    #caixas de texto:
    add_numero_voo = Entry(voo, width=30)
    add_numero_voo.grid(row=0, column=1, padx=20)

    add_companhia_aerea = Entry(voo, width=30)
    add_companhia_aerea.grid(row=1, column=1, padx=20)

    add_dia = Entry(voo, width=30)
    add_dia.grid(row=2, column=1, padx=20)


    #labels pras caixas de texto
    numero_voo_label = Label(voo, text="Número voo")
    numero_voo_label.grid(row=0, column=0)
    
    nome_companhia_label = Label(voo, text="Companhia Aérea")
    nome_companhia_label.grid(row=1, column=0)

    dia_label = Label(voo, text="Dia da semana")
    dia_label.grid(row=2, column=0)
    
    #lista
    lista_voo = Listbox(voo, height=8, width=50)
    lista_voo.grid(row=25, column=0, columnspan=3, rowspan=5, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(voo)
    scrollbar.grid(row=25, column=3)

    #colocar a scroll na lista
    lista_voo.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_voo.yview)

    #ligar a lista ao select
    lista_voo.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
