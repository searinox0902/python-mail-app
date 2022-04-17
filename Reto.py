from tkinter import ttk
from tkinter import *

class Registro:

    def __init__(self, window):
        self.wind = window
        self.wind.title("Cacharreria Universal")

        # Creación de contaimer
        frame = LabelFrame(self.wind, text= "Registro Usuarios")
        frame.grid(row= 0, column= 0, columnspan= 4, pady= 2)
        frame.config(width= 400, height= 200, bd= 0)

        # Seccion nombre
        Label(frame, text= "Nombre: ").grid(row= 1, column= 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row= 1, column= 1, pady= 2)

        # Seccion cedula
        Label(frame, text= "Cedula: ").grid(row= 2, column= 0)
        self.cedula = Entry(frame)
        self.cedula.grid(row= 2, column= 1, pady= 2)

        # Seccion email
        Label(frame, text= "Email: ").grid(row= 3, column= 0)
        self.email = Entry(frame)
        self.email.grid(row= 3, column= 1, pady= 2)

        # Seccion edad
        Label(frame, text= "Edad: ").grid(row= 4, column= 0)
        self.edad = Entry(frame)
        self.edad.grid(row= 4, column= 1, pady= 2)

        # Seccion ciudad
        Label(frame, text= "Ciudad: ").grid(row= 5, column= 0)
        self.ciudad = Entry(frame)
        self.ciudad.grid(row= 5, column= 1, pady= 2)

        # Seccion producto
        Label(frame, text= "Productos: ").grid(row= 6, column= 0)
        self.producto = Entry(frame)
        self.producto.grid(row= 6, column= 1, pady= 2)

        #Seccion boton
        ttk.Button(frame, text= "Guardar").grid(row= 7, columnspan= 2, sticky= W + E)

if __name__ == '__main__':
    window = Tk()
    application = Registro(window)
    window.mainloop()