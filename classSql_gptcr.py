import sqlite3 as sq
import hashlib as sh
import os

class SQLITE: 
    def __init__(self, nomeBanco: str):
        self.nomeBanco = nomeBanco

    def conectarBanco(self):
        os.makedirs('assets/databases', exist_ok=True)
        database = sq.connect(f'assets/databases/{self.nomeBanco}.db')
        cursor = database.cursor()
        return database, cursor

    def criarTabela(self, nomeTabela: str, Colunas: list, ColunasTipo: list):
        if isinstance(Colunas, list) and isinstance(ColunasTipo, list) and len(Colunas) == len(ColunasTipo):
            database, cursor = self.conectarBanco()
            colunas = [f'{Colunas[i]} {ColunasTipo[i]}' for i in range(len(Colunas))]
            ColunasSQL = ', '.join(colunas)
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {nomeTabela} ({ColunasSQL})')
            database.commit()
            database.close()
        else:
            print('Impossível criar tabela: listas incompatíveis ou inválidas.')

    def inserirDados(self, nomeTabela: str, Colunas: list, dados: list):
        if isinstance(Colunas, list) and isinstance(dados, list) and len(Colunas) == len(dados):
            database, cursor = self.conectarBanco()
            Dados = [f"'{dado}'" if isinstance(dado, str) else str(dado) for dado in dados]
            ColunaSQL = ', '.join(Colunas)
            DadoSQL = ', '.join(Dados)
            cursor.execute(f'INSERT INTO {nomeTabela} ({ColunaSQL}) VALUES ({DadoSQL})')
            database.commit()
            database.close()
        else:
            print('Impossível salvar os dados: listas incompatíveis ou inválidas.')

    def editarDados(self, nomeTabela: str, Coluna: str, valor: str, conditions: str = ''):
        database, cursor = self.conectarBanco()
        sql = f'UPDATE {nomeTabela} SET {Coluna} = {valor}' + (f' WHERE {conditions}' if conditions else '')
        cursor.execute(sql)
        database.commit()
        database.close()

    def apagarDados(self, nomeTabela: str, conditions: str = ''):
        database, cursor = self.conectarBanco()
        sql = f'DELETE FROM {nomeTabela}' + (f' WHERE {conditions}' if conditions else '')
        cursor.execute(sql)
        database.commit()
        database.close()

    def verdados(self, nomeTabela: str, Colunas='*', conditions: str = ''):
        database, cursor = self.conectarBanco()
        ColunaSQL = ', '.join(Colunas) if isinstance(Colunas, list) else Colunas
        sql = f'SELECT {ColunaSQL} FROM {nomeTabela}' + (f' WHERE {conditions}' if conditions else '')
        cursor.execute(sql)
        dados = cursor.fetchall()
        database.close()
        return dados

    def encrypt_password(self, senha: str):
        hash = sh.sha512()
        hash.update(bytes(senha, 'UTF-8'))
        return hash.hexdigest()

sqlite = SQLITE('users')
sqlite.criarTabela('usuarios',['nome','idade','senha'], ['TEXT','INTEGER','TEXT'])

# nao criou o arquivo database

