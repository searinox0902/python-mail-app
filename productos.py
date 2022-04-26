from tkinter import ttk
from tkinter import *


class Producto:

    def __init__(self, window):
        self.wind = window
        self.wind.title("Cacharreria Universal")
        window.geometry('250x250')

        # Creación de frame o contaimer
        frame = LabelFrame(self.wind, text= "Registro Productos")
        frame.grid(row= 0, column= 0, columnspan= 8, pady= 5, padx=5)
        frame.config(width=200, height=200)
                
        # Seccion nombre
        Label(frame, text= "Nombre: ").grid(row= 1, column= 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row= 1, column= 1, pady= 2)

        # Seccion cedula
        Label(frame, text= "Descripción: ").grid(row= 2, column= 0)
        self.cedula = Entry(frame)
        self.cedula.grid(row= 2, column= 1, pady= 2)

        # Seccion email
        Label(frame, text= "Precio: ").grid(row= 3, column= 0)
        self.email = Entry(frame)
        self.email.grid(row= 3, column= 1, pady= 2)

        # Seccion edad
        Label(frame, text= "Ced. Usuario: ").grid(row= 4, column= 0)
        self.edad = Entry(frame)
        self.edad.grid(row= 4, column= 1, pady= 2)

       

        #Seccion boton Registro usuario
        ttk.Button(frame, text= "Registrar Compra").grid(row= 7, columnspan= 2, sticky= W + E)

        #Seccion boton enviar correos
        ttk.Button(frame, text= "Registrar Usuario").grid(row= 8, columnspan= 2, sticky= W + E)
        
        #Seccion boton enviar correos
        ttk.Button(frame, text= "Enviar correos").grid(row= 9, columnspan= 2, sticky= W + E)


if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    window.mainloop()