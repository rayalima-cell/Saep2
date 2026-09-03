import mysql.connector
from config import DB_CONFIG

def conectar():
    conexao = mysql.connector.connect(**DB_CONFIG)

def criar_tabela():
    conexao = None
    try:
        conexao = conectar()
