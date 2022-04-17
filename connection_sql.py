from sqlite3 import Cursor
import pyodbc

try: 
    connection= pyodbc.connect(
        'DRIVER={SQL server}; SERVER=DESKTOP-7ROJSEE; DATABASE=UNIVERSAL; Trusted_Connection=yes'
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    row=cursor.fetchone()
    cursor.execute("SELECT * FROM usuarios")
    print(row) 
    rows=cursor.fetchall()
    for row in rows:
        print(rows)

except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Sesion finalizada")