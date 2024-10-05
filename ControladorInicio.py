from BaseInicio import Crear_Conexion
from ModeloInicio import ModeloUsuario
from VistaInicio import VistaUsuario
from VistaTablas import VistaTablas1
from VistaVendedor import Davista2
from vistaProductos import Davista
import json

class Controlador:
    def __init__(self, conexion, modelo):
        self.conexion=conexion
        self.modelo = modelo
        
    def obtener_productos(self):
        return self.modelo.obtener_productos()
        
    def agregar_productos(self,Id, nombre, precio, categoria, cantidad):
        return self.modelo.agregar_producto(Id,nombre, precio, categoria, cantidad)
    
    def subirImagen2(self,nombre,imagenBinaria):
        return self.modelo.imagenABaseDatos2(nombre, imagenBinaria )

    def registrar(self, usuario, contrasena, rol):
        return self.modelo.registrar_usuario(usuario, contrasena, rol)

    def iniciar_sesion(self, correo, contrasena):
        rol = self.modelo.autenticar_usuario(correo, contrasena)
        if rol:
            vistaUsuario.destruir()
            if rol == 'administra':#<-- esto lo cambia a minusculas tal cual como lo tiene en la base de datos.
                self.mostrar_vista_vendedor()  
            elif rol == "vendedor":
                self.mostrar_vista_vendedor()
            elif rol == 'CLIENTE':
                self.mostrar_vista_cliente()
            return rol
        else:
            return None
        
    def get_user_role(self):
        return self.modelo.obtener_usuario_id()
    
    def obtenerMasYMenosVendidos(self):
        return self.modelo.obtenerMasYMenosVendidos()
    
    def generarInforme(self, mas_vendidos, menos_vendidos):
        data = {
            "Mas Vendidos": mas_vendidos,
            "Menos Vendidos": menos_vendidos
        }
        json_data = json.dumps(data, indent=4)
        self.modelo.setInforme(json_data)
    
    def modificar_producto(self, id,nuevoNombre=None,nuevo_precio=None, nueva_descripcion=None, nueva_cantidad=None):
        self.modelo.modificar_producto(id,nuevoNombre, nuevo_precio, nueva_descripcion, nueva_cantidad)

    def eliminar_producto(self, id):
        self.modelo.eliminar_producto(id)

    def actualizar_cantidad_productos(self,productos):
        self.modelo.actualizar_cantidad_productos(productos)

    def obtener_producto_por_nombre(self, nombre):
        return self.modelo.obtener_producto_por_nombre(nombre)

    def mostrar_vista_vendedor(self):
        vistaVendedor.iniciarVendedor()

    def vistaInformes(self):
        vistaTablas.iniciarTablas()

    def mostrar_vista_cliente(self):
        vista_producto.iniciarProductos()

    def mostrarLogin(self):
        vistaUsuario.iniciarUsuario()

    
    def actualizar_inventario(self, id_producto, cantidad_comprada):
        """ Actualiza el inventario de un producto tras realizar una compra. """
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                # Primero, obtener la cantidad actual del producto
                cursor.execute("SELECT cantidad FROM productos WHERE id = %s", (id_producto,))
                cantidad_actual = cursor.fetchone()[0]

                # Calcular la nueva cantidad después de la compra
                nueva_cantidad = cantidad_actual - cantidad_comprada

                # Evitar cantidades negativas
                if nueva_cantidad < 0:
                    nueva_cantidad = 0

                # Actualizar la cantidad en la base de datos
                cursor.execute("UPDATE productos SET cantidad = %s WHERE id = %s", (nueva_cantidad, id_producto))
                self.conexion.commit()

            except Exception as e:
                print(f"Error al actualizar el inventario: {e}")
            finally:
                cursor.close()

    def realizar_pedido(self, productos_seleccionados):
        """ Realiza un pedido y actualiza el inventario para cada producto. """
        for producto in productos_seleccionados:
            id_producto = producto[0]  # Suponiendo que el ID del producto está en la primera posición
            cantidad_comprada = producto[4]  # La cantidad comprada está en la posición 4

            # Actualizar el inventario por cada producto
            self.actualizar_inventario(id_producto, cantidad_comprada)

        # Aquí puedes agregar más lógica para finalizar el pedido, como registrar el pedido en la base de datos
        print("Pedido realizado con éxito.")
        
    def realizar_pedido(self,productos):
        self.modelo.comprar_producto(productos)

# PRINCIPAL
conexion = Crear_Conexion.conexionBaseDeDatos()
if conexion:
    modelo=ModeloUsuario(conexion)    
    controlador = Controlador(conexion,modelo)
    vista_producto=Davista(controlador)
    vistaTablas=VistaTablas1(controlador)
    vistaVendedor=Davista2(controlador)
    vistaUsuario=VistaUsuario(controlador)
    vistaUsuario.iniciarUsuario()
else:
    print("No se pudo establecer conexión con la base de datos.")