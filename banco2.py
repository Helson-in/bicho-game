import sqlite3
from sqlite3 import Error
import os

pastaApp_2 = os.path.dirname(__file__)
nomeBanco_2 = pastaApp_2+"\\banco_numeros.db"

def ConexaoBanco2():  # Conectar com o banco
    banco2 = None
    try:
        banco2 = sqlite3.connect("banco_numeros.db")
    except Error as ex:
        print(ex)
    return(banco2)

def dql_2(query): #SELECT
    vcon2=ConexaoBanco2
    cursor2=vcon2.cursor()
    cursor2.execute(query)
    res=cursor2.fetchall()
    vcon2.close()
    return res

def dml_2(query): # INSERT, UPDATE, SELECT
    try:
        vcon2=ConexaoBanco2
        cursor2=vcon2.cursor()
        cursor2.execute(query)
        vcon2.commit()
        vcon2.close()
    except Error as ex:
        print(ex)