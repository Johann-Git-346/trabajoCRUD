import tkinter as tk
from tkinter import messagebox

class VistaUsuario:
    def __init__(self, controlador):
        self.controlador = controlador

    def iniciarUsuario(self):
        self.rootLogin = tk.Tk()
        self.rootLogin.title("Inicio de Sesión")
        self.rootLogin.geometry("400x300")
        self.rootLogin.configure(bg="#D3D3D3")

        self.Datos_de_inicio()

        self.rootLogin.mainloop()

    def Datos_de_inicio(self):
        self.label_correo = tk.Label(self.rootLogin, text="Correo electrónico:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        self.label_correo.pack(pady=10)

        self.entry_correo = tk.Entry(self.rootLogin, font=("Arial", 12))
        self.entry_correo.pack(pady=10)

        self.label_contrasena = tk.Label(self.rootLogin, text="Contraseña:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        self.label_contrasena.pack(pady=10)

        self.entry_contrasena = tk.Entry(self.rootLogin, show="*", font=("Arial", 12))
        self.entry_contrasena.pack(pady=10)

        self.boton_registrar = tk.Button(self.rootLogin, text="Registrarse", command=self.mostrar_ventana_registro, bg="#B0E0E6", font=("Arial", 12, "bold"), cursor="hand2")
        self.boton_registrar.pack(pady=10)

        self.boton_iniciar_sesion = tk.Button(self.rootLogin, text="Iniciar Sesión", command=self.iniciar_sesion, bg="#87CEEB", font=("Arial", 12, "bold"), cursor="hand2")
        self.boton_iniciar_sesion.pack(pady=10)

    def mostrar_ventana_registro(self):
        self.ventana_registro = tk.Toplevel(self.rootLogin)
        self.ventana_registro.title("Registro de Usuario")
        self.ventana_registro.geometry("400x400")
        self.ventana_registro.configure(bg="#D3D3D3")

        label_correo = tk.Label(self.ventana_registro, text="Correo electrónico:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        label_correo.pack(pady=10)

        entry_correo = tk.Entry(self.ventana_registro, font=("Arial", 12))
        entry_correo.pack(pady=10)

        label_contrasena = tk.Label(self.ventana_registro, text="Contraseña:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        label_contrasena.pack(pady=10)

        entry_contrasena = tk.Entry(self.ventana_registro, show="*", font=("Arial", 12))
        entry_contrasena.pack(pady=10)

        label_rol = tk.Label(self.ventana_registro, text="Seleccione Para Qué Desea su Cuenta:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        label_rol.pack(pady=10)

        rol_var = tk.StringVar(value="Usuario")

        radio_usuario = tk.Radiobutton(self.ventana_registro, text="Administrador", variable=rol_var, value="administra", bg="#D3D3D3", font=("Arial", 12))
        radio_usuario.pack()

        radio_vendedor = tk.Radiobutton(self.ventana_registro, text="Vendedor", variable=rol_var, value="Vendedor", bg="#D3D3D3", font=("Arial", 12))
        radio_vendedor.pack()

        def registrar_usuario():
            correo = entry_correo.get()
            contrasena = entry_contrasena.get()
            rol = rol_var.get()

            if "@" not in correo:
                messagebox.showerror("Error", "El correo debe contener '@'.")
                return

            if correo and contrasena:
                if self.controlador.registrar(correo, contrasena, rol):
                    messagebox.showinfo("Éxito", "Registro exitoso.")
                else:
                    messagebox.showerror("Error", "El correo ya está registrado o ocurrió un error.")
            else:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

            self.ventana_registro.destroy()

        boton_confirmar_registro = tk.Button(self.ventana_registro, text="Registrar", command=registrar_usuario, bg="#87CEEB", font=("Arial", 12, "bold"), cursor="hand2")
        boton_confirmar_registro.pack(pady=10)
        boton_cancelar_registro = tk.Button(self.ventana_registro, text="Cancelar", command=self.cancelar_registro, bg="#87CEEB", font=("Arial", 12, "bold"), cursor="hand2")
        boton_cancelar_registro.pack(pady=10)

    def cancelar_registro(self):
        self.ventana_registro.destroy()

    def iniciar_sesion(self):
        correo = self.entry_correo.get()
        contrasena = self.entry_contrasena.get()

        if "@" not in correo:
            messagebox.showerror("Error", "El correo debe contener '@'.")
            return

        if not self.controlador.iniciar_sesion(correo, contrasena):
            messagebox.showerror("Error", "Correo electrónico o contraseña incorrectos.")

    def destruir(self):
        self.rootLogin.destroy()
