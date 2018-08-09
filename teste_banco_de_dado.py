import sqlite3
import time
import datetime


# conectando...
connection = sqlite3.connect('bancoDeDados.db')
# definido um cursor
c = connection.cursor()

def create_table():
    # Criando a Tabela de Dados
    c.execute('CREATE TABLE IF NOT EXISTS dados (id INTEGER, unix REAL, keyword TEXT, datestamp TEXT, value REAL )')

create_table()

def dataentry():

    # Inserindo dados:
    #c.execute('INSERT INTO dados VALUES (1, 1365921, "Python Sentiment", "2013-04-14 10:09:41", 5)')
    #c.execute('INSERT INTO dados VALUES (2, 1365922, "Python Sentiment", "2013-04-14 10:10:41", 6)')
    #c.execute('INSERT INTO dados VALUES (3, 1365923, "Python Sentiment", "2013-04-14 10:11:41", 7)')
    c.execute('INSERT INTO dados VALUES (4, 1365924, "Python Sentiment", "2013-04-14 10:12:41", 8)')

    data_id = 4
    keyword = 'Python'
    value = 4

    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute('INSERT INTO dados (id, unix, keyword, datestamp, value) VALUES (?, ?, ?, ?, ?)',\
              (data_id, time.time(), keyword, date, value))

    # Gravar no Banco de Dados:
    connection.commit()

dataentry()


connection.close()
