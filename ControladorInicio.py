from ModeloInicio import ModeloUsuario
from VistaInicio import VistaUsuario
from vistaProductos import Davista
from VistaTablas import VistaTablas1
from VistaVendedor import Davista2

class Controlador:
    def __init__(self, conexion):
        self.modelo = ModeloUsuario(conexion)
        self.vista = VistaUsuario(self)

    def iniciar(self):
        self.vista.iniciar()

    def registrar(self, email, contrasena, rol):
        return self.modelo.registrar_usuario(email, contrasena, rol)

    def iniciar_sesion(self, email, contrasena):
        rol = self.modelo.autenticar_usuario(email, contrasena)
        if rol:
            #si quiere que le sirva cambie lo que esta en las comillas por lo que tiene en la base de datos
            if rol == 'ADMINISTRA':#<-- esto lo cambia a minusculas tal cual como lo tiene en la base de datos.
                self.mostrar_vista_admin()
            elif rol == 'VENDEDOR':
                self.mostrar_vista_vendedor()
            elif rol == 'CLIENTE':
                self.mostrar_vista_cliente()
            return rol
        else:
            return None

    def mostrar_vista_admin(self):
        tablas=VistaTablas1()

    def mostrar_vista_vendedor(self):
        app = Davista2()

    def mostrar_vista_cliente(self):
        app = Davista()
