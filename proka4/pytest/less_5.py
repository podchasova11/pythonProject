import sqlite3
import pytest

def connect_data_base():
    connection = sqlite3.connect("test.db")
    print("ы подключили ДБ")
    return connection
cursor = connect_data_base().cursor()
cursor.execute("SELECT *FROM employees")
cursor.fetchall()  # собери все записи и запринть
connect_data_base().close()   #закрывает БД

