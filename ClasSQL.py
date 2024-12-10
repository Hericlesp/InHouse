import sqlite3 as sq
import hashlib as sh

class SQLITE: 

    def __init__(self, nomeBanco:str):
        self.nomeBanco = nomeBanco

    def conectarBanco(self):
        database = sq.connect(f'assets/databases/{self.nomeBanco}.db')
        cursor = database.cursor()

        return database, cursor
    
    def criarTabela(self, nomeTabela:str , Colunas:list, ColunasTipo: list):

        if type(Colunas) == list and type(ColunasTipo) == list:
            if len(Colunas) == len(ColunasTipo):

                database, cursor = self.conectarBanco()
                colunas=[]

                for i in range(len(Colunas)):
                    colunas.append(f'{Colunas[i]} {ColunasTipo[i]}')

                ColunasSQL = ','.join(colunas)

                cursor.execute(f'CREATE TABLE IF NOT EXISTS {nomeTabela} ({ColunasSQL})')

                database.commit()
                database.close()

            else:
                print('Impossivel crear tabela')

        else:
            print('Impossivel crear tabela')

    def inserirDados(self, nomeTabela: str, Colunas: list, dados: list):

        if type(Colunas) == list and type(dados) == list:
            if len(Colunas) == len(dados):

                database, cursor = self.conectarBanco()
                Dados =[]

                for dado in Dados:
                    if type(dado) == str:
                        Dados.append(f"'{dado}'")

                else:
                    Dados.append(str(dado))

                ColunaSQL= ','.join(Colunas)
                DadoSQL = ','.join(Dados)

                cursor.execute(f'INSERT INTO {nomeTabela} ({ColunaSQL} VALUES ({DadoSQL}))')

                database.commit()
                database.close()

            else:
               print('Impossivel salvar os dados') 
               
        else:
             print('Impossivel salvar os dados') 
