import tkinter as tk
from tkinter import messagebox

class VistaUsuario:
    def __init__(self, controlador):
        self.controlador = controlador

    def iniciarUsuario(self):
        self.rootLogin = tk.Tk()
        self.rootLogin.title("Inicio de Sesión")
        self.centrar_ventana(self.rootLogin, 400, 300)
        self.rootLogin.configure(bg="#D3D3D3")

        # Llama a la función que configura el contenido centrado
        self.Datos_de_inicio()

        self.rootLogin.mainloop()

    def centrar_ventana(self, ventana, ancho, alto):
        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)

        # Establecer la geometría de la ventana con el tamaño y la posición calculada
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def Datos_de_inicio(self):
        # Creamos un Frame centrado dentro de la ventana
        frame_contenido = tk.Frame(self.rootLogin, bg="#D3D3D3")
        frame_contenido.pack(expand=True)  # El Frame se expandirá para llenar el espacio disponible

        # Añadir widgets al frame con margen adecuado
        self.label_correo = tk.Label(frame_contenido, text="Correo electrónico:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        self.label_correo.pack(pady=10)

        self.entry_correo = tk.Entry(frame_contenido, font=("Arial", 12))
        self.entry_correo.pack(pady=10)

        self.label_contrasena = tk.Label(frame_contenido, text="Contraseña:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        self.label_contrasena.pack(pady=10)

        self.entry_contrasena = tk.Entry(frame_contenido, show="*", font=("Arial", 12))
        self.entry_contrasena.pack(pady=10)

        self.boton_registrar = tk.Button(frame_contenido, text="Registrarse", command=self.mostrar_ventana_registro, bg="#B0E0E6", font=("Arial", 12, "bold"), cursor="hand2")
        self.boton_registrar.pack(pady=10)

        self.boton_iniciar_sesion = tk.Button(frame_contenido, text="Iniciar Sesión", command=self.iniciar_sesion, bg="#87CEEB", font=("Arial", 12, "bold"), cursor="hand2")
        self.boton_iniciar_sesion.pack(pady=10)

    def mostrar_ventana_registro(self):
        self.ventana_registro = tk.Toplevel(self.rootLogin)
        self.ventana_registro.title("Registro de Usuario")
        self.centrar_ventana(self.ventana_registro, 400, 400)
        self.ventana_registro.configure(bg="#D3D3D3")

        frame_contenido_registro = tk.Frame(self.ventana_registro, bg="#D3D3D3")
        frame_contenido_registro.pack(expand=True)

        label_correo = tk.Label(frame_contenido_registro, text="Correo electrónico:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        label_correo.pack(pady=10)

        entry_correo = tk.Entry(frame_contenido_registro, font=("Arial", 12))
        entry_correo.pack(pady=10)

        label_contrasena = tk.Label(frame_contenido_registro, text="Contraseña:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        label_contrasena.pack(pady=10)

        entry_contrasena = tk.Entry(frame_contenido_registro, show="*", font=("Arial", 12))
        entry_contrasena.pack(pady=10)

        label_rol = tk.Label(frame_contenido_registro, text="Seleccione Para Qué Desea su Cuenta:", bg="#D3D3D3", font=("Arial", 12, "bold"))
        label_rol.pack(pady=10)

        rol_var = tk.StringVar(value="Usuario")

        radio_usuario = tk.Radiobutton(frame_contenido_registro, text="  Usuario  ", variable=rol_var, value="Usuario", bg="#D3D3D3", font=("Arial", 12))
        radio_usuario.pack()

        radio_vendedor = tk.Radiobutton(frame_contenido_registro, text="Vendedor", variable=rol_var, value="Vendedor", bg="#D3D3D3", font=("Arial", 12))
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

        boton_confirmar_registro = tk.Button(frame_contenido_registro, text="Registrar", command=registrar_usuario, bg="#87CEEB", font=("Arial", 12, "bold"), cursor="hand2")
        boton_confirmar_registro.pack(pady=10)

        boton_cancelar_registro = tk.Button(frame_contenido_registro, text="Cancelar", command=self.cancelar_registro, bg="#87CEEB", font=("Arial", 12, "bold"), cursor="hand2")
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
