from ModeloInicio import ModeloUsuario
from VistaInicio import VistaUsuario

class Controlador:
    def __init__(self, conexion):
        self.modelo = ModeloUsuario(conexion)
        self.vista = VistaUsuario(self)
        self.crear_administrador_predeterminado()

    def iniciar(self):
        self.vista.iniciar()

    def crear_administrador_predeterminado(self):
        admin_email = "admin@gmail.com"
        admin_contrasena = "admin123"
        self.modelo.registrar_usuario(admin_email, admin_contrasena)

    def registrar(self, email, contrasena):
        return self.modelo.registrar_usuario(email, contrasena)

    def iniciar_sesion(self, email, contrasena):
        return self.modelo.autenticar_usuario(email, contrasena)
