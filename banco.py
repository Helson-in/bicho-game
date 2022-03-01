<<<<<<< HEAD
import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+"\\banco_bolao.db"

# Criação do banco de dados / CONNECT
def ConexaoBanco1():
    banco1 = None
    try:
        banco1 = sqlite3.connect("banco_bolao.db")
    except Error as ex:
        print(ex)
    return(banco1)

def dql(query): #SELECT
    vcon=ConexaoBanco1
    cursor1=vcon.cursor()
    cursor1.execute(query)
    res=cursor1.fetchall()
    vcon.close()
    return res

def dml(query): # INSERT, UPDATE, SELECT
    try:
        vcon=ConexaoBanco1
        cursor1=vcon.cursor()
        cursor1.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)



#####################################################################################################################################################################################################






=======
import sqlite3
from sqlite3 import Error
import os

path_app = os.path.dirname(__file__)
name_bank = path_app + "\\databank.db"


def connection_bank():
    const = None
    try:
        const = sqlite3.connect(name_bank)
    except Error as ex:
        print(ex)
    return const


def dql(query):  # select
    view_connection = connection_bank()
    cursor = view_connection.cursor()
    cursor.execute(query)
    result - cursor.fetchall()  # retorna todos resultados
    view_connection.close()
    return result


def dml(query): # insert, update, delete
    try:
        view_connection = connection_bank()
        connection = view_connection.cursor()
        connection.execute(query)
        view_connection.commit()
        view_connection.close()
    except Error as ex:
        print(ex)
>>>>>>> e45b9c5976ba6b89c14a8de58c7c9db4eb127864
