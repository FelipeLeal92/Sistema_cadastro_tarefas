# Conectar o banco de dados
import sqlite3

def conectar(): # Executa o banco de dados
     return sqlite3.connect('tarefas.db') 
    