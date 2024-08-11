import tkinter as ventana
from tkinter import messagebox

class Vista:
    def __init__(self):
        pass

    def crearVentana(self):
        self.ventanaCrear=ventana.Tk()
        self.ventanaCrear.title("Login")
        self.ventanaCrear.geometry("400x300")
        self.ventanaCrear.config(background="#3f79f2")
        self.usuario=ventana.StringVar()
        self.contraseña=ventana.StringVar()
        labelUsuario=ventana.Label(text="ingrese su usuario",width=30,height=2,font=("Arial",12,"bold"))
        labelUsuario.pack(padx=10,pady=10)
        labelUsuario.config(background="#bfffff")
        entryUsuario=ventana.Entry(textvariable=self.usuario,font=("Arial",12),width=30)
        entryUsuario.pack(padx=10,pady=10)
        labelContraseña=ventana.Label(text="ingrese la contraseña",width=30,height=2,font=("Arial",12,"bold"))
        labelContraseña.pack(padx=10,pady=10)
        labelContraseña.config(background="#bfffff")
        entryContraseña=ventana.Entry(textvariable=self.contraseña,show="*",font=("Arial",12),width=30)
        entryContraseña.pack(padx=10,pady=10)
        boton=ventana.Button(text="iniciar sesion", command=lambda:self.tomarDatos(self.usuario,self.contraseña))
        boton.pack()


        self.ventanaCrear.mainloop()

    def tomarDatos(self,datoUsuario,datoContraseña):
        messagebox.showinfo("info","inicio de sesion exitoso")
        usuario=datoUsuario.get()
        contraseña=datoContraseña.get()
        datos=[usuario,contraseña]



vision=Vista()
vision.crearVentana()