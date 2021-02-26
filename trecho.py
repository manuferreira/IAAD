from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *
from tkinter.ttk import *

mydb = Database()

#TABELA TRECHO
def tabela_trecho():
    trecho = Tk()
    trecho.title("Trecho")
    trecho.geometry("760x350")
    style = ttk.Style(trecho)
    trecho.configure(bg='#FDFFFF')
    style.configure('TButton', font=('calibri', 11),
                    padding=5, width=20)

    def populate_list():
        lista_trecho.delete(0, END)
        popular = mydb.mostrar_trecho_voo()
        for linha in popular:
            lista_trecho.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_trecho.curselection()[0]
            item_selecionado = lista_trecho.get(indice)
            add_numero_trecho.delete(0, END)
            add_numero_trecho.insert(END, item_selecionado[0])
            combo_numero_voo.delete(0, END)
            combo_numero_voo.insert(END, item_selecionado[1])
            combo_aeroporto_p.delete(0, END)
            combo_aeroporto_p.insert(END, item_selecionado[2])
            combo_aeroporto_c.delete(0, END)
            combo_aeroporto_c.insert(END, item_selecionado[3])
            add_horario_partida.delete(0, END)
            add_horario_partida.insert(END, item_selecionado[4])
            add_horario_chegada.delete(0, END)
            add_horario_chegada.insert(END, item_selecionado[5])
        except IndexError:
            pass


    def add_trecho():
        if add_numero_trecho.get() == '' or combo_numero_voo.get() == '' or combo_aeroporto_p.get() == '' or combo_aeroporto_c.get() == '' or add_horario_partida.get() == '' or add_horario_chegada.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return

        # apenas adiciona ao database, não insere na lista
        mydb.inserir_trecho_voo(add_numero_trecho.get(), combo_numero_voo.get(), combo_aeroporto_p.get(), combo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())

        lista_trecho.delete(0, END) #limpa os dados da lista
        lista_trecho.insert(END,(add_numero_trecho.get(), combo_numero_voo.get(), combo_aeroporto_p.get(), combo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())) #insere na lista o dado que foi adicionado
        limpar_trecho()
        populate_list()


    def remove_trecho():
        mydb.remover_trecho_voo(item_selecionado[0], item_selecionado[1])
        limpar_trecho()
        populate_list()


    def update_trecho():
        mydb.atualizar_trecho_voo(item_selecionado[0], item_selecionado[1], combo_aeroporto_p.get(
        ), combo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())
        populate_list()


    def limpar_trecho():
        add_numero_trecho.delete(0, END)
        combo_numero_voo.delete(0, END)
        combo_aeroporto_p.delete(0, END)
        combo_aeroporto_c.delete(0, END)
        add_horario_partida.delete(0, END)
        add_horario_chegada.delete(0, END)


     #Botões pra tela trecho
    adicionar_trecho = Button(trecho, text="Adicionar Trecho", command=add_trecho)
    adicionar_trecho.grid(row=8, column=0, padx=10, pady=10)

    remover_trecho = Button(trecho, text="Remover Trecho", command=remove_trecho)
    remover_trecho.grid(row=8, column=1, padx=10, pady=10)

    atualizar_trecho = Button(trecho, text="Atualizar Trecho", command=update_trecho)
    atualizar_trecho.grid(row=8, column=2, padx=10, pady=10)

    limpar_campo_trecho = Button(trecho, text="Limpar campos", command=limpar_trecho)
    limpar_campo_trecho.grid(row=8, column=3, padx=10, pady=10)



    #caixas de texto:
    add_numero_trecho = Entry(trecho, width=30)
    add_numero_trecho.grid(row=0, column=1, padx=20)


    results_1 = mydb.mostrar_primary_key_voo()
    combo_results_1 = [result for result in results_1]
    combo_numero_voo = ttk.Combobox(trecho, values=combo_results_1, width=27)
    combo_numero_voo.grid(row=1, column=1, padx=20)
    # add_numero_voo = Entry(trecho, width=30)
    # add_numero_voo.grid(row=0, column=1, padx=20)

    results_2 = mydb.mostrar_primary_key_aeroporto()
    combo_results_2 = [result for result in results_2]
    combo_aeroporto_p = ttk.Combobox(trecho, values=combo_results_2, width=27)
    combo_aeroporto_p.grid(row=2, column=1, padx=20)
    # add_codigo_aeroporto_p = Entry(trecho, width=30)
    # add_codigo_aeroporto_p.grid(row=2, column=1, padx=20)


    results_3 = mydb.mostrar_primary_key_aeroporto()
    combo_results_3 = [result for result in results_3]
    combo_aeroporto_c = ttk.Combobox(trecho, values=combo_results_3, width=27)
    combo_aeroporto_c.grid(row=3, column=1, padx=20)
    # add_codigo_aeroporto_c = Entry(trecho, width=30)
    # add_codigo_aeroporto_c.grid(row=3, column=1, padx=20)

    add_horario_partida = Entry(trecho, width=30)
    add_horario_partida.grid(row=4, column=1, padx=20)

    add_horario_chegada = Entry(trecho, width=30)
    add_horario_chegada.grid(row=5, column=1, padx=20)
    


    #labels pras caixas de texto
    numero_trecho_label = Label(trecho, text="Número Trecho")
    numero_trecho_label.grid(row=0, column=0)

    numero_voo_label = Label(trecho, text="Número Voo")
    numero_voo_label.grid(row=1, column=0)

    codigo_aeroporto_p_label = Label(trecho, text="Aeroporto de Partida")
    codigo_aeroporto_p_label.grid(row=2, column=0)

    codigo_aeroporto_c_label = Label(trecho, text="Aeroporto de Chegada")
    codigo_aeroporto_c_label.grid(row=3, column=0)
    
    horario_partida_label = Label(trecho, text="Hora de Partida")
    horario_partida_label.grid(row=4, column=0)

    horario_chegada_label = Label(trecho, text="Hora de Chegada")
    horario_chegada_label.grid(row=5, column=0)
    
    #lista
    lista_trecho = Listbox(trecho, height=8, width=60)
    lista_trecho.grid(row=25, column=0, columnspan=2, rowspan=5, pady=10, padx=10)

    #criando scrollbar
    scrollbar = Scrollbar(trecho)
    scrollbar.grid(row=25, column=2)

    #colocar a scroll na lista
    lista_trecho.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_trecho.yview)

    #ligar a lista ao select
    lista_trecho.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()
