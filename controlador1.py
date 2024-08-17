from modelo import ModeloUsuario
from vista import VistaUsuario

class Controlador:
    def __init__(self, conexion):
        self.modelo = ModeloUsuario(conexion)
        self.vista = VistaUsuario(self)

    def iniciar(self):
        self.vista.iniciar()

    def registrar(self, nombre_usuario, contrasena):
        if self.modelo.registrar_usuario(nombre_usuario, contrasena):
            self.vista.mostrarMensajeExitoso()
        else:
            self.vista.mostrarMensajeRegistrado()

    def iniciar_sesion(self, nombre_usuario, contrasena):
        if self.modelo.autenticar_usuario(nombre_usuario, contrasena):
            return True
        else:
            self.vista.mostrarMensajeError()
            return False