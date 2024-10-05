import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import io

class Davista:
    def __init__(self, objController):
        self.objController = objController
        self.productos_seleccionados = []
        self.carrito = {}  # Cambiar a un diccionario para almacenar cantidades

    def iniciarProductos(self):
        self.rootCliente = tk.Tk()
        self.rootCliente.title("Cliente")
        self.rootCliente.geometry("800x600")
        self.rootCliente.state('zoomed')

        self.create_top_frame()
        self.create_sidebar_frame()
        self.create_catalog_frame()

        self.rootCliente.mainloop()

    def create_top_frame(self):
        # Crear el marco superior para el nombre de la empresa y la imagen del logo. 
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

    def create_sidebar_frame(self):
        # Crear el marco lateral con los botones de opciones. 
        self.frame_sidebar = tk.Frame(self.rootCliente, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#D3D3D3")

        sidebar_buttons = ["Realizar Pedido"]
        sidebar_commands = [self.realizar_pedido]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2", bg="#87CEEB", foreground="black", font=("Arial", 10, "bold"), text=text, command=self.actualizar).pack(fill=tk.X, padx=10, pady=20)

        
        sidebar_buttons = ["Carrito", "Cerrar sesión"]
        sidebar_commands = [ self.mostrarCarrito, self.CerrarSesion]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2", bg="#87CEEB", foreground="black", font=("Arial", 10, "bold"), text=text, command=command).pack(fill=tk.X, padx=10, pady=20)

      

    def create_catalog_frame(self):
        # Crear el marco para las categorías y el catálogo. 
        self.productos = self.objController.obtener_productos()

        self.frame_catalog = tk.Frame(self.rootCliente)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#D3D3D3")

        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#D3D3D3")

        categories = ["Celular", "Laptops"]
        comandoCategoria = [self.catalogoTelefono, self.catalogoLaptop]
        for text, comando in zip(categories, comandoCategoria):
            tk.Button(self.frame_categories, cursor="hand2", bg="#ADD8E6", font=("Arial", 10, "bold"), foreground="black", text=text, command=comando).pack(side=tk.LEFT, padx=260, pady=5)

        self.catalog_title = tk.Label(self.frame_catalog, text="Celular", foreground="#000000", font=("Arial", 16, "bold"), relief=tk.GROOVE, borderwidth=2)
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#B0E0E6")

        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#D3D3D3")

        self.mostrar_productos_categoria("celular")

    def catalogoTelefono(self):
        # Muestra los productos de la categoría celulares. 
        self.catalog_title.config(text="Celulares")
        self.mostrar_productos_categoria("celular")

    def catalogoLaptop(self):
        # Muestra los productos de la categoría laptops. 
        self.catalog_title.config(text="Laptops")
        self.mostrar_productos_categoria("laptop")

    def mostrar_productos_categoria(self, categoria):
        # Muestra los productos filtrados por categoría. 
        self.catalog_title.config(text=categoria)

        self.productos_filtrados = [p for p in self.productos if p[3].lower() == categoria.lower()]

        for widget in self.frame_products.winfo_children():
            widget.destroy()

        self.imagenes_tk = []
        filas = (len(self.productos_filtrados) // 3) + (1 if len(self.productos_filtrados) % 3 != 0 else 0)

        for i in range(filas):
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#D3D3D3")

            for j in range(3):  # Aseguramos que haya hasta 3 productos por fila
                img_index = (i * 3) + j
                if img_index < len(self.productos_filtrados):
                    self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                    self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                    self.product_frame.config(bg="#B0E0E6")
                    self.crear_cuadro_producto(self.product_frame, self.productos_filtrados[img_index])

    def crear_cuadro_producto(self, product_frame, producto):
        # Crea un cuadro individual para un producto. 
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

        tk.Button(product_frame, text="Agregar al carrito", cursor="hand2", command=lambda: self.agregar_al_carrito(producto, info_label)).pack(pady=5)


    def agregar_al_carrito(self, producto, info_label):
        #Agrega el producto al carrito de compras. 
        if producto[4] > 0:  # Solo agregar si hay stock disponible
            cantidad_a_agregar = 1
                
            # Actualiza el carrito con la nueva cantidad
            if producto in self.carrito:  # Si el producto ya está en el carrito, incrementa la cantidad
                self.carrito[producto] += cantidad_a_agregar
            else:  # Si no está en el carrito, lo añade con cantidad especificada
                self.carrito[producto] = cantidad_a_agregar

            self.actualizar_cantidad_producto(producto, cantidad_a_agregar, info_label)  # Actualiza la cantidad en la vista y en la base de datos
            messagebox.showinfo("Éxito", f"Producto {producto[1]} agregado al carrito. Cantidad en carrito: {self.carrito[producto]}")

        else:
            messagebox.showwarning("Sin stock", f"No hay suficiente stock para {producto[1]}")

    def actualizar_cantidad_producto(self, producto, cantidad, info_label):
        # Actualiza la cantidad del producto en la vista y en la base de datos. 
        nuevo_stock = producto[4] - cantidad
        # Actualizar la cantidad en la base de datos
        self.objController.actualizar_inventario(producto[0], cantidad)  # Suponiendo que el ID del producto está en la primera posición
        # Actualiza la vista
       
        #info_label.config(text=f"Nombre: {producto[1]}\nPrecio: {producto[2]}\nCantidad: {nuevo_stock}")

    def mostrarCarrito(self):
        # Muestra los productos en el carrito.
        if not self.carrito:
            messagebox.showinfo("Carrito", "El carrito está vacío.")
            return

        self.carrito_window = tk.Toplevel(self.rootCliente)
        self.carrito_window.title("Carrito")
        self.carrito_window.geometry("400x400")
        
        tk.Label(self.carrito_window, text="Productos en el carrito", font=("Arial", 16)).pack(pady=10)

        total = 0
        for producto, cantidad in self.carrito.items():
            total += producto[2]  * cantidad  # Asumiendo que el precio está en la segunda posición
            product_frame = tk.Frame(self.carrito_window)
            product_frame.pack(fill=tk.X, padx=5, pady=5)

            tk.Label(product_frame, text=f"{producto[1]} - Cantidad: {cantidad} - Precio: {producto[2] * cantidad}").pack(side=tk.LEFT)

            tk.Button(product_frame, text="Modificar", command=lambda prod=producto, cant=cantidad: self.modificar_producto(prod, cant)).pack(side=tk.LEFT, padx=5)
            

        tk.Label(self.carrito_window, text=f"Total: {total}", font=("Arial", 14, "bold")).pack(pady=20)


    def modificar_producto(self, producto, cantidad_actual):
        #Modifica la cantidad de un producto en el carrito. 
        def guardar_cambio():
            nueva_cantidad = int(entry.get())
            if nueva_cantidad < 0:
                messagebox.showwarning("Error", "La cantidad no puede ser negativa.")
                return
            if nueva_cantidad == 0:
                self.eliminar_producto(producto)  # Eliminar si la nueva cantidad es 0
            else:
                diferencia = cantidad_actual -nueva_cantidad
                if diferencia > 0:
                    if producto[4] < diferencia:  # Verifica si hay suficiente stock
                        messagebox.showwarning("Sin stock", f"No hay suficiente stock para modificar la cantidad de {producto[1]}.")
                        return
                self.carrito[producto] = nueva_cantidad  # Actualiza la cantidad en el carrito
                self.actualizar_stock_producto(producto, diferencia)  # Actualiza el stock
                self.carrito_window.destroy()  # Cierra la ventana de modificación
                self.mostrarCarrito()  # Actualiza la vista del carrito

        self.modificar_window = tk.Toplevel(self.carrito_window)
        self.modificar_window.title("Modificar Cantidad")
        tk.Label(self.modificar_window, text=f"Modificar cantidad de {producto[1]}:").pack(pady=10)
        entry = tk.Entry(self.modificar_window)
        entry.insert(0, cantidad_actual)
        entry.pack(pady=5)
        tk.Button(self.modificar_window, text="Guardar", command=guardar_cambio).pack(pady=10)


    
    def actualizar(self):
        self.rootCliente.destroy()
        self.objController.mostrar_vista_cliente()

    def actualizar_stock_producto(self, producto, cantidad):
       # Actualiza el stock del producto en la base de datos.
        self.objController.actualizar_inventario(producto[0], -cantidad)  # Actualiza el stock en la base de datos

    def realizar_pedido(self):
        # Realiza el pedido, limpia el carrito y actualiza la interfaz. 
        if not self.carrito:
            messagebox.showwarning("Carrito vacío", "El carrito está vacío, no puedes realizar un pedido.")
            return

        # Muestra los productos en el carrito que serán procesados en el pedido
        productos_carrito = {prod[1]: cant for prod, cant in self.carrito.items()}
        print(f"Pedido realizado con los siguientes productos: {productos_carrito}")

        # Muestra un mensaje de confirmación al usuario
        messagebox.showinfo("Pedido realizado", f"Su pedido ha sido realizado con éxito.")

        # Limpia el carrito
        self.carrito.clear()

        # Cierra la ventana del carrito después de realizar el pedido
        self.carrito_window.destroy()

    def CerrarSesion(self):
        """ Cierra la sesión y vuelve a la ventana principal. """
        self.rootCliente.destroy()
        self.objController.mostrarLogin()  # Llama al método que muestra la ventana de login


