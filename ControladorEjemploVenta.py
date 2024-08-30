from tkinter import Tk, Button
from ModeloEjemploVenta import ProductoModel
from VistaUsuario import UsuarioView
from VistaVendedor import VendedorView

class ProductoController:
    def __init__(self, model):
        self.model = model

    def obtener_productos(self):
        return self.model.obtener_productos()

    def obtener_producto_por_nombre(self, nombre):
        return self.model.obtener_producto_por_nombre(nombre)

    def agregar_producto(self, nombre, precio, descripcion, cantidad):
        self.model.agregar_producto(nombre, precio, descripcion, cantidad)

    def modificar_producto(self, nombre, nuevo_precio=None, nueva_descripcion=None, nueva_cantidad=None):
        self.model.modificar_producto(nombre, nuevo_precio, nueva_descripcion, nueva_cantidad)

    def eliminar_producto(self, nombre):
        self.model.eliminar_producto(nombre)


#inicio principal

def iniciar_usuario():
    root = Tk()
    model = ProductoModel()
    controller = ProductoController(model)
    UsuarioView(root, controller)
    root.mainloop()

def iniciar_vendedor():
    root = Tk()
    model = ProductoModel()
    controller = ProductoController(model)
    VendedorView(root, controller)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Sistema de Gestión de Productos")

    Button(root, text="Vista Usuario", command=iniciar_usuario).pack(pady=10)
    Button(root, text="Vista Vendedor", command=iniciar_vendedor).pack(pady=10)

    root.mainloop()