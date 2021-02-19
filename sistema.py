from tkinter import *
from tkinter import messagebox
from db import *

mydb = Database()

root = Tk() #janela principal
root.title('Companhia Aérea')
root.geometry("700x350")


# TABELA AEROPORTO
def tabela_aeroporto():
    aeroporto = Tk()
    aeroporto.title("Aeroporto")
    aeroporto.geometry("700x350")


    def populate_list():
        lista_aeroporto.delete(0, END)
        popular = mydb.mostrar_aeroportos()
        for linha in popular:
            lista_aeroporto.insert(END, linha)

    def add_aeroporto():
        if add_codigo.get() == '' or add_nome.get() == '' or add_cidade.get() == '' or add_estado.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return
        mydb.inserir_aeroporto(add_codigo.get(), add_nome.get(), add_cidade.get(), add_estado.get()) #apenas adiciona ao database, não insere na lista
        lista_aeroporto.delete(0, END) #limpa os dados da lista
        lista_aeroporto.insert(END, (add_codigo.get(), add_nome.get(), add_cidade.get(), add_estado.get())) #insere na lista o dado que foi adicionado
        limpar_aeroporto()
        populate_list()

    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_aeroporto.curselection()[0]
            item_selecionado = lista_aeroporto.get(indice)
            #colocar os dados selecionados dentro das entries, primeiro deleta dos campos e depois adiciona
            add_codigo.delete(0, END)
            add_codigo.insert(END, item_selecionado[0])
            add_nome.delete(0, END)
            add_nome.insert(END, item_selecionado[1])
            add_cidade.delete(0, END)
            add_cidade.insert(END, item_selecionado[2])
            add_estado.delete(0, END)
            add_estado.insert(END, item_selecionado[3])
        except IndexError:
            pass
  

    def remove_aeroporto():
        mydb.remover_aeroporto(item_selecionado[0]) #remove o item a partir do código do aeroporto
        limpar_aeroporto()
        populate_list()


    def update_aeroporto():
        mydb.atualizar_aeroportos(item_selecionado[0], add_nome.get(), add_cidade.get(), add_estado.get())
        populate_list()

    def limpar_aeroporto():
        add_codigo.delete(0, END)
        add_nome.delete(0, END)
        add_cidade.delete(0, END)
        add_estado.delete(0, END)
    
    def mostrar_reserva():
        passagem = Tk()
        passagem.title("Passagens Reservadas")
        passagem.geometry("700x350")

        lista_reservas = Listbox(passagem,height=8, width=80)
        lista_reservas.grid(row=1, column=0, columnspan=20, rowspan=5, pady=20, padx=20)
        

        def populate_list_reservas():
            lista_reservas.delete(0, END)
            passagens = mydb.mostrar_passagens()
            for linha in passagens:
                lista_reservas.insert(END, linha)
                
    
        populate_list_reservas()
        
        #quit_button = Button(lista_reservas, text="Quit", command=root.destroy).pack()
        
        
    #botões pra tela aeroporto:
    adicionar_aeroporto = Button(aeroporto, text="Adicionar aeroporto", command=add_aeroporto)
    adicionar_aeroporto.grid(row=8, column=0, padx=10, pady=10)

    remover_aeroporto = Button(aeroporto, text="Remover aeroporto", command=remove_aeroporto)
    remover_aeroporto.grid(row=8, column=1, padx=10, pady=10)

    atualizar_aeroporto = Button(aeroporto, text="Atualizar aeroporto", command=update_aeroporto)
    atualizar_aeroporto.grid(row=8, column=2, padx=10, pady=10)

    limpar_campo_aeroporto = Button(aeroporto, text="Limpar campos", command=limpar_aeroporto)
    limpar_campo_aeroporto.grid(row=8, column=3, padx=10, pady=10)

    reserva = Button(aeroporto, text="Passagens reservadas", command=mostrar_reserva)
    reserva.grid(row=31, column=0, padx=10, pady=10)    


    #caixas de texto:
    add_codigo = Entry(aeroporto, width=30)
    add_codigo.grid(row=0, column=1, padx=20)

    add_nome = Entry(aeroporto, width=30)
    add_nome.grid(row=1, column=1, padx=20)

    add_cidade = Entry(aeroporto, width=30)
    add_cidade.grid(row=2, column=1, padx=20)

    add_estado = Entry(aeroporto, width=30)
    add_estado.grid(row=3, column=1, padx=20)


    #labels pras caixas de texto
    add_aeroporto_label = Label(aeroporto, text="Codigo Aeroporto")
    add_aeroporto_label.grid(row=0, column=0)
    
    nome_aeroporto_label = Label(aeroporto, text="Nome")
    nome_aeroporto_label.grid(row=1, column=0)

    cidade_aeroporto_label = Label(aeroporto, text="Cidade")
    cidade_aeroporto_label.grid(row=2, column=0)

    estado_aeroporto_label = Label(aeroporto, text="Estado")
    estado_aeroporto_label.grid(row=3, column=0)

    #lista
    lista_aeroporto = Listbox(aeroporto, height=8, width=50)
    lista_aeroporto.grid(row=25, column=0, columnspan=3, rowspan=5, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(aeroporto)
    scrollbar.grid(row=25, column=3)

    #colocar a scroll na lista
    lista_aeroporto.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_aeroporto.yview)

    #ligar a lista ao select
    lista_aeroporto.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()


# TABELA VOO
def tabela_voo():
    voo = Tk()
    voo.title("Aeroporto")
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

def tabela_trecho():
    trecho = Tk()
    trecho.title("Aeroporto")
    trecho.geometry("700x350")

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
            add_numero_voo.delete(0, END)
            add_numero_voo.insert(END, item_selecionado[1])
            add_codigo_aeroporto_p.delete(0, END)
            add_codigo_aeroporto_p.insert(END, item_selecionado[2])
            add_codigo_aeroporto_c.delete(0, END)
            add_codigo_aeroporto_c.insert(END, item_selecionado[3])
            add_horario_partida.delete(0, END)
            add_horario_partida.insert(END, item_selecionado[4])
            add_horario_chegada.delete(0, END)
            add_horario_chegada.insert(END, item_selecionado[5])
        except IndexError:
            pass


    def add_trecho():
        if add_numero_trecho.get() == '' or add_numero_voo.get() == '' or add_codigo_aeroporto_p.get() == '' or add_codigo_aeroporto_c.get() == '' or add_horario_partida.get() == '' or add_horario_chegada.get() == '':
            messagebox.showerror('Preencha todos os campos')
            return

        mydb.inserir_trecho_voo(add_numero_trecho.get(), add_numero_voo.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get()) #apenas adiciona ao database, não insere na lista

        lista_trecho.delete(0, END) #limpa os dados da lista
        lista_trecho.insert(END,(add_numero_trecho.get(), add_numero_voo.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())) #insere na lista o dado que foi adicionado
        limpar_trecho()
        populate_list()


    def remove_trecho():
        mydb.remover_trecho_voo(item_selecionado[0])
        limpar_trecho()
        populate_list()


    def update_trecho():
        mydb.atualizar_trecho_voo(item_selecionado[0], add_numero_voo.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())
        populate_list()


    def limpar_trecho():
        add_numero_trecho.delete(0, END)
        add_numero_voo.delete(0, END)
        add_codigo_aeroporto_p.delete(0, END)
        add_codigo_aeroporto_c.delete(0, END)
        add_horario_partida.delete(0, END)
        add_horario_chegada.delete(0, END)

     #Botões pra tela voo
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

    add_numero_voo = Entry(trecho, width=30)
    add_numero_voo.grid(row=1, column=1, padx=20)

    add_codigo_aeroporto_p = Entry(trecho, width=30)
    add_codigo_aeroporto_p.grid(row=2, column=1, padx=20)

    add_codigo_aeroporto_c = Entry(trecho, width=30)
    add_codigo_aeroporto_c.grid(row=3, column=1, padx=20)

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
    lista_trecho = Listbox(trecho, height=8, width=50)
    lista_trecho.grid(row=25, column=0, columnspan=7, rowspan=6, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(trecho)
    scrollbar.grid(row=25, column=8)

    #colocar a scroll na lista
    lista_trecho.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_trecho.yview)

    #ligar a lista ao select
    lista_trecho.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()

def tabela_instancia_trecho():
    instancia_trecho = Tk()
    instancia_trecho.title("Aeroporto")
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
            add_numero_trecho.delete(0, END)
            add_numero_trecho.insert(END, item_selecionado[0])
            add_numero_voo.delete(0, END)
            add_numero_voo.insert(END, item_selecionado[1])
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

        lista_trecho.delete(0, END) #limpa os dados da lista
        lista_trecho.insert(END,(add_numero_trecho.get(), add_numero_voo.get(), add_Data.get(), add_numero_assentos.get(), add_codigo_aeronave.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())) #insere na lista o dado que foi adicionado
        limpar_trecho()
        populate_list()


    def remove_instancia_trecho():
        mydb.remover_instancia_trecho(item_selecionado[0])
        limpar_trecho()
        populate_list()


    def update_instancia_trecho():
        mydb.atualizar_instancia_trecho(item_selecionado[0], add_numero_voo.get(),  add_Data.get(), add_numero_assentos.get(), add_codigo_aeronave.get(), add_codigo_aeroporto_p.get(), add_codigo_aeroporto_c.get(), add_horario_partida.get(), add_horario_chegada.get())
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

#Botões pra tela principal
aeroporto = Button(root, text="Dados aeroporto", command=tabela_aeroporto)
aeroporto.grid(row=20, column=0, padx=10)

voo = Button(root, text="Dados voo", command=tabela_voo)
voo.grid(row=20, column=1, padx=10)

trecho = Button(root, text="Dados dos Trechos", command=tabela_trecho)
trecho.grid(row=20, column=2, padx=10)

instancia_trecho = Button(root, text="Dados das Instancias dos Trechos", command=tabela_instancia_trecho)
instancia_trecho.grid(row=20, column=3, padx=10)

root.mainloop()
mydb.encerrar_conexao()




