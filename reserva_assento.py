from tkinter import *
from tkinter import messagebox
from db import *

mydb = Database()

#TABELA RESERVA_ASSENTO
def tabela_reserva_assento():
    reserva_assento = Tk()
    reserva_assento.title("Reservade assentos")
    reserva_assento.geometry("700x550")

    def populate_list():
        lista_reserva_assento.delete(0, END)
        popular = mydb.mostrar_reserva_assento()
        for linha in popular:
            lista_reserva_assento.insert(END, linha)


    def selecionar_item(event):
        try:
            global item_selecionado
            indice = lista_reserva_assento.curselection()[0]
            item_selecionado = lista_reserva_assento.get(indice)
            add_numero_trecho.delete(0, END)
            add_numero_trecho.insert(END, item_selecionado[1])
            add_numero_voo.delete(0, END)
            add_numero_voo.insert(END, item_selecionado[0])
            add_Data.delete(0, END)
            add_Data.insert(END, item_selecionado[2])
            add_numero_assento.delete(0, END)
            add_numero_assento.insert(END, item_selecionado[3])
            add_Nome_cliente.delete(0, END)
            add_Nome_cliente.insert(END, item_selecionado[4])
            add_Telefone_cliente.delete(0, END)
            add_Telefone_cliente.insert(END, item_selecionado[5])
           
        except IndexError:
            pass


    def add_reserva_assento():
        if add_numero_trecho.get() == '' or add_numero_voo.get() == '' or add_Data.get()=='' or add_numero_assento.get()=='' or add_Nome_cliente.get()=='' or  add_Telefone_cliente.get() == '': #
            messagebox.showerror('Preencha todos os campos')
            return

        mydb.inserir_reserva_assento(add_numero_trecho.get(), add_numero_voo.get(),  add_Data.get(), add_numero_assento.get(), add_Nome_cliente.get(), add_Telefone_cliente.get()) #apenas adiciona ao database, não insere na lista

        lista_reserva_assento.delete(0, END) #limpa os dados da lista
        lista_reserva_assento.insert(END,(add_numero_trecho.get(), add_numero_voo.get(),  add_Data.get(), add_numero_assento.get(), add_Nome_cliente.get(), add_Telefone_cliente.get())) #insere na lista o dado que foi adicionado
        limpar_reserva_assento()
        populate_list()


    def remove_reserva_assento():
        mydb.remover_reserva_assento(item_selecionado[1])
        limpar_reserva_assento()
        populate_list()


    def update_reserva_assento():
        mydb.atualizar_reserva_assento(add_numero_trecho.get(), add_numero_voo.get(),  add_Data.get(), add_numero_assento.get(), add_Nome_cliente.get(), add_Telefone_cliente.get())
        populate_list()


    def limpar_reserva_assento():
        add_numero_trecho.delete(0, END)
        add_numero_voo.delete(0, END)
        add_Data.delete(0, END)
        add_numero_assento.delete(0, END)
        add_Nome_cliente.delete(0, END)
        add_Telefone_cliente.delete(0, END)
     

     #Botões pra tela reserva_assento
    adicionar_reserva_assento = Button(reserva_assento, text="Adicionar reserva_assento", command=add_reserva_assento)
    adicionar_reserva_assento.grid(row=9, column=0, padx=10, pady=10)

    remover_reserva_assento = Button(reserva_assento, text="Remover reserva_assento", command=remove_reserva_assento)
    remover_reserva_assento.grid(row=9, column=1, padx=10, pady=10)

    atualizar_reserva_assento = Button(reserva_assento, text="Atualizar reserva_assento", command=update_reserva_assento)
    atualizar_reserva_assento.grid(row=9, column=2, padx=10, pady=10)

    limpar_campo_reserva_assento = Button(reserva_assento, text="Limpar campos", command=limpar_reserva_assento)
    limpar_campo_reserva_assento.grid(row=9, column=3, padx=10, pady=10)



    #caixas de texto:
    add_numero_trecho = Entry(reserva_assento, width=30)
    add_numero_trecho.grid(row=0, column=1, padx=20)

    add_numero_voo = Entry(reserva_assento, width=30)
    add_numero_voo.grid(row=1, column=1, padx=20)

    add_Data = Entry(reserva_assento, width=30)
    add_Data.grid(row=2, column=1, padx=20)

    add_numero_assento = Entry(reserva_assento, width=30)
    add_numero_assento.grid(row=3, column=1, padx=20)

    add_Nome_cliente = Entry(reserva_assento, width=30)
    add_Nome_cliente.grid(row=4, column=1, padx=20)

    add_Telefone_cliente = Entry(reserva_assento, width=30)
    add_Telefone_cliente.grid(row=5, column=1, padx=20)


    #labels pras caixas de texto
    numero_trecho_label = Label(reserva_assento, text="Número Trecho")
    numero_trecho_label.grid(row=0, column=0)
    
    numero_voo_label = Label(reserva_assento, text="Número Voo")
    numero_voo_label.grid(row=1, column=0)

    Data_label = Label(reserva_assento, text="Data")
    Data_label.grid(row=2, column=0)

    numero_assento_label = Label(reserva_assento, text="Número Assento")
    numero_assento_label.grid(row=3, column=0)
    
    Nome_cliente_label = Label(reserva_assento, text="Nome Cliente")
    Nome_cliente_label.grid(row=4, column=0)

    Telefone_cliente_label = Label(reserva_assento, text="Telefone")
    Telefone_cliente_label.grid(row=5, column=0)

    
    #lista
    lista_reserva_assento = Listbox(reserva_assento, height=8, width=50)
    lista_reserva_assento.grid(row=25, column=0, columnspan=9, rowspan=6, pady=20, padx=20)

    #criando scrollbar
    scrollbar = Scrollbar(reserva_assento)
    scrollbar.grid(row=25, column=8)

    #colocar a scroll na lista
    lista_reserva_assento.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_reserva_assento.yview)

    #ligar a lista ao select
    lista_reserva_assento.bind('<<ListboxSelect>>', selecionar_item)

    populate_list()    
