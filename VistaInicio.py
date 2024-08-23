import tkinter as tk
from tkinter import messagebox

class VistaUsuario:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")

        self.Datos_de_inicio()

    def Datos_de_inicio(self):
        self.label_email = tk.Label(self.root, text="Correo electrónico:", bg="lightblue", font=("Arial", 12, "bold"))
        self.label_email.pack(pady=10)

        self.entry_email = tk.Entry(self.root, font=("Arial", 12))
        self.entry_email.pack(pady=10)

        self.label_contrasena = tk.Label(self.root, text="Contraseña:", bg="lightblue", font=("Arial", 12, "bold"))
        self.label_contrasena.pack(pady=10)

        self.entry_contrasena = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.entry_contrasena.pack(pady=10)

        self.boton_registrar = tk.Button(self.root, text="Registrarse", command=self.mostrar_ventana_registro, bg="lightgreen", font=("Arial", 12, "bold"))
        self.boton_registrar.pack(pady=10)

        self.boton_iniciar_sesion = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion, bg="lightgreen", font=("Arial", 12, "bold"))
        self.boton_iniciar_sesion.pack(pady=10)

    def mostrar_ventana_registro(self):
        ventana_registro = tk.Toplevel(self.root)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.geometry("400x350")
        ventana_registro.configure(bg="lightyellow")

        label_email = tk.Label(ventana_registro, text="Correo electrónico:", bg="lightyellow", font=("Arial", 12, "bold"))
        label_email.pack(pady=10)

        entry_email = tk.Entry(ventana_registro, font=("Arial", 12))
        entry_email.pack(pady=10)

        label_contrasena = tk.Label(ventana_registro, text="Contraseña:", bg="lightyellow", font=("Arial", 12, "bold"))
        label_contrasena.pack(pady=10)

        entry_contrasena = tk.Entry(ventana_registro, show="*", font=("Arial", 12))
        entry_contrasena.pack(pady=10)

        label_rol = tk.Label(ventana_registro, text="Seleccione Para Que Desea su Cuenta:", bg="lightyellow", font=("Arial", 12, "bold"))
        label_rol.pack(pady=10)

        rol_var = tk.StringVar(value="Usuario")  # Valor por defecto

        radio_usuario = tk.Radiobutton(ventana_registro, text="Usuario", variable=rol_var, value="Usuario", bg="lightyellow", font=("Arial", 12))
        radio_usuario.pack()

        radio_vendedor = tk.Radiobutton(ventana_registro, text="Vendedor", variable=rol_var, value="Vendedor", bg="lightyellow", font=("Arial", 12))
        radio_vendedor.pack()

        def registrar_usuario():
            email = entry_email.get()
            contrasena = entry_contrasena.get()
            rol = rol_var.get()  # Obtener el rol seleccionado

            if email and contrasena:
                if self.controlador.registrar(email, contrasena, rol):
                    messagebox.showinfo("Éxito", "Registro exitoso.")
                else:
                    messagebox.showerror("Error", "El correo ya está registrado o ocurrió un error.")
            else:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

            ventana_registro.destroy()

        boton_confirmar_registro = tk.Button(ventana_registro, text="Registrar", command=registrar_usuario, bg="lightgreen", font=("Arial", 12, "bold"))
        boton_confirmar_registro.pack(pady=10)

    def iniciar_sesion(self):
        email = self.entry_email.get()
        contrasena = self.entry_contrasena.get()
        if not self.controlador.iniciar_sesion(email, contrasena):
            messagebox.showerror("Error", "Correo electrónico o contraseña incorrectos.")

    def iniciar(self):
        self.root.mainloop()
