from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry


class EnvioMail:

    def __init__(self, window):
    
        self.wind = window
        self.wind.title("Cacharreria Universal: Envio Mail")

        # Creación de container
        frame = LabelFrame(self.wind, text= "Envio Mail", pady=10)
        frame.grid(row= 1, column= 0, columnspan= 4, pady= 2, padx=10)
        frame.config(width=800, height=800, bd= 0)

        # date init 
        cal = DateEntry(frame, width= 16, background= "#696969", foreground= "#696969", bd=1)
        cal.grid(row=2, column= 0, pady= 4)
        
        # date end
        cal = DateEntry(frame, width= 16, background= "#696969", foreground= "#696969", bd=1)
        cal.grid(row=3, column= 0, pady= 4)

        # Seccion ciudad
        Label(frame, text= "Ciudad: ").grid(row= 4, column= 0)
        self.ciudad = Entry(frame)
        self.ciudad.grid(row= 5, column= 0, pady= 2)

        # Seccion producto
        Label(frame, text= "Id Producto: ").grid(row=6, column= 0)
        self.producto = Entry(frame)
        self.producto.grid(row= 7, column= 0, pady= 2)

        #Seccion boton
        ttk.Button(frame, text= "Enviar Mail").grid(row= 8, columnspan= 2, sticky= W + E, pady=10)

if __name__ == '__main__':
    window = Tk()
    application = EnvioMail(window)
    window.mainloop()