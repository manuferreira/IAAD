from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *
from tkinter.ttk import *

mydb = Database()

#TABELA INSTANCIA_TRECHO
def tabela_instancia_trecho():
    instancia_trecho = Tk()
    instancia_trecho.title("Instacia Trecho")
    instancia_trecho.geometry("760x400")
    style = ttk.Style(instancia_trecho)
    instancia_trecho.configure(bg='#FDFFFF')
    style.configure('TButton', font=('calibri', 11),
                    padding=5, width=20)

    def populate_list():
        lista_instancia_trecho.delete(0, END)
        popular = mydb.mostrar_instancia_trecho()
        for linha in popular:
            lista_instancia_trecho.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_instancia_trecho.curselection()[0]
            item_selecionado = lista_instancia_trecho.get(indice)
            combo_numero_voo.delete(0, END)
            combo_numero_voo.insert(END, item_selecionado[0])
            combo_numero_trecho.delete(0, END)
            combo_numero_trecho.insert(END, item_selecionado[1])
            add_Data.delete(0, END)
            add_Data.insert(END, item_selecionado[2])
            add_numero_assentos.delete(0, END)
            add_numero_assentos.insert(END, item_selecionado[3])
            combo_codigo_aeronave.delete(0, END)
            combo_codigo_aeronave.insert(END, item_selecionado[4])
            combo_codigo_aeroporto_p.delete(0, END)
            combo_codigo_aeroporto_p.insert(END, item_selecionado[5])
            add_horario_partida.delete(0, END)
            add_horario_partida.insert(END, item_selecionado[6])
            combo_codigo_aeroporto_c.delete(0, END)
            combo_codigo_aeroporto_c.insert(END, item_selecionado[7])
            add_horario_chegada.delete(0, END)
            add_horario_chegada.insert(END, item_selecionado[8])
        except IndexError:
            pass


    def add_instancia_trecho():
        if combo_numero_voo.get() == '' or combo_numero_trecho.get() == '' or add_Data.get() == '' or add_numero_assentos.get() == '' or combo_codigo_aeronave.get() == '' or combo_codigo_aeroporto_p.get() == '' or combo_codigo_aeroporto_c.get() == '' or add_horario_partida.get() == '' or add_horario_chegada.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return

        mydb.inserir_instancia_trecho(combo_numero_voo.get(), combo_numero_trecho.get(), add_Data.get(), add_numero_assentos.get(), combo_codigo_aeronave.get(), combo_codigo_aeroporto_p.get(), add_horario_partida.get(), combo_codigo_aeroporto_c.get(), add_horario_chegada.get())

        lista_instancia_trecho.delete(0, END)
        lista_instancia_trecho.insert(END, (combo_numero_voo.get(), combo_numero_trecho.get(), add_Data.get(), add_numero_assentos.get(
        ), combo_codigo_aeronave.get(), combo_codigo_aeroporto_p.get(), add_horario_partida.get(),combo_codigo_aeroporto_c.get(), add_horario_chegada.get()))
        limpar_instancia_trecho()
        populate_list()


    def remove_instancia_trecho():
        mydb.remover_instancia_trecho(item_selecionado[0], item_selecionado[1], item_selecionado[2])
        limpar_instancia_trecho()
        populate_list()


    def update_instancia_trecho():
        mydb.atualizar_instancia_trecho(combo_numero_voo.get(), combo_numero_trecho.get(),  add_Data.get(), add_numero_assentos.get(), combo_codigo_aeronave.get(), combo_codigo_aeroporto_p.get(), add_horario_partida.get(), combo_codigo_aeroporto_c.get(),  add_horario_chegada.get())
        populate_list()


    def limpar_instancia_trecho():
        combo_numero_voo.delete(0, END)
        combo_numero_trecho.delete(0, END)
        add_Data.delete(0, END)
        add_numero_assentos.delete(0, END)
        combo_codigo_aeronave.delete(0, END)
        combo_codigo_aeroporto_p.delete(0, END)
        add_horario_partida.delete(0, END)
        combo_codigo_aeroporto_c.delete(0, END)
        add_horario_chegada.delete(0, END)


    adicionar_instancia_trecho = Button(instancia_trecho, text="Adicionar instância", command=add_instancia_trecho)
    adicionar_instancia_trecho.grid(row=9, column=0, padx=10, pady=10)

    remover_instancia_trecho = Button(instancia_trecho, text="Remover instância", command=remove_instancia_trecho)
    remover_instancia_trecho.grid(row=9, column=1, padx=10, pady=10)

    atualizar_instancia_trecho = Button(instancia_trecho, text="Atualizar instância", command=update_instancia_trecho)
    atualizar_instancia_trecho.grid(row=9, column=2, padx=10, pady=10)

    limpar_campo_instancia_trecho = Button(instancia_trecho, text="Limpar campos", command=limpar_instancia_trecho)
    limpar_campo_instancia_trecho.grid(row=9, column=3, padx=10, pady=10)



    #caixas de texto:

    results_2 = mydb.mostrar_primary_key_voo()
    results_for_combobox_2 = [result for result in results_2]
    combo_numero_voo = ttk.Combobox(
        instancia_trecho, values=results_for_combobox_2, width=27)
    combo_numero_voo.grid(row=0, column=1, padx=20)
    # add_numero_voo = Entry(instancia_trecho, width=30)
    # add_numero_voo.grid(row=1, column=1, padx=20)

    results_1 = mydb.mostrar_pk_trecho_voo()
    results_for_combobox_1 = [result for result in results_1]
    combo_numero_trecho = ttk.Combobox(
    instancia_trecho, values=results_for_combobox_1, width=27)
    combo_numero_trecho.grid(row=1, column=1, padx=20)
    # add_numero_trecho = Entry(instancia_trecho, width=30)
    # add_numero_trecho.grid(row=0, column=1, padx=20)


    add_Data = Entry(instancia_trecho, width=30)
    add_Data.grid(row=2, column=1, padx=20)

    add_numero_assentos = Entry(instancia_trecho, width=30)
    add_numero_assentos.grid(row=3, column=1, padx=20)


    results_3 = mydb.mostrar_pk_aeronave()
    results_for_combobox_3 = [result for result in results_3]
    combo_codigo_aeronave = ttk.Combobox(
        instancia_trecho, values=results_for_combobox_3, width=27)
    combo_codigo_aeronave.grid(row=4, column=1, padx=20)
    # add_codigo_aeronave = Entry(instancia_trecho, width=30)
    # add_codigo_aeronave.grid(row=4, column=1, padx=20) 


    results_4 = mydb.mostrar_primary_key_aeroporto()
    results_for_combobox_4 = [result for result in results_4]
    combo_codigo_aeroporto_p = ttk.Combobox(
        instancia_trecho, values=results_for_combobox_4, width=27)
    combo_codigo_aeroporto_p.grid(row=5, column=1, padx=20)
    # add_codigo_aeroporto_p = Entry(instancia_trecho, width=30)
    # add_codigo_aeroporto_p.grid(row=5, column=1, padx=20)


    add_horario_partida = Entry(instancia_trecho, width=30)
    add_horario_partida.grid(row=6, column=1, padx=20)


    results_5 = mydb.mostrar_primary_key_aeroporto()
    results_for_combobox_5 = [result for result in results_5]
    combo_codigo_aeroporto_c = ttk.Combobox(
        instancia_trecho, values=results_for_combobox_5, width=27)
    combo_codigo_aeroporto_c.grid(row=7, column=1, padx=20)
    # add_codigo_aeroporto_c = Entry(instancia_trecho, width=30)
    # add_codigo_aeroporto_c.grid(row=6, column=1, padx=20)


    add_horario_chegada = Entry(instancia_trecho, width=30)
    add_horario_chegada.grid(row=8, column=1, padx=20)
    

    #labels pras caixas de texto
    numero_voo_label = Label(instancia_trecho, text="Número Voo")
    numero_voo_label.grid(row=0, column=0)

    numero_trecho_label = Label(instancia_trecho, text="Número Trecho")
    numero_trecho_label.grid(row=1, column=0)

    Data_label = Label(instancia_trecho, text="Data")
    Data_label.grid(row=2, column=0)

    numero_assento_label = Label(instancia_trecho, text="Assentos disponíveis")
    numero_assento_label.grid(row=3, column=0)
    
    codigo_aeronave_label = Label(instancia_trecho, text="Codigo Aeronave")
    codigo_aeronave_label.grid(row=4, column=0)

    codigo_aeroporto_p_label = Label(instancia_trecho, text="Aeroporto de Partida")
    codigo_aeroporto_p_label.grid(row=5, column=0)

    horario_partida_label = Label(instancia_trecho, text="Hora de Partida")
    horario_partida_label.grid(row=6, column=0)

    codigo_aeroporto_c_label = Label(instancia_trecho, text="Aeroporto de Chegada")
    codigo_aeroporto_c_label.grid(row=7, column=0)
    
    horario_chegada_label = Label(instancia_trecho, text="Hora de Chegada")
    horario_chegada_label.grid(row=8, column=0)
    
    #lista
    lista_instancia_trecho = Listbox(instancia_trecho, height=8, width=60)
    lista_instancia_trecho.grid(row=25, column=0, columnspan=2, rowspan=5, pady=10, padx=10)

    #criando scrollbar
    scrollbar = Scrollbar(instancia_trecho)
    scrollbar.grid(row=25, column=2)

    #colocar a scroll na lista
    lista_instancia_trecho.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_instancia_trecho.yview)

    #ligar a lista ao select
    lista_instancia_trecho.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()    
