import sqlite3 as sq
import hashlib as sh

class SQLITE: 

    def __init__(self, nomeBanco:str):
        self.nomeBanco = nomeBanco

    def conectarBanco(self):
        database = sq.connect(f'assets/databases/{self.nomeBanco}.db')
        cursor = database.cursor()

        return database, cursor
    
    def criarTabela(self, nomeTabela:str , Colunas: list, ColunasTipo: list):

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

    def editarDados(self, nomeTabela: str, Coluna: str, valor:str, conditions: str=''):

        database, cursor = self.conectarBanco()
        
        if conditions == '':
            cursor.execute(f'UPDATE TABLE {nomeTabela} SET {Coluna} = {valor}')

        else:  
            cursor.execute(f'UPDATE TABLE {nomeTabela} SET {Coluna} = {valor} WHERE {conditions}')

        database.commit()
        database.close()


    def apagarDados(self, nomeTabala:str, conditions: str = ''):

        database, cursor = self.conectarBanco()

        if conditions == '':
            cursor.execute(f'DELETE TABLE {nomeTabala}')

        else:
            cursor.execute(f'DELETE TABLE {nomeTabala} WHERE {conditions}')

        database.commit()
        database.close()

    def verdados(self, nomeTabela: str, Colunas: list= '*', conditions: str= '' ):

        database, cursor = self.conectarBanco()

        ColunaSQL = ','.join(Colunas)

        if conditions == '':
            cursor.execute(f'SELECT {ColunaSQL} FROM {nomeTabela}')

        else:
            cursor.execute(f'SELECT {ColunaSQL} FROM {nomeTabela} WHERE {conditions}')

        dados = cursor.fetchall()

        database.commit()
        database.close()

        return dados
    
    def encrypt_password(self, senha: str):
        
        hash= sh.sha512()

        hash.update(bytes(senha,'UTF-8'))

        password_hashed= hash.hexdigest()

        return password_hashed
    
            # print(SQLITE('users').encrypt_password('senha123') ) printar na tela o codigo cripytografado.


sqlite = SQLITE('users')
sqlite.criarTabela('usuarios',['nome','idade', 'senha'], ['TEXT', 'INTEGER', 'TEXT'])
