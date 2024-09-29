from BaseInicio import Crear_Conexion
from ModeloInicio import ModeloUsuario
from VistaInicio import VistaUsuario
from VistaTablas import VistaTablas1
from VistaVendedor import Davista2
from VistaCliente import Davista3
from vistaProductos import Davista
import json

class Controlador:
    def __init__(self, conexion, modelo):
        self.conexion=conexion
        self.modelo = modelo
        
    def obtener_productos(self):
        return self.modelo.obtener_productos()
        
    def agregar_productos(self, nombre, precio, categoria, cantidad):
        return self.modelo.agregar_producto(nombre, precio, categoria, cantidad)
    
    def subirImagen(self,nombre,imagen):
        return self.modelo.imagenABaseDatos(nombre, imagen)
    
    def subirImagen2(self,nombre,imagenBinaria):
        return self.modelo.imagenABaseDatos2(nombre, imagenBinaria )

    def registrar(self, usuario, contrasena, rol):
        return self.modelo.registrar_usuario(usuario, contrasena, rol)

    def iniciar_sesion(self, correo, contrasena):
        rol = self.modelo.autenticar_usuario(correo, contrasena)
        if rol:
            vistaUsuario.destruir()
            if rol == 'administra':#<-- esto lo cambia a minusculas tal cual como lo tiene en la base de datos.
                self.vistaInformes()  
            elif rol == "vendedor":
                self.mostrar_vista_vendedor()
            elif rol == 'CLIENTE':
                self.mostrar_vista_cliente()
            return rol
        else:
            return None
        
    def obtenerMasYMenosVendidos(self):
        return self.modelo.obtenerMasYMenosVendidos()
    
    def generarInforme(self, mas_vendidos, menos_vendidos):
        data = {
            "Mas Vendidos": mas_vendidos,
            "Menos Vendidos": menos_vendidos
        }
        json_data = json.dumps(data, indent=4)
        self.modelo.setInforme(json_data)
    
    def modificar_producto(self, nombre,nuevoNombre=None,nuevo_precio=None, nueva_descripcion=None, nueva_cantidad=None):
        self.modelo.modificar_producto(nombre,nuevoNombre, nuevo_precio, nueva_descripcion, nueva_cantidad)

    def eliminar_producto(self, nombre):
        self.modelo.eliminar_producto(nombre)

    def obtener_producto_por_nombre(self, nombre):
        return self.modelo.obtener_producto_por_nombre(nombre)

    def mostrar_vista_vendedor(self):
        vistaVendedor.iniciarVendedor()

    def vistaInformes(self):
        vistaTablas.iniciarTablas()

    def mostrar_vista_cliente(Self):
        VistaCliente.iniciarCliente()

    def mostrar_vista_cliente(self):
        vista_producto.iniciarProductos()

    def mostrarLogin(self):
        vistaUsuario.iniciarUsuario()

# PRINCIPAL
conexion = Crear_Conexion.conexionBaseDeDatos()
if conexion:
    modelo=ModeloUsuario(conexion)    
    controlador = Controlador(conexion,modelo)
    vista_producto=Davista(controlador)
    vistaTablas=VistaTablas1(controlador)
    vistaVendedor=Davista2(controlador)
    VistaCliente=Davista3(controlador)
    vistaUsuario=VistaUsuario(controlador)
    vistaUsuario.iniciarUsuario()
else:
    print("No se pudo establecer conexión con la base de datos.")