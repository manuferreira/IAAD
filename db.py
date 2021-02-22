import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self): #conexão com o banco de dados
        self.db = mysql.connector.connect(host = "localhost", 
                                            user = "root",
                                            passwd = "manussa1",
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


    #metodos referente a Tabela trecho_voo

    def mostrar_trecho_voo(self):
        self.my_cursor.execute("SELECT * FROM trecho_voo")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_trecho_voo(self, Numero_trecho, Numero_voo, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida_previsto, Horario_chegada_previsto):
        self.my_cursor.execute("INSERT INTO trecho_voo VALUES (%s, %s, %s, %s, %s, %s)", (Numero_trecho, Numero_voo, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida_previsto, Horario_chegada_previsto))
        self.db.commit()


    def remover_trecho_voo(self, Numero_trecho):
        self.my_cursor.execute("DELETE FROM trecho_voo WHERE Numero_trecho = %s", (Numero_trecho,))
        self.db.commit()
       

    def atualizar_trecho_voo(self, Numero_trecho, Numero_voo, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida_previsto, Horario_chegada_previsto):
        self.my_cursor.execute("UPDATE trecho_voo SET Codigo_aeroporto_partida=%s, Codigo_aeroporto_chegada=%s, Horario_partida_previsto=%s, Horario_chegada_previsto=%s WHERE Numero_voo = %s AND Numero_trecho=%s", (Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida_previsto, Horario_chegada_previsto, Numero_voo, Numero_trecho))
        self.db.commit()


# métodos referentes a tabela tarifa
    def mostrar_tarifas(self):
        self.my_cursor.execute("SELECT * FROM tarifa")
        linhas = self.my_cursor.fetchall()
        return linhas


    def inserir_tarifa(self, Numero_voo, Codigo_tarifa, Quantidade, Restricoes):
        self.my_cursor.execute("INSERT INTO tarifa VALUES (%s, %s, %s, %s)",
                               (Numero_voo, Codigo_tarifa, Quantidade, Restricoes))
        self.db.commit()


    def remover_tarifa(self, Codigo_tarifa):
        self.my_cursor.execute("DELETE FROM tarifa WHERE Codigo_tarifa = %s", (Codigo_tarifa,))
        self.db.commit()


    def atualizar_tarifa(self, Numero_voo, Codigo_tarifa, Quantidade, Restricoes):
        self.my_cursor.execute("UPDATE tarifa SET Quantidade = %s, Restricoes = %s WHERE Numero_voo = %s AND Codigo_tarifa = %s",(Quantidade, Restricoes, Numero_voo, Codigo_tarifa))
        self.db.commit()
        

# Métodos referentes a tabela tipo_aeronave 
    def mostrar_tipo_aeronave(self):
        self.my_cursor.execute("SELECT * FROM tipo_aeronave")
        linhas = self.my_cursor.fetchall()
        return linhas


    def adicionar_tipo_aeronave(self, Nome_tipo_aeronave, Qtd_max_assentos, Companhia):
        self.my_cursor.execute("INSERT INTO tipo_aeronave VALUES (%s, %s, %s)",
                               (Nome_tipo_aeronave, Qtd_max_assentos, Companhia))
        self.db.commit()


    def remover_tipo_aeronave(self, Nome_tipo_aeronave):
        self.my_cursor.execute("DELETE FROM tipo_aeronave WHERE Nome_tipo_aeronave = %s", (Nome_tipo_aeronave,))
        self.db.commit()


    def atualizar_tipo_aeronave(self, Nome_tipo_aeronave, Qtd_max_assentos, Companhia):
        self.my_cursor.execute(
            "UPDATE tipo_aeronave SET Qtd_max_assentos = %s, Companhia = %s WHERE Nome_tipo_aeronave = %s", (Qtd_max_assentos, Companhia, Nome_tipo_aeronave))
        self.db.commit()


# métodos referentes a tabela pode_pousar
    def mostrar_pode_pousar(self):
        self.my_cursor.execute("SELECT * FROM pode_pousar")
        linhas = self.my_cursor.fetchall()
        return linhas


    def adicionar_pode_pousar(self, Nome_tipo_aeronave, Codigo_aeroporto):
        self.my_cursor.execute("INSERT INTO pode_pousar VALUES (%s, %s)", (Nome_tipo_aeronave, Codigo_aeroporto))
        self.db.commit()


    def remover_pode_pousar(self, Nome_tipo_aeronave, Codigo_aeroporto):
        self.my_cursor.execute("DELETE FROM pode_pousar WHERE Nome_tipo_aeronave=%s AND Codigo_aeroporto=%s",(Nome_tipo_aeronave, Codigo_aeroporto))


    #metodos referente a Tabela instancia_trecho

    def mostrar_instancia_trecho(self):
        self.my_cursor.execute("SELECT * FROM instancia_trecho")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_instancia_trecho(self, Numero_trecho, Numero_voo, Data, Numero_assentos, Codigo_aeronave, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida, Horario_chegada):
        self.my_cursor.execute("INSERT INTO instancia_trecho VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Numero_voo, Numero_trecho, Data, Numero_assentos, Codigo_aeronave, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida, Horario_chegada))
        self.db.commit()


    def remover_instancia_trecho(self, Numero_trecho):
        self.my_cursor.execute("DELETE FROM instancia_trecho WHERE Numero_trecho = %s", (Numero_trecho,))
        self.db.commit()


    def atualizar_instancia_trecho(self, Numero_trecho, Numero_voo, Data, Numero_assentos, Codigo_aeronave, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida, Horario_chegada):
        self.my_cursor.execute("UPDATE instancia_trecho SET Numero_assentos=%s, Codigo_aeronave=%s Codigo_aeroporto_partida=%s, Codigo_aeroporto_chegada=%s, Horario_partida=%s, Horario_chegada=%s WHERE Numero_voo = %s AND Numero_trecho=%s AND Data=%s,", ( Numero_assentos, Codigo_aeronave, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida, Horario_chegada, Numero_voo, Numero_trecho, Data))
        self.db.commit()

    #métodos referentes a tabela aeronave
    def mostrar_aeronave(self):
        self.my_cursor.execute("SELECT * FROM aeronave")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_aeronave(self, Codigo_aeronave, Numero_total_assentos, Tipo_aeronave):
        self.my_cursor.execute("INSERT INTO aeronave VALUES (%s, %s, %s)", (Codigo_aeronave, Numero_total_assentos, Tipo_aeronave))
        self.db.commit()


    def remover_aeronave(self, Codigo_aeronave):
        self.my_cursor.execute("DELETE FROM aeronave WHERE Codigo_aeronave = %s", (Codigo_aeronave,))
        self.db.commit()


    def atualizar_aeronave(self, Codigo_aeronave, Numero_total_assentos, Tipo_aeronave):
        self.my_cursor.execute("UPDATE aeronave SET Numero_total_assentos=%s, Tipo_aeronave=%s WHERE Codigo_aeronave=%s", (Numero_total_assentos, Tipo_aeronave, Codigo_aeronave))
        self.db.commit()    
    
    #metodos referente a Tabela reserva_assento

    def mostrar_reserva_assento(self):
        self.my_cursor.execute("SELECT * FROM reserva_assento")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_reserva_assento(self, Numero_trecho, Numero_voo, Data, Numero_assento, Nome_cliente, Telefone_cliente):
        self.my_cursor.execute("INSERT INTO reserva_assento VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Numero_trecho, Numero_voo, Data, Numero_assento, Nome_cliente, Telefone_cliente))
        self.db.commit()


    def remover_reserva_assento(self, Numero_trecho):
        self.my_cursor.execute("DELETE FROM reserva_assento WHERE Numero_trecho = %s", (Numero_trecho,))
        self.db.commit()


    def atualizar_reserva_assento(self, Numero_trecho, Numero_voo, Data, Numero_assento, Nome_cliente, Telefone_cliente):
        self.my_cursor.execute("UPDATE reserva_assento SET Numero_assentos=%s, Nome_cliente=%s Telefone_cliente=%s WHERE Numero_voo = %s AND Numero_trecho=%s AND Data=%s,", ( Numero_assento, Nome_cliente, Telefone_cliente, Numero_voo, Numero_trecho, Data))
        self.db.commit()

    def encerrar_conexao(self): #fecha a conexão com o banco
        self.db.close()










