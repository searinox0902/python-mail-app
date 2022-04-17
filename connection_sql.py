
import pyodbc

try: 
    connection= pyodbc.connect(
        'DRIVER={SQL server}; SERVER=SVARGAS; DATABASE=UNIVERSAL; Trusted_Connection=yes'
    )

    print("Conexión exitosa")

except Exception as ex:
    print(ex)
