from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.geometry("600x400")
raiz.title("Registro Usurios")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))

#-----Seccion de Nombre-----
nombre_label= Label(miFrame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)
cuadro_nombre=Entry(miFrame)
cuadro_nombre.grid(row=1, column=1)

#-----Seccion de Cédula-----
cedula_label=Label(miFrame, text="Cedula: ")
cedula_label.grid(row=2, column=0)
cedula_label.config(padx=10, pady=10)
cuadro_Cedula=Entry(miFrame)
cuadro_Cedula.grid(row=2, column=1)

#-----Seccion de Email-----
email=Label(miFrame, text="Email: ")
email.grid(row=3, column=0)
email.config(padx=10, pady=10)
cuadro_Email=Entry(miFrame)
cuadro_Email.grid(row=3, column=1)

#-----Seccion de Edad-----
edad=Label(miFrame, text="Edad: ")
edad.grid(row=4, column=0)
edad.config(padx=10, pady=10)
cuadro_Edad=Entry(miFrame)
cuadro_Edad.grid(row=4, column=1)

#-----Seccion de Ciudad-----
ciudad=Label(miFrame, text="Ciudad: ")
ciudad.grid(row=5, column=0)
ciudad.config(padx=10, pady=10)
cuadro_Ciudad=Entry(miFrame)
cuadro_Ciudad.grid(row=5, column=1)

#-----Seccion boton-----



raiz.mainloop()