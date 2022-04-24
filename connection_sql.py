import pyodbc

class ConnectionBD:
    
    def __init__(self):

        try: 
            connection= pyodbc.connect(
                'DRIVER={SQL server}; SERVER=DESKTOP-7ROJSEE; DATABASE=UNIVERSAL; Trusted_Connection=yes'
            )
            print("Conexión exitosa")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuarios")
            row=cursor.fetchone()
            print(row) 
            rows=cursor.fetchall()
            for row in rows:
                print(rows)


        except Exception as ex:
            print(ex)
        finally:
            connection.close()
            print("Sesion finalizada")