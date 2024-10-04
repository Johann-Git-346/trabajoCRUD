import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import io
from tkinter import messagebox,ttk
#Vista Vendedor
class Davista2:
    def __init__(self,objController):
        self.objController=objController
    
    def iniciarVendedor(self):
        self.rootVendedor = tk.Tk()
        self.rootVendedor.title("PRODUCTOS")
        self.rootVendedor.geometry("800x600")

        self.rootVendedor.state('zoomed')

        self.CrearSlider()
        self.CrearSliderLateral()
        self.CrearSliderCatalogo()
        self.rootVendedor.mainloop()
        
    def CrearSlider(self):
        """ Crear el marco superior para el nombre de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_top.config(background="#333333")

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_left = tk.Frame(self.frame_top)
        spacer_left.pack(side=tk.LEFT, expand=True)
        spacer_left.config(background="#333333")

        company_name = tk.Label(self.frame_top, text="TecnoNube", font=("Arial", 24,"bold"),foreground="#FFFFFF", anchor="center")
        company_name.pack(side=tk.LEFT, padx=10, pady=10)
        company_name.config(background="#333333")

        logo = tk.Frame(self.frame_top,width=20,height=20)
        logo.pack(side=tk.RIGHT, padx=10, pady=10)
        logo.config(background="#333333")
        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_right = tk.Frame(self.frame_top)
        spacer_right.pack(side=tk.RIGHT, expand=True)
        spacer_right.config(background="#333333")
            
        etiqueta = tk.Label(logo)
        etiqueta.pack(side=tk.RIGHT)
        etiqueta.config(background="#333333")

        self.rutaimagen2= "imagenes/LOGO.jpg"

        if not os.path.exists(self.rutaimagen2):
            print(f"Error: La ruta de la imagen no existe: {self.rutaimagen2}")
            return
        
        try:
            imagen2 = Image.open(self.rutaimagen2)
            imagen2 = imagen2.resize((155, 130))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen2) # Mantén la referencia a la imagen
            
            etiqueta_imagen = tk.Label(logo, image=self.imagen_tk2)
            etiqueta_imagen.pack()
            etiqueta_imagen.config(bg="#333333")

        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

    def CrearSliderLateral(self):
        """ Crear el marco para la barra lateral izquierda y añadir botones. """
        self.frame_sidebar = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#D3D3D3")

        # Añadir botones de la barra lateral
        sidebar_buttons = ["Productos","Informes","Cerrar sesion"]
        sidebar_commands = [self.mostrarProductos,self.mostrarInforme,self.CerrarSesion]
        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2",bg="#87CEEB",foreground="black",font=("Arial", 10,"bold"),text=text, command=command).pack(fill=tk.X, padx=10, pady=20)

        # Controles multimedia (espacios reservados)
        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=10, pady=10)

    def CrearSliderCatalogo(self):
        """ Crear el marco para las categorías y el catálogo. """
        self.productos = self.objController.obtener_productos()

        self.frame_catalog = tk.Frame(self.rootVendedor)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#D3D3D3")

        # Crear el marco de categorías
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#D3D3D3")

        # Añadir botones de categorías
        categories = ["Celular","Laptops"]
        comandoCategoria=[self.catalogoTelefono, self.catalogoLaptop]
        for text, comandoCategoria in zip(categories, comandoCategoria):
            tk.Button(self.frame_categories,cursor="hand2", bg="#ADD8E6",font=("Arial", 10,"bold"),foreground="black",text=text,command=comandoCategoria).pack(side=tk.LEFT, padx=280, pady=5)

        # Crear el título del catálogo
        self.catalog_title = tk.Label(self.frame_catalog, text="Celular",foreground="#000000", font=("Arial", 16,"bold"),relief=tk.GROOVE, borderwidth=2)
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#B0E0E6")

        # Crear el marco para los self.productos
        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#D3D3D3")
        
        # Inicialmente mostrar teléfonos
        self.mostrar_productos_categoria("celular")
    
    def mostrar_productos_categoria(self, categoria):
            """ Muestra los productos filtrados por categoría. """
            self.catalog_title.config(text=categoria)

            # Filtrar productos por categoría
            self.productos_filtrados = [p for p in self.productos if p[3] == categoria]

            # Limpiar el marco de productos antes de agregar los productos filtrados
            for widget in self.frame_products.winfo_children():
                widget.destroy()

            # Volver a crear los cuadros de productos filtrados
            self.imagenes_tk = []  # Limpiar la lista de imágenes
            self.labels_imagenes = []  # Limpiar la lista de etiquetas

            filas = (len(self.productos_filtrados) // 3) + (1 if len(self.productos_filtrados) % 3 != 0 else 0)  

            for i in range(filas):  # Crear las filas 
                row = tk.Frame(self.frame_products)
                row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
                row.config(background="#D3D3D3")
                
                for j in range(7):  # columnas
                    img_index = (i * 7) + j
                    if img_index < len(self.productos_filtrados):  
                        self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                        self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                        self.product_frame.config(bg="#B0E0E6")
                        self.crear_cuadro_producto(self.product_frame, self.productos_filtrados[img_index])

    def crear_cuadro_producto(self, product_frame, producto):
        """ Crea un cuadro individual para un producto. """
        try:
            # Convertir la imagen binaria a un objeto de imagen
            imagen = Image.open(io.BytesIO(producto[5]))
            imagen = imagen.resize((110, 110))      
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.imagenes_tk.append(imagen_tk)  
            etiqueta_imagen = tk.Label(product_frame, image=imagen_tk, width=130, height=100)
            etiqueta_imagen.pack(pady=5)
            etiqueta_imagen.config(bg="#B0E0E6")
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")
        
        # Información del producto
        info_label = tk.Label(product_frame, text=f"Nombre: {producto[1]}\nPrecio: {producto[2]}\nCantidad: {producto[4]}", justify=tk.LEFT)
        info_label.pack()
        info_label.config(bg="#B0E0E6", font=("Arial", 10, "bold"), foreground="#000000")

    def actualizar_catalogo(self, categoria):
        self.productos = self.objController.obtener_productos()
        """ Método para refrescar el catálogo de productos. """
        self.productos_filtrados = [p for p in self.productos if p[3] == categoria]
        # Limpiar el marco de productos antes de agregar los productos actualizados
        for widget in self.frame_products.winfo_children():
            widget.destroy()

        self.imagenes_tk = []  

        filas = (len(self.productos_filtrados) // 3) + (1 if len(self.productos_filtrados) % 3 != 0 else 0)  

        for i in range(filas): # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#D3D3D3")
            
            for j in range(7):  # columnas
                img_index = (i * 7) + j
                if img_index < len(self.productos_filtrados):
                    self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                    self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                    self.product_frame.config(bg="#B0E0E6")
                    self.crear_cuadro_producto(self.product_frame, self.productos_filtrados[img_index])

        print("Catálogo actualizado.")

    def montarImagen(self,nombre):
        # Abre el diálogo para seleccionar una imagen
        ruta_imagen = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=(("Archivos de imagen", ".jpg;.jpeg;.png"), ("Todos los archivos", ".*"))
        )
        
        if not ruta_imagen:
            print("No se seleccionó ninguna imagen")
            return
        imagen=ruta_imagen
        self.convertir_imagen_a_binario(nombre,imagen)
        messagebox.showinfo("Éxito", "Producto agregado correctamente")

    def convertir_imagen_a_binario(self,nombre,ruta_imagen):
        with open(ruta_imagen, 'rb') as archivo:
            binario = archivo.read()
        return self.objController.subirImagen2(nombre,binario)

    def catalogoTelefono(self):
        self.catalog_title.config(text="celulares")
        self.mostrar_productos_categoria("celular")
        self.actualizar_catalogo("celular")

    def catalogoLaptop(self):
        self.catalog_title.config(text="Laptops")
        self.mostrar_productos_categoria("laptop")
        self.actualizar_catalogo("laptop")

    def mostrarProductos(self):
        self.rootVendedor.destroy()
        self.ventanaMostrar=tk.Tk()
        self.ventanaMostrar.title("Productos")
        self.ventanaMostrar.config(background="#D3D3D3")
        self.ventanaMostrar.state('zoomed')
        self.frameMostrar = tk.Frame(self.ventanaMostrar,bg="#D3D3D3")
        self.frameMostrar.pack(fill=tk.BOTH, expand=True)

        mostrarProductos = tk.Label(self.frameMostrar, text="Productos",foreground="#000000", font=("Arial", 16,"bold"),bg="#B0E0E6",relief=tk.SOLID, borderwidth=1)
        mostrarProductos.pack(side=tk.TOP, pady=20,padx=30)

        self.mostrarProductos_tree = ttk.Treeview(self.frameMostrar,columns=("ID","Producto", "Cantidad", "Categoria","Precio" , "Imagen"), show="headings")
        self.mostrarProductos_tree.heading("ID", text="ID")
        self.mostrarProductos_tree.heading("Producto", text="Nombre Producto")
        self.mostrarProductos_tree.heading("Cantidad", text="Cantidad")
        self.mostrarProductos_tree.heading("Categoria", text="Categoria")
        self.mostrarProductos_tree.heading("Precio", text="Precio")
        self.mostrarProductos_tree.heading("Imagen", text="Imagen")
        
        self.mostrarProductos_tree.column("ID", width=30)
        self.mostrarProductos_tree.column("Producto", width=30)
        self.mostrarProductos_tree.column("Cantidad", width=30)
        self.mostrarProductos_tree.column("Categoria", width=30)
        self.mostrarProductos_tree.column("Precio", width=30)
        self.mostrarProductos_tree.column("Imagen", width=30)

        self.cargar_datos()

        self.mostrarProductos_tree.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        self.mostrarProductos_tree.bind("<ButtonRelease-1>", self.on_tree_select)

        entry_frame = tk.Frame(self.frameMostrar,bg="#D3D3D3")
        entry_frame.pack(padx=5, pady=5)

        Id=tk.IntVar()
        nombre=tk.StringVar()
        precio=tk.DoubleVar()
        categoria=tk.StringVar()
        cantidad=tk.IntVar()

        self.labelId = tk.Label(entry_frame, text="ID:",bg="#D3D3D3",font=("Arial", 10,"bold"),foreground="black")
        self.labelId.pack(side=tk.LEFT, padx=15, pady=5)
        self.entry_Id = tk.Entry(entry_frame,textvariable=Id)
        self.entry_Id.pack(side=tk.LEFT, padx=10, pady=5)

        self.labelProducto = tk.Label(entry_frame, text="Nombre:",bg="#D3D3D3",font=("Arial", 10,"bold"),foreground="black")
        self.labelProducto.pack(side=tk.LEFT, padx=15, pady=5)
        self.entry_producto = tk.Entry(entry_frame,textvariable=nombre)
        self.entry_producto.pack(side=tk.LEFT, padx=10, pady=5)

        self.labelCantidad = tk.Label(entry_frame, text="Cantidad:",bg="#D3D3D3",font=("Arial", 10,"bold"),foreground="black")
        self.labelCantidad.pack(side=tk.LEFT, padx=15, pady=5)
        self.entry_cantidad = tk.Entry(entry_frame,textvariable=cantidad)
        self.entry_cantidad.pack(side=tk.LEFT, padx=10, pady=5)

        self.labelCategoria = tk.Label(entry_frame, text="Categoria:",bg="#D3D3D3",font=("Arial", 10,"bold"),foreground="black")
        self.labelCategoria.pack(side=tk.LEFT, padx=15, pady=5)
        self.entry_categoria = tk.Entry(entry_frame,textvariable=categoria)
        self.entry_categoria.pack(side=tk.LEFT, padx=10, pady=5)

        self.labelPrecio = tk.Label(entry_frame, text="Precio:",bg="#D3D3D3",font=("Arial", 10,"bold"),foreground="black")
        self.labelPrecio.pack(side=tk.LEFT, padx=5, pady=5)
        self.entry_Precio = tk.Entry(entry_frame,textvariable=precio)
        self.entry_Precio.pack(side=tk.LEFT, padx=10, pady=5)

        button_frame = tk.Frame(self.frameMostrar,bg="#D3D3D3")
        button_frame.pack(padx=5, pady=5)

        datos=[Id,nombre,cantidad,categoria,precio]

        self.botonAgregar=tk.Button(button_frame,text="Agregar",command=lambda:self.agregar_Producto(datos),cursor="hand2", bg="#87CEEB",font=("Arial", 10,"bold"),foreground="black")
        self.botonAgregar.pack(side=tk.LEFT, padx=15, pady=5)

        self.buttonModificar = tk.Button(button_frame, text="Modificar", command=lambda:self.modificarDatos(datos),cursor="hand2", bg="#87CEEB",font=("Arial", 10,"bold"),foreground="black")
        self.buttonModificar.pack(side=tk.LEFT, padx=15, pady=5)

        self.buttonEliminar = tk.Button(button_frame, text="Eliminar", command=lambda:self.eliminarDatos(datos),cursor="hand2", bg="#87CEEB",font=("Arial", 10,"bold"),foreground="black")
        self.buttonEliminar.pack(side=tk.LEFT, padx=15, pady=5)

        self.buttonImagen = tk.Button(button_frame, text="agregar/actualizar imagen", command=lambda:self.agregar_modificar_imagen(datos),cursor="hand2", bg="#87CEEB",font=("Arial", 10,"bold"),foreground="black")
        self.buttonImagen.pack(side=tk.LEFT, padx=15, pady=5)

        self.buttonSalir = tk.Button(button_frame, text="Volver", command=self.volverInicio,cursor="hand2", bg="#ADD8E6",font=("Arial", 10,"bold"),foreground="black",)
        self.buttonSalir.pack(side=tk.LEFT, padx=15, pady=5)

    def cargar_datos(self):
        for item in self.mostrarProductos_tree.get_children():
            self.mostrarProductos_tree.delete(item)
        self.Productos = self.objController.obtener_productos()
        for producto in self.Productos:
            imagen_text = "Sí" if producto[5] else "No"
            self.mostrarProductos_tree.insert("", "end", values=(producto[0], producto[1], producto[4], producto[3],producto[2], imagen_text))

    def on_tree_select(self, event):
        selected_item = self.mostrarProductos_tree.selection()[0]
        item_values = self.mostrarProductos_tree.item(selected_item, "values")
        self.entry_Id.delete(0, tk.END)
        self.entry_Id.insert(0, item_values[0])
        self.entry_producto.delete(0, tk.END)
        self.entry_producto.insert(0, item_values[1])
        self.entry_cantidad.delete(0, tk.END)
        self.entry_cantidad.insert(0, item_values[2])
        self.entry_categoria.delete(0, tk.END)
        self.entry_categoria.insert(0, item_values[3])
        self.entry_Precio.delete(0, tk.END)
        self.entry_Precio.insert(0, item_values[4])
        self.selected_item = selected_item

    def agregar_Producto(self,dato):
        Id=dato[0].get()
        nombre=dato[1].get()
        cantidad=dato[2].get()
        categoria=dato[3].get()
        precio=dato[4].get()
        if not nombre or not precio or not categoria or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios para agregar un producto")
            return

        try:
            self.objController.agregar_productos(Id,nombre,precio,categoria,cantidad)
            self.cargar_datos()
            self.limpiar_campos()
            messagebox.showinfo("Exito","producto creado con exito")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")

    def modificarDatos(self,dato):
        nombre2=dato[1].get()
        nuevo_nombre=dato[1].get()
        nuevo_cantidad=dato[2].get()
        nuevo_categoria=dato[3].get()
        nuevo_precio=dato[4].get()
        try:
            self.objController.modificar_producto(nombre2,nuevo_nombre,nuevo_precio,nuevo_categoria,nuevo_cantidad)
            self.cargar_datos()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Producto modificado con éxito")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")


    def eliminarDatos(self,dato):
        Id=dato[0].get()
        nombre=dato[1].get()
        producto = self.objController.obtener_producto_por_nombre(nombre)
        if producto:
            self.objController.eliminar_producto(Id)
            self.cargar_datos()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def agregar_modificar_imagen(self,dato):
        nombre=dato[1].get()
        self.montarImagen(nombre)
        self.cargar_datos()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_producto.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_Precio.delete(0, tk.END)

    def volverInicio(self):
        self.ventanaMostrar.destroy()
        self.iniciarVendedor()

    def mostrarInforme(self):
        user_role = self.objController.get_user_role()
        if user_role == 'administra':
            self.rootVendedor.destroy()
            self.objController.vistaInformes()
        else:
            messagebox.showerror("Error","solo los administradores pueden realizar esta acción")
            print("solo los administradores pueden realizar esta acción")

    def CerrarSesion(self):
        confirm = messagebox.askyesno("Cerrar Sesión", "¿Está seguro de que desea cerrar sesión?")
        if confirm:
            self.rootVendedor.destroy()
            self.objController.mostrarLogin()