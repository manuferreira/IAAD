import mysql.connector
from tkinter import *

root = Tk() #janela
root.title('Companhia Aérea')
root.geometry("400x400")

mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    passwd = "",
    database = "companhia_aerea",
)

my_cursor = mydb.cursor()

# função de limpar campos
def limpar_campos():
    codigo_aeronave_campo.delete(0, END)
    numero_total_assentos_campo.delete(0, END)
    tipo_aeronave_campo.delete(0, END)

def adicionar_aeronave():
    query = "INSERT INTO aeronave (codigo_aeronave, numero_total_assentos, tipo_aeronave) VALUES (%s, %s, %s)"

    values = (codigo_aeronave_campo.get(), numero_total_assentos_campo.get(), tipo_aeronave_campo.get())

    my_cursor.execute(query, values)

    mydb.commit()

    #limpar os campos
    limpar_campos()



# caixas de texto
codigo_aeronave_campo = Entry(root, width=30)
codigo_aeronave_campo.grid(row=0, column=1, padx=20)

numero_total_assentos_campo = Entry(root, width=30)
numero_total_assentos_campo.grid(row=1, column=1, padx=20)

tipo_aeronave_campo = Entry(root, width=30)
tipo_aeronave_campo.grid(row=2, column=1, padx=20)


#labels pras caixas de texto
codigo_aeronave_label = Label(root, text="Codigo Aeronave")
codigo_aeronave_label.grid(row=0, column=0)

numero_total_assentos_label = Label(root, text="Total assentos")
numero_total_assentos_label.grid(row=1, column=0)

tipo_aeronave_label = Label(root, text="Tipo aeronave")
tipo_aeronave_label.grid(row=2, column=0)


# botões
add_aeronave = Button(root, text="Adicionar aeronave", command=adicionar_aeronave)
add_aeronave.grid(row=7, column=0, padx=10, pady=10)

apagar_campos = Button(root, text="Limpar campos", command=limpar_campos)
apagar_campos.grid(row = 7, column=1, padx=10, pady=10)


root.mainloop()



