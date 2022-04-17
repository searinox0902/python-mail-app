import pyodbc

try: 
    connection= pyodbc.connect(
        'DRIVER= {SQL server}; SERVER= DESKTOP-7ROJSEE; DATABASE= UNIVERSAL; Trusted_Connection=yes'
    )

    print("Conexión exitosa")

except Exception as ex:
    print(ex)
