import tkinter as tk
from tkinter import messagebox
from vistaProductos import Davista

class VistaUsuario:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")

        self.Datos_de_inicio()

    def Datos_de_inicio(self):
        self.label_nombre_usuario = tk.Label(self.root, text="Nombre de usuario:", bg="lightblue",font=("Arial",12,"bold"))
        self.label_nombre_usuario.pack(pady=10)

        self.entry_nombre_usuario = tk.Entry(self.root,font=("Arial",12))
        self.entry_nombre_usuario.pack(pady=10)

        self.label_contrasena = tk.Label(self.root, text="Contraseña:", bg="lightblue",font=("Arial",12,"bold"))
        self.label_contrasena.pack(pady=10)

        self.entry_contrasena = tk.Entry(self.root, show="*",font=("Arial",12))
        self.entry_contrasena.pack(pady=10)

        self.boton_registrar = tk.Button(self.root, text="Registrarse", command=self.mostrar_ventana_registro, bg="lightgreen",font=("Arial",12,"bold"))
        self.boton_registrar.pack(pady=10)
        self.boton_registrar.config(cursor="hand2")
        self.boton_registrar.bind("<Return>", (lambda event: self.mostrar_ventana_registro()))

        self.boton_iniciar_sesion = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion, bg="lightgreen",font=("Arial",12,"bold"))
        self.boton_iniciar_sesion.pack(pady=10)
        self.boton_iniciar_sesion.config(cursor="hand2")
        self.boton_iniciar_sesion.bind("<Return>", (lambda event: self.iniciar_sesion()))

    def mostrar_ventana_registro(self):
        ventana_registro = tk.Toplevel(self.root)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.geometry("400x300")
        ventana_registro.configure(bg="lightyellow")

        label_nombre_usuario = tk.Label(ventana_registro, text="Nombre de usuario:", bg="lightyellow",font=("Arial",12,"bold"))
        label_nombre_usuario.pack(pady=10)

        entry_nombre_usuario = tk.Entry(ventana_registro,font=("Arial",12))
        entry_nombre_usuario.pack(pady=10)

        label_contrasena = tk.Label(ventana_registro, text="Contraseña:", bg="lightyellow",font=("Arial",12,"bold"))
        label_contrasena.pack(pady=10)

        entry_contrasena = tk.Entry(ventana_registro, show="*",font=("Arial",12,"bold"))
        entry_contrasena.pack(pady=10)

        def registrar_usuario():
            nombre_usuario = entry_nombre_usuario.get()
            contrasena = entry_contrasena.get()
            self.controlador.registrar(nombre_usuario, contrasena)
            ventana_registro.destroy()

        boton_confirmar_registro = tk.Button(ventana_registro, text="Registrar", command=registrar_usuario, bg="lightgreen",font=("Arial",12,"bold"))
        boton_confirmar_registro.pack(pady=10)
        boton_confirmar_registro.config(cursor="hand2")
        boton_confirmar_registro.bind("<Return>", (lambda event: registrar_usuario()))

    def iniciar_sesion(self):
        nombre_usuario = self.entry_nombre_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.controlador.iniciar_sesion(nombre_usuario, contrasena):
            self.root.destroy()  
            self.mostrarVentanaProductos()

    def mostrarVentanaProductos(self):
        app = Davista()

    def iniciar(self):
        self.root.mainloop()