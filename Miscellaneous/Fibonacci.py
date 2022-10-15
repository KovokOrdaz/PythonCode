#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ing. Ordaz, Mario"
__copyright__ = "Todos los Derechos Reserdos 2020, Ordaz, Mario"
__credits__ = "KodeZ"

__license__ = "GPL"
__version__ = "0.0.0A"
__maintainer__ = "Ing. Ordaz, Mario"
__email__ = "Marioordazv@gmail.com"
__status__ = "Develover"

try:
    from tkinter import *
    print("Importado Tkinter Satisfactoriamente...")
except ImportError:
    try:
        from Tkinter import *
        print("Importado Tkinter Satisfactoriamente...")
    except:
        print("Error 0.0.1: No se pudo establecer conexion con el Tkinder, Porfavor Comunicarse con su Empresa...")
try:
    from tkinter import messagebox
    from tkinter import ttk
    from tkinter.ttk import Style

    print("Libreria de Python Importado Satisfactoriamente...")
except:
    print("Error 0.0.2: No se logro Importar Libreria de Python...")

# Modules
try:
    print("Modulos de Python Importado Satisfactoriamente...")
except:
    print("Error 0.0.3: No se logro Importar Modulos de Python...")

class fibonacci(object):
    """docstring for fibonacci"""
    def __init__(self, value_a, value_b):
        self.a = value_a
        self.b = value_b
        self.c = 0

    def view(self, window):
        print("Vistas Importado Satisfactoriamente...")
        self.window_main=window
        self.window_main.title("Fibonacci 0.0.0")
        self.window_main.configure(background="white")
        self.x = (self.window_main.winfo_screenwidth() - self.window_main.winfo_reqwidth()) / 2
        self.y = (self.window_main.winfo_screenheight() - self.window_main.winfo_reqheight()) / 2
        self.h=280
        self.window_main.geometry("%dx%d+%d+%d" % (320,self.h,self.x,self.y))
        
        self.window_main.resizable(0,0)

        title_app=Label(self.window_main, text="Fibonacci 0.0.0")
        title_app.place(x=0, y=5)
        title_app.config(font=("Calibri",38))
        
        label_value=Label(self.window_main, text="Detener en: ")
        label_value.config(fg="black", bg="white", font=("Calibri",20))
        label_value.place(x=20, y=100)

        validation=self.window_main.register(self.only_numbers)
        self.input_value=Entry(self.window_main, justify=CENTER, validate="key", validatecommand=(validation, "%S"))
        self.input_value.focus()
        self.input_value.place(x=170, y=110)
        self.input_value.insert(0,"0")

        self.button_login=Button(self.window_main, text="Calcular", command=lambda:(self.controller(self.input_value.get())), bg="black", fg="white", font=("Calibri",18))
        self.button_login.place(x=110, y=160)

        self.hcopy=self.h-15
        self.copy_right=Label(self.window_main, text="TODOS LOS DERECHOS RESERVADOS © ING. ORDAZ, MARIO")
        self.copy_right.config(fg="gray", bg="white", font=("Calibri",6))
        self.copy_right.place(x=60, y=self.hcopy)

    def only_numbers(self, char):
        return char.isdigit()

    def model(self, value_c):
        value_max= int(value_c)
        if self.a != 0 and self.b != 1:
            self.a = 0
            self.b = 1
        px=60
        py=220
        Label(self.window_main, text=self.a).place(x=20, y=220)
        Label(self.window_main, text=self.b).place(x=60, y=220)
        while self.c<value_max:
            px=px+40
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
            print(self.c)
            if px>280:
                px = 20
                py = py +20
                Label(self.window_main, text=self.c).place(x=px, y=py)
                self.h=self.h+20
                self.window_main.geometry("%dx%d+%d+%d" % (320,self.h,self.x,self.y))
                self.hcopy=self.h-15
                self.copy_right.place(x=60, y=self.hcopy)
            else:
                Label(self.window_main, text=self.c).place(x=px, y=py)

            

    def controller(self, value_d):
        print("Controller Active...")
        if len(value_d) != 0:
            value_e= int(value_d)
            if value_e>1:
                print(value_d," is Valide")
                self.model(value_d)
            else:
               print(value_d," is Not Valide")
               messagebox.showwarning("Numero Invalido", "Debe Ingresar Un Numero Mayor a 1") 
        else:
            print(value_d," is Empty")
            messagebox.showwarning("Casilla Vacia", " No Debar la Casilla Vacia")

if __name__ == '__main__':
    window = Tk()
    application = fibonacci(0, 1)
    application.view(window)

    window.mainloop()
