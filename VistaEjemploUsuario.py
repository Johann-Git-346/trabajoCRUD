import tkinter as tk
from tkinter import messagebox

class UsuarioView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Vista Usuario - Comprar Productos")

        # Lista de productos
        self.product_listbox = tk.Listbox(root)
        self.product_listbox.grid(row=0, column=0, columnspan=2)
        self.actualizar_lista_productos()

        tk.Label(root, text="Nombre del Producto").grid(row=1, column=0)
        self.producto_nombre_entry = tk.Entry(root)
        self.producto_nombre_entry.grid(row=1, column=1)

        tk.Label(root, text="Cantidad").grid(row=2, column=0)
        self.cantidad_entry = tk.Entry(root)
        self.cantidad_entry.grid(row=2, column=1)

        tk.Button(root, text="Comprar", command=self.comprar_producto).grid(row=3, column=0, columnspan=2)

    def actualizar_lista_productos(self):
        self.product_listbox.delete(0, tk.END)
        productos = self.controller.obtener_productos()
        for producto in productos:
            self.product_listbox.insert(tk.END, f"Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[4]}")

    def comprar_producto(self):
        nombre = self.producto_nombre_entry.get()
        cantidad = self.cantidad_entry.get()
        try:
            cantidad = int(cantidad)
            producto = self.controller.obtener_producto_por_nombre(nombre)
            if producto:
                self.controller.comprar_producto(nombre, cantidad)
                messagebox.showinfo("Éxito", "Compra realizada con éxito")
                self.actualizar_lista_productos()
            else:
                messagebox.showerror("Error", "Producto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos")
