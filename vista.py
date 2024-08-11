import tkinter as tk
from tkinter import messagebox

class VistaUsuario:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")
        self.root.configure(bg="lightblue")

        self.Datos_de_inicio()

    def Datos_de_inicio(self):
        self.label_nombre_usuario = tk.Label(self.root, text="Nombre de usuario:", bg="lightblue")
        self.label_nombre_usuario.pack(pady=5)

        self.entry_nombre_usuario = tk.Entry(self.root)
        self.entry_nombre_usuario.pack(pady=5)

        self.label_contrasena = tk.Label(self.root, text="Contraseña:", bg="lightblue")
        self.label_contrasena.pack(pady=5)

        self.entry_contrasena = tk.Entry(self.root, show="*")
        self.entry_contrasena.pack(pady=5)

        self.boton_registrar = tk.Button(self.root, text="Registrarse", command=self.mostrar_ventana_registro, bg="lightgreen")
        self.boton_registrar.pack(pady=5)

        self.boton_iniciar_sesion = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion, bg="lightgreen")
        self.boton_iniciar_sesion.pack(pady=5)

    def mostrar_ventana_registro(self):
        ventana_registro = tk.Toplevel(self.root)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.geometry("300x200")
        ventana_registro.configure(bg="lightyellow")

        label_nombre_usuario = tk.Label(ventana_registro, text="Nombre de usuario:", bg="lightyellow")
        label_nombre_usuario.pack(pady=5)

        entry_nombre_usuario = tk.Entry(ventana_registro)
        entry_nombre_usuario.pack(pady=5)

        label_contrasena = tk.Label(ventana_registro, text="Contraseña:", bg="lightyellow")
        label_contrasena.pack(pady=5)

        entry_contrasena = tk.Entry(ventana_registro, show="*")
        entry_contrasena.pack(pady=5)

        def registrar_usuario():
            nombre_usuario = entry_nombre_usuario.get()
            contrasena = entry_contrasena.get()
            self.controlador.registrar(nombre_usuario, contrasena)
            ventana_registro.destroy()

        boton_confirmar_registro = tk.Button(ventana_registro, text="Registrar", command=registrar_usuario, bg="lightgreen")
        boton_confirmar_registro.pack(pady=5)

    def iniciar_sesion(self):
        nombre_usuario = self.entry_nombre_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.controlador.iniciar_sesion(nombre_usuario, contrasena):
            self.root.destroy()  # Cierra la ventana principal si la autenticación es exitosa
            self.mostrar_ventana_bienvenida()

    def mostrar_ventana_bienvenida(self):
        ventana_bienvenida = tk.Toplevel()
        ventana_bienvenida.title("Bienvenido")
        ventana_bienvenida.geometry("300x200")
        ventana_bienvenida.configure(bg="white")

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)
    
    def iniciar(self):
        self.root.mainloop()
