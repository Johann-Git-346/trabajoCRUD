from baseDatos import Crear_Conexion
from modelo import ModeloUsuario
from vista import VistaUsuario
from vistaProductos import Davista
from VistaTablas import VistaTablas1
from VistaVendedor import Davista2

class Controlador:
    def __init__(self, conexion,modelo):
        self.conexion=conexion
        self.modelo = modelo
        
    def agregar_productos(self,nombre,precio,categoria,cantidad):
        return self.modelo.agregar_producto(nombre,precio,categoria,cantidad)
    
    def subirImagen(self,nombre,imagen):
        return self.modelo.imagenABaseDatos(nombre, imagen )
    
    def obtener_productos(self):
        return self.modelo.obtener_productos()

    def registrar(self, email, contrasena, rol):
        return self.modelo.registrar_usuario(email, contrasena, rol)

    def iniciar_sesion(self, email, contrasena):
        rol = self.modelo.autenticar_usuario(email, contrasena)
        if rol:
            #si quiere que le sirva cambie lo que esta en las comillas por lo que tiene en la base de datos
            if rol == 'ADMINISTRA':#<-- esto lo cambia a minusculas tal cual como lo tiene en la base de datos.
                self.mostrar_vista_vendedor()
            elif rol == 'VENDEDOR':
                self.mostrar_vista_vendedor()
            elif rol == 'CLIENTE':
                self.mostrar_vista_cliente()
            return rol
        else:
            return None
    def mostrar_vista_vendedor(self):
        vistaVendedor.iniciarVendedor()

    def mostrar_vista_cliente(self):
        vistaProductos.iniciarProductos()

    def vistaInformes(self):
        vistaTablas.iniciarTablas()

    def mostrarLogin(self):
        vistaUsuario.iniciarUsuario()



# PRINCIPAL
conexion = Crear_Conexion.conexionBaseDeDatos()
if conexion:
    modelo=ModeloUsuario(conexion)    
    controlador = Controlador(conexion,modelo)
    vistaProductos=Davista(controlador)
    vistaTablas=VistaTablas1(controlador)
    vistaVendedor=Davista2(controlador)
    vistaUsuario=VistaUsuario(controlador)
    vistaUsuario.iniciarUsuario()
else:
    print("No se pudo establecer conexión con la base de datos.")