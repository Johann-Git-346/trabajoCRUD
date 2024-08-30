import tkinter as tk
from tkinter import messagebox

class VendedorView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Vista Vendedor - Gestión de Productos")

        # Lista de productos
        self.product_listbox = tk.Listbox(root)
        self.product_listbox.grid(row=0, column=0, columnspan=3)
        self.actualizar_lista_productos()

        # Campos para agregar o modificar producto
        tk.Label(root, text="Nombre del Producto").grid(row=1, column=0)
        self.producto_nombre_entry = tk.Entry(root)
        self.producto_nombre_entry.grid(row=1, column=1)

        tk.Label(root, text="Nuevo Precio").grid(row=2, column=0)
        self.nuevo_precio_entry = tk.Entry(root)
        self.nuevo_precio_entry.grid(row=2, column=1)

        tk.Label(root, text="Nueva Descripción").grid(row=3, column=0)
        self.nueva_descripcion_entry = tk.Entry(root)
        self.nueva_descripcion_entry.grid(row=3, column=1)

        tk.Label(root, text="Nueva Cantidad").grid(row=4, column=0)
        self.nueva_cantidad_entry = tk.Entry(root)
        self.nueva_cantidad_entry.grid(row=4, column=1)

        # Botones para agregar, modificar y eliminar producto
        tk.Button(root, text="Agregar Producto", command=self.agregar_producto).grid(row=5, column=0)
        tk.Button(root, text="Modificar Producto", command=self.modificar_producto).grid(row=5, column=1)
        tk.Button(root, text="Eliminar Producto", command=self.eliminar_producto).grid(row=5, column=2)

    def actualizar_lista_productos(self):
        self.product_listbox.delete(0, tk.END)
        productos = self.controller.obtener_productos()
        for producto in productos:
            self.product_listbox.insert(tk.END, f"Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[4]}")

    def agregar_producto(self):
        nombre = self.producto_nombre_entry.get()
        precio = self.nuevo_precio_entry.get()
        descripcion = self.nueva_descripcion_entry.get()
        cantidad = self.nueva_cantidad_entry.get()

        if not nombre or not precio or not descripcion or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios para agregar un producto")
            return

        try:
            precio = float(precio)
            cantidad = int(cantidad)
            self.controller.agregar_producto(nombre, precio, descripcion, cantidad)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.actualizar_lista_productos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")

    def modificar_producto(self):
        nombre = self.producto_nombre_entry.get()
        nuevo_precio = self.nuevo_precio_entry.get()
        nueva_descripcion = self.nueva_descripcion_entry.get()
        nueva_cantidad = self.nueva_cantidad_entry.get()

        if not nombre:
            messagebox.showerror("Error", "El nombre del producto es obligatorio para modificarlo")
            return

        try:
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            producto = self.controller.obtener_producto_por_nombre(nombre)
            if producto:
                self.controller.modificar_producto(nombre, nuevo_precio, nueva_descripcion, nueva_cantidad)
                messagebox.showinfo("Éxito", "Producto modificado con éxito")
                self.actualizar_lista_productos()
            else:
                messagebox.showerror("Error", "Producto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")

    def eliminar_producto(self):
        nombre = self.producto_nombre_entry.get()
        if not nombre:
            messagebox.showerror("Error", "El nombre del producto es obligatorio para eliminarlo")
            return

        producto = self.controller.obtener_producto_por_nombre(nombre)
        if producto:
            self.controller.eliminar_producto(nombre)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.actualizar_lista_productos()
        else:
            messagebox.showerror("Error", "Producto no encontrado")
