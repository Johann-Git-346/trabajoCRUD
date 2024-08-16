from ModeloInicio import ModeloUsuario
from VistaInicio import VistaUsuario

class Controlador:
    def __init__(self, conexion):
        self.modelo = ModeloUsuario(conexion)
        self.vista = VistaUsuario(self)

    def iniciar(self):
        self.vista.iniciar()

    def registrar(self, nombre_usuario, contrasena):
        if self.modelo.registrar_usuario(nombre_usuario, contrasena):
            self.vista.mostrar_mensaje("Registro exitoso.")
        else:
            self.vista.mostrar_mensaje("El nombre de usuario ya está registrado.")

    def iniciar_sesion(self, nombre_usuario, contrasena):
        if self.modelo.autenticar_usuario(nombre_usuario, contrasena):
            return True
        else:
            self.vista.mostrar_mensaje("Nombre de usuario o contraseña incorrectos.")
            return False
