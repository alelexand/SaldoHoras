import sqlite3
from Arquivo.consulta import Consulta


class Banco:
    def __init__(self):
        print("INICIANDO COLETA DE DADOS NA PLANILHA")
        print("INSERINDO OS DADOS NO BANCO DE DADOS")
        self.banco = sqlite3.connect(fr"T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Robô_folha\dbfolha\DB_folha.db")
        self.cursor = self.banco.cursor()

    def horas(self):
        hora = Consulta()
        lista = hora.horas()
        for dados in lista:
            self.cursor.execute(f"UPDATE registro SET horas_saldo = '{dados[1]}' WHERE nome = '{dados[0]}'")
            self.banco.commit()


