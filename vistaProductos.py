import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import io

class Davista:
    def __init__(self, objController):
        self.objController = objController
        self.productos_seleccionados = []

    def iniciarProductos(self):
        self.rootCliente = tk.Tk()
        self.rootCliente.title("Cliente")
        self.rootCliente.geometry("800x600")
        self.rootCliente.state('zoomed')

        self.CrearSlider()
        self.CrearSliderLateral()
        self.CrearSliderCatalogo()
        self.rootCliente.mainloop()

    def CrearSlider(self):
        """ Crear el marco superior para el nombre de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.rootCliente, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_top.config(background="#333333")

        company_name = tk.Label(self.frame_top, text="TecnoNube", font=("Arial", 24, "bold"), foreground="#FFFFFF", anchor="center")
        company_name.pack(side=tk.LEFT, padx=10, pady=10)
        company_name.config(background="#333333")

        logo = tk.Frame(self.frame_top, width=20, height=20)
        logo.pack(side=tk.RIGHT, padx=10, pady=10)
        logo.config(background="#333333")

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_left = tk.Frame(self.frame_top)
        spacer_left.pack(side=tk.LEFT, expand=True)
        spacer_left.config(background="#333333")

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_right = tk.Frame(self.frame_top)
        spacer_right.pack(side=tk.RIGHT, expand=True)
        spacer_right.config(background="#333333")

        etiqueta = tk.Label(logo)
        etiqueta.pack(side=tk.RIGHT)
        etiqueta.config(background="#333333")

        self.rutaimagen2 = "imagenes/LOGO.jpg"

        if not os.path.exists(self.rutaimagen2):
            print(f"Error: La ruta de la imagen no existe: {self.rutaimagen2}")
            return

        try:
            imagen2 = Image.open(self.rutaimagen2)
            imagen2 = imagen2.resize((155, 130))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen2)
            etiqueta_imagen = tk.Label(logo, image=self.imagen_tk2)
            etiqueta_imagen.pack()
            etiqueta_imagen.config(bg="#333333")
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

    def CrearSliderLateral(self):
        """ Crear el marco lateral con los botones de opciones. """
        self.frame_sidebar = tk.Frame(self.rootCliente, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#D3D3D3")

        sidebar_buttons = ["Realizar Pedido", "Ver Pedido", "Cerrar sesión"]
        sidebar_commands = [self.realizar_pedido, self.ver_pedido, self.CerrarSesion]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2", bg="#87CEEB", foreground="black", font=("Arial", 10, "bold"), text=text, command=command).pack(fill=tk.X, padx=10, pady=20)

    def CrearSliderCatalogo(self):
        """ Crear el marco para las categorías y el catálogo. """
        self.productos = self.objController.obtener_productos()

        self.frame_catalog = tk.Frame(self.rootCliente)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#D3D3D3")

        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#D3D3D3")

        categories = ["Celular", "Laptops"]
        comandoCategoria = [self.catalogoTelefono, self.catalogoLaptop]
        for text, comandoCategoria in zip(categories, comandoCategoria):
            tk.Button(self.frame_categories, cursor="hand2", bg="#ADD8E6", font=("Arial", 10, "bold"), foreground="black", text=text, command=comandoCategoria).pack(side=tk.LEFT, padx=280, pady=5)

        self.catalog_title = tk.Label(self.frame_catalog, text="Celular", foreground="#000000", font=("Arial", 16, "bold"), relief=tk.GROOVE, borderwidth=2)
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#B0E0E6")

        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#D3D3D3")

        self.mostrar_productos_categoria("celular")

    def mostrar_productos_categoria(self, categoria):
        """ Muestra los productos filtrados por categoría. """
        self.catalog_title.config(text=categoria)

        self.productos_filtrados = [p for p in self.productos if p[3] == categoria]

        for widget in self.frame_products.winfo_children():
            widget.destroy()

        self.imagenes_tk = []
        filas = (len(self.productos_filtrados) // 3) + (1 if len(self.productos_filtrados) % 3 != 0 else 0)

        for i in range(filas):
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#D3D3D3")

            for j in range(7):
                img_index = (i * 7) + j
                if img_index < len(self.productos_filtrados):
                    self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                    self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                    self.product_frame.config(bg="#B0E0E6")
                    self.crear_cuadro_producto(self.product_frame, self.productos_filtrados[img_index])

    def crear_cuadro_producto(self, product_frame, producto):
        """ Crea un cuadro individual para un producto. """
        try:
            imagen = Image.open(io.BytesIO(producto[5]))
            imagen = imagen.resize((110, 110))
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.imagenes_tk.append(imagen_tk)
            etiqueta_imagen = tk.Label(product_frame, image=imagen_tk, width=130, height=100)
            etiqueta_imagen.pack(pady=5)
            etiqueta_imagen.config(bg="#B0E0E6")
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

        info_label = tk.Label(product_frame, text=f"Nombre: {producto[1]}\nPrecio: {producto[2]}\nCantidad: {producto[4]}", justify=tk.LEFT)
        info_label.pack()
        info_label.config(bg="#B0E0E6", font=("Arial", 10, "bold"), foreground="#000000")

        tk.Button(product_frame, text="Agregar al carrito", cursor="hand2", bg="#4A94B3", command=lambda: self.agregar_al_carrito(producto)).pack(pady=5)

    def agregar_al_carrito(self, producto):
        self.productos_seleccionados.append(producto)
        messagebox.showinfo("Éxito", f"Producto {producto[1]} agregado al carrito")

    def realizar_pedido(self):
        if not self.productos_seleccionados:
            messagebox.showwarning("Carrito vacío", "No ha seleccionado ningún producto para comprar.")
            return

        total = sum(p[2] for p in self.productos_seleccionados)
        confirm = messagebox.askyesno("Confirmar pedido", f"El total de su compra es ${total:.2f}. ¿Desea realizar el pedido?")

        if confirm:
            self.objController.realizar_pedido(self.productos_seleccionados)
            messagebox.showinfo("Pedido realizado", "Su pedido se ha realizado con éxito.")
            self.productos_seleccionados.clear()

    def ver_pedido(self):
        """ Muestra los productos seleccionados para el pedido en una ventana emergente. """
        if not self.productos_seleccionados:
            messagebox.showinfo("Carrito vacío", "No ha seleccionado ningún producto para el pedido.")
            return

        self.ventana_pedido = tk.Toplevel(self.rootCliente)
        self.ventana_pedido.title("Productos Seleccionados")
        self.ventana_pedido.geometry("400x400")
        self.ventana_pedido.config(bg="#f0f0f0")

        frame_productos_pedido = tk.Frame(self.ventana_pedido, bg="#f0f0f0")
        frame_productos_pedido.pack(fill=tk.BOTH, expand=True)

        for producto in self.productos_seleccionados:
            producto_frame = tk.Frame(frame_productos_pedido, bg="#d3d3d3", pady=5, padx=5)
            producto_frame.pack(fill=tk.X, pady=5)

            label_producto = tk.Label(producto_frame, text=f"{producto[1]} - ${producto[2]:.2f}", bg="#d3d3d3", font=("Arial", 10, "bold"))
            label_producto.pack(side=tk.LEFT)

            boton_eliminar = tk.Button(producto_frame, text="Eliminar", cursor="hand2", bg="red", font=("Arial", 10, "bold"),
                                       command=lambda p=producto: self.eliminar_producto_carrito(p, producto_frame))
            boton_eliminar.pack(side=tk.RIGHT)

    def eliminar_producto_carrito(self, producto, frame):
        """ Elimina un producto del carrito. """
        self.productos_seleccionados.remove(producto)
        frame.destroy()
        messagebox.showinfo("Producto eliminado", f"Producto {producto[1]} ha sido eliminado del carrito.")

    def CerrarSesion(self):
        confirm = messagebox.askyesno("Cerrar Sesión", "¿Está seguro de que desea cerrar sesión?")
        if confirm:
            self.rootCliente.destroy()
            self.objController.mostrarLogin()

    def catalogoTelefono(self):
        self.mostrar_productos_categoria("celular")

    def catalogoLaptop(self):
        self.mostrar_productos_categoria("laptop")
