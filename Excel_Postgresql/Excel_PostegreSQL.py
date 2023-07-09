import psycopg2
import pandas as pd
import time

host = 'localhost'
dbname = 'databaseName'
user = 'userName'
password = '*******'

con_string = 'host={0} user={1} dbname={2} password={3}'.format(host, user, dbname, password)

con = psycopg2.connect(con_string)

print('conectado')

cursor = con.cursor()

cursor.execute("CREATE TABLE products6 (id serial PRIMARY KEY, name varchar(50), brand varchar(30), weight INTEGER, price INTEGER );")

table = pd.read_excel("C:\")

for linha in table.index:
    a = table['prod'][linha]
    b = table['marca'][linha]
    c = table['prço'][linha]
    d = table['peso'][linha]

    c2 = str(c)
    d2 = str(d)

    dad_stm = ("INSERT INTO products6 (name, brand, weight, price)"
               "VALUES (%s, %s, %s, %s)")
    dados = (a, b, c2, d2)
    cursor.execute(dad_stm, dados)
    time.sleep(0.1)

con.commit()
cursor.close()
con.close()
print("OK")
