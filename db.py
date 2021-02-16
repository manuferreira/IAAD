import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self): #conexão com o banco de dados
        self.db = mysql.connector.connect(host = "localhost", 
                                            user = "root",
                                            passwd = "",
                                            database = "companhia_aerea",)
        self.my_cursor = self.db.cursor()


    # métodos referentes a tabela aeroporto
    def mostrar_aeroportos(self):
        self.my_cursor.execute("SELECT * FROM aeroporto")
        linhas = self.my_cursor.fetchall()
        return linhas
    
    def mostrar_passagens(self):
        self.my_cursor.execute("""SELECT Nome_cliente, Dia_da_semana, Companhia_aerea, Horario_partida, Horario_chegada, Numero_assento, Nome, Codigo_aeroporto_chegada 
        FROM reserva_assento  
        left join  voo on reserva_assento.Numero_voo = voo.Numero_voo
        left join instancia_trecho on reserva_assento.Numero_trecho = instancia_trecho.Numero_trecho
        inner join aeroporto on Codigo_aeroporto_partida = Codigo_aeroporto;""")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_aeroporto(self, codigo_aeroporto, nome, cidade, estado):
        self.my_cursor.execute("INSERT INTO aeroporto VALUES (%s, %s, %s, %s)",(codigo_aeroporto, nome, cidade, estado))
        self.db.commit()
        #o API do database pega strings como argumentos e depois converte pro datatype apropriado

    def remover_aeroporto(self, codigo_aeroporto):
        self.my_cursor.execute("DELETE FROM aeroporto WHERE codigo_aeroporto = %s", (codigo_aeroporto,))
        self.db.commit()

    def atualizar_aeroportos(self, codigo_aeroporto, nome, cidade, estado):
        self.my_cursor.execute("UPDATE aeroporto SET nome= %s, cidade= %s, estado= %s WHERE codigo_aeroporto = %s",(nome, cidade, estado, codigo_aeroporto))
        self.db.commit()


    #métodos referentes a tabela voo
    def mostrar_voos(self):
        self.my_cursor.execute("SELECT * FROM voo")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_voo(self, Numero_voo, Companhia_aerea, Dia_da_semana):
        self.my_cursor.execute("INSERT INTO voo VALUES (%s, %s, %s)", (Numero_voo, Companhia_aerea, Dia_da_semana))
        self.db.commit()


    def remover_voo(self, Numero_voo):
        self.my_cursor.execute("DELETE FROM voo WHERE Numero_voo = %s", (Numero_voo,))
        self.db.commit()


    def atualizar_voo(self, Numero_voo, Companhia_aerea, Dia_da_semana):
        self.my_cursor.execute("UPDATE voo SET Companhia_aerea=%s, Dia_da_semana=%s WHERE Numero_voo=%s", (Companhia_aerea, Dia_da_semana, Numero_voo))
        self.db.commit()


    # próxima tabela

    def encerrar_conexao(self): #fecha a conexão com o banco
        self.db.close()











