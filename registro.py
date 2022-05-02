from tkinter import ttk
from tkinter import *
from compra import *



def start(root):
        wind = root
        wind.title("Cacharreria Universal - Registro Usuario")
        wind.resizable(True, True)
        wind.iconbitmap("settings.ico")
        #self.wind.geometry("700x450")

        #variables

        emailVar = StringVar()

        # Creación de frame o contaimer
        frame = Frame()
        frame.pack()
        frame.grid(row= 0, column= 0, columnspan= 4, pady= 2)
        frame.config(width="700", height="450")

        # Seccion nombre
        Label(frame, text= "Registro Usuarios").grid(row= 0, column= 0)
        Label(frame, text= "Nombre: ").grid(row= 1, column= 0)
        name = Entry(frame, textvariable="names")


     
        name.focus()
        name.grid(row= 1, column= 1, pady= 2)

        # Seccion cedula
        Label(frame, text= "Cedula: ").grid(row= 2, column= 0)
        cedula = Entry(frame, textvariable="emailVar")
        cedula.grid(row= 2, column= 1, pady= 2)

        # Seccion email
        Label(frame, text= "Email: ").grid(row= 3, column= 0)
     
        #-------------------------      funciones      -------------------------------""
        
        def validarNumeros(i):
            if type(i) in (int, float, complex):
                print("No es string")
            else:
                print("Es string")


        def validadForm(): 
            nameGet = name.get()
            validarNumeros(nameGet)

    
            
        #---------------------------------------------------------#
        # Seccion edad
        Label(frame, text= "Edad: ").grid(row= 4, column= 0)
        edad = Entry(frame)
        edad.grid(row= 4, column= 1, pady= 2)

        # Seccion ciudad
        Label(frame, text= "Ciudad: ").grid(row= 5, column= 0)
        ciudad = Entry(frame)
        ciudad.grid(row= 5, column= 1, pady= 2)

        # Seccion producto
        Label(frame, text= "Productos: ").grid(row= 6, column= 0)
        producto = Entry(frame)
        producto.grid(row= 6, column= 1, pady= 2)

          #Seccion boton guardar
        ttk.Button(frame, text= "Capturar Datos", command=validadForm).grid(row= 7, columnspan= 2, sticky= W + E, pady=15)

        #Seccion boton guardar
        ttk.Button(frame, text= "Cerrar", command=closed).grid(row= 8, columnspan= 2, sticky= W + E)

        #Seccion boton enviar correos
        ttk.Button(frame, text= "Enviar correo", command=validadForm).grid(row= 9, columnspan= 2, sticky= W + E)



def closed():     
    root.destroy() 
    fun2()


if __name__ == '__main__':
    root = Tk()
    start(root)
    root.mainloop()