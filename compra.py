
from tkinter import *



def screen3(root):
        wind = root
        wind.title("Registro compra")
        root.geometry('250x250')

        # Creación de frame o contaimer
        frame = LabelFrame(wind, text= "Registro Productos")
        frame.grid(row= 0, column= 0, columnspan= 8, pady= 5, padx=5)
        frame.config(width=200, height=200)
                
        # Seccion nombre
        Label(frame, text= "Nombre: ").grid(row= 1, column= 0)
        name = Entry(frame)
        name.focus()
        name.grid(row= 1, column= 1, pady= 2)

        # Seccion cedula
        Label(frame, text= "Descripción: ").grid(row= 2, column= 0)
        cedula = Entry(frame)
        cedula.grid(row= 2, column= 1, pady= 2)

        # Seccion email
        Label(frame, text= "Precio: ").grid(row= 3, column= 0)
        email = Entry(frame)
        email.grid(row= 3, column= 1, pady= 2)

        # Seccion edad
        Label(frame, text= "Ced. Usuario: ").grid(row= 4, column= 0)
        edad = Entry(frame)
        edad.grid(row= 4, column= 1, pady= 2)

       

        #Seccion boton Registro usuario
        ttk.Button(frame, text= "Registrar Compra").grid(row= 7, columnspan= 2, sticky= W + E)

        #Seccion boton enviar correos
        ttk.Button(frame, text= "Registrar Usuario").grid(row= 8, columnspan= 2, sticky= W + E)
        
        #Seccion boton enviar correos
        ttk.Button(frame, text= "Enviar correos").grid(row= 9, columnspan= 2, sticky= W + E)



def fun2():
    root=Tk()
    screen3(root)
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    screen3(root)
    root.mainloop()