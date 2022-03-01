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






