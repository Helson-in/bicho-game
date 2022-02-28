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
