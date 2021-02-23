from tkinter import *
from tkinter import messagebox
from db import *
mydb = Database()

#TABELA INSTANCIA_TRECHO
def tabela_instancia_trecho():
    instancia_trecho = Tk()
    instancia_trecho.title("Instacia Trecho")
    instancia_trecho.geometry("700x550")

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
            add_numero_voo.delete(0, END)
            add_numero_voo.insert(END, item_selecionado[0])
            add_numero_trecho.delete(0, END)
            add_numero_trecho.insert(END, item_selecionado[1])
            add_Data.delete(0, END)
            add_Data.insert(END, item_selecionado[2])
            add_numero_assentos.delete(0, END)
            add_numero_assentos.insert(END, item_selecionado[3])
            add_codigo_aeronave.delete(0, END)
            add_codigo_aeronave.insert(END, item_selecionado[4])
            add_codigo_aeroporto_p.delete(0, END)
            add_codigo_aeroporto_p.insert(END, item_selecionado[5])
            add_codigo_aeroporto_c.delete(0, END)
            add_codigo_aeroporto_c.insert(END, item_selecionado[6])
            add_horario_partida.delete(0, END)
            add_horario_partida.insert(END, item_selecionado[7])
            add_horario_chegada.delete(0, END)
            add_horario_chegada.insert(END, item_selecionado[8])
        except IndexError:
            pass


    def add_instancia_trecho():
        if add_numero_trecho.get() == '' or add_numero_voo.get() == '' or add_Data.get()=='' or add_numero_assentos.get()=='' or add_codigo_aeronave.get()=='' or  add_codigo_aeroporto_p.get() == '' or add_codigo_aeroporto_c.get() == '' or add_horario_partida.get() == '' or add_horario_chegada.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return

        mydb.inserir_instancia_trecho(add_numero_trecho.get(), add_numero_voo.get(), add_Data.get(), add_numero_assentos.get(), add_codigo_aeronave.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get()) #apenas adiciona ao database, não insere na lista

        lista_instancia_trecho.delete(0, END) #limpa os dados da lista
        lista_instancia_trecho.insert(END,(add_numero_trecho.get(), add_numero_voo.get(), add_Data.get(), add_numero_assentos.get(), add_codigo_aeronave.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())) #insere na lista o dado que foi adicionado
        limpar_instancia_trecho()
        populate_list()


    def remove_instancia_trecho():
        mydb.remover_instancia_trecho(item_selecionado[1])
        limpar_instancia_trecho()
        populate_list()


    def update_instancia_trecho():
        mydb.atualizar_instancia_trecho(add_numero_trecho.get(), add_numero_voo.get(),  add_Data.get(), add_numero_assentos.get(), add_codigo_aeronave.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())
        populate_list()


    def limpar_instancia_trecho():
        add_numero_trecho.delete(0, END)
        add_numero_voo.delete(0, END)
        add_Data.delete(0, END)
        add_numero_assentos.delete(0, END)
        add_codigo_aeronave.delete(0, END)
        add_codigo_aeroporto_p.delete(0, END)
        add_codigo_aeroporto_c.delete(0, END)
        add_horario_partida.delete(0, END)
        add_horario_chegada.delete(0, END)

     #Botões pra tela voo
    adicionar_instancia_trecho = Button(instancia_trecho, text="Adicionar Instancia Trecho", command=add_instancia_trecho)
    adicionar_instancia_trecho.grid(row=9, column=0, padx=10, pady=10)

    remover_instancia_trecho = Button(instancia_trecho, text="Remover Instancia Trecho", command=remove_instancia_trecho)
    remover_instancia_trecho.grid(row=9, column=1, padx=10, pady=10)

    atualizar_instancia_trecho = Button(instancia_trecho, text="Atualizar Instancia Trecho", command=update_instancia_trecho)
    atualizar_instancia_trecho.grid(row=9, column=2, padx=10, pady=10)

    limpar_campo_instancia_trecho = Button(instancia_trecho, text="Limpar campos", command=limpar_instancia_trecho)
    limpar_campo_instancia_trecho.grid(row=9, column=3, padx=10, pady=10)



    #caixas de texto:
    add_numero_trecho = Entry(instancia_trecho, width=30)
    add_numero_trecho.grid(row=0, column=1, padx=20)

    add_numero_voo = Entry(instancia_trecho, width=30)
    add_numero_voo.grid(row=1, column=1, padx=20)

    add_Data = Entry(instancia_trecho, width=30)
    add_Data.grid(row=2, column=1, padx=20)

    add_numero_assentos = Entry(instancia_trecho, width=30)
    add_numero_assentos.grid(row=3, column=1, padx=20)

    add_codigo_aeronave = Entry(instancia_trecho, width=30)
    add_codigo_aeronave.grid(row=4, column=1, padx=20)

    add_codigo_aeroporto_p = Entry(instancia_trecho, width=30)
    add_codigo_aeroporto_p.grid(row=5, column=1, padx=20)

    add_codigo_aeroporto_c = Entry(instancia_trecho, width=30)
    add_codigo_aeroporto_c.grid(row=6, column=1, padx=20)

    add_horario_partida = Entry(instancia_trecho, width=30)
    add_horario_partida.grid(row=7, column=1, padx=20)

    add_horario_chegada = Entry(instancia_trecho, width=30)
    add_horario_chegada.grid(row=8, column=1, padx=20)
    


    #labels pras caixas de texto
    numero_trecho_label = Label(instancia_trecho, text="Número Trecho")
    numero_trecho_label.grid(row=0, column=0)
    
    numero_voo_label = Label(instancia_trecho, text="Número Voo")
    numero_voo_label.grid(row=1, column=0)

    Data_label = Label(instancia_trecho, text="Data")
    Data_label.grid(row=2, column=0)

    numero_assento_label = Label(instancia_trecho, text="Número Assento")
    numero_assento_label.grid(row=3, column=0)
    
    codigo_aeronave_label = Label(instancia_trecho, text="Codigo Aeronave")
    codigo_aeronave_label.grid(row=4, column=0)

    codigo_aeroporto_p_label = Label(instancia_trecho, text="Aeroporto de Partida")
    codigo_aeroporto_p_label.grid(row=5, column=0)

    codigo_aeroporto_c_label = Label(instancia_trecho, text="Aeroporto de Chegada")
    codigo_aeroporto_c_label.grid(row=6, column=0)
    
    horario_partida_label = Label(instancia_trecho, text="Hora de Partida")
    horario_partida_label.grid(row=7, column=0)

    horario_chegada_label = Label(instancia_trecho, text="Hora de Chegada")
    horario_chegada_label.grid(row=8, column=0)
    
    #lista
    lista_instancia_trecho = Listbox(instancia_trecho, height=8, width=50)
    lista_instancia_trecho.grid(row=25, column=0, columnspan=9, rowspan=6, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(instancia_trecho)
    scrollbar.grid(row=25, column=8)

    #colocar a scroll na lista
    lista_instancia_trecho.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_instancia_trecho.yview)

    #ligar a lista ao select
    lista_instancia_trecho.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()    
