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

    

#Botões pra tela principal
aeroporto = Button(root, text="Dados aeroporto", command=tabela_aeroporto)
aeroporto.grid(row=20, column=0, padx=10)

voo = Button(root, text="Dados voo", command=tabela_voo)
voo.grid(row=20, column=1, padx=10)



root.mainloop()
mydb.encerrar_conexao()




