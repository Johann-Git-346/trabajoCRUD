import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import messagebox
class Davista2:
    def __init__(self,objController):
        self.objController=objController
    

    def iniciarVendedor(self):
        self.rootVendedor = tk.Tk()
        self.rootVendedor.title("ADMINISTRADOR")
        self.rootVendedor.geometry("800x600")

        self.create_top_frame()
        self.create_sidebar_frame()
        self.create_catalog_frame()
        self.rootVendedor.mainloop()
        

    def create_top_frame(self):
        """ Crear el marco superior para el nombre de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_top.config(background="#333333")

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_left = tk.Frame(self.frame_top)
        spacer_left.pack(side=tk.LEFT, expand=True)

        company_name = tk.Label(self.frame_top, text="TecnoNube", font=("Arial", 24),foreground="#FFFFFF", anchor="center")
        company_name.pack(side=tk.LEFT, padx=10, pady=10)
        company_name.config(background="#333333")

        logo = tk.Frame(self.frame_top,width=20,height=20)
        logo.pack(side=tk.RIGHT, padx=10, pady=10)
        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_right = tk.Frame(self.frame_top)
        spacer_right.pack(side=tk.RIGHT, expand=True)
            

        etiqueta = tk.Label(logo)
        etiqueta.pack(side=tk.RIGHT)

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

        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")



    def create_sidebar_frame(self):
        """ Crear el marco para la barra lateral izquierda y añadir botones. """
        self.frame_sidebar = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#FFFFFF")

        # Añadir botones de la barra lateral
        sidebar_buttons = ["Agregar","Modificar", "Eliminar","cerrar sesion"]
        sidebar_commands = [ self.agregar_producto, self.guardarComando, self.eliminar_command, self.CerrarSesion]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2",bg="#FFD700",foreground="black",text=text, command=command).pack(fill=tk.X, padx=10, pady=20)

        # Controles multimedia (espacios reservados)
        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=10, pady=10)




    #Dato
    def create_catalog_frame(self):
        """ Crear el marco para las categorías y el catálogo. """
        self.productos = self.objController.obtener_productos()

        self.frame_catalog = tk.Frame(self.rootVendedor)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#FFFFFF")

        # Crear el marco de categorías
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#FFFFFF")

        # Añadir botones de categorías
        categories = ["Teléfonos", "Laptops"]
        comandos_categoria = [self.telefono,self.laptop]

        for text, comando in zip(categories, comandos_categoria):
            tk.Button(self.frame_categories, cursor="hand2", bg="#333333", foreground="#FFFFFF", text=text, command=comando).pack(side=tk.LEFT, padx=100, pady=5)

        # Crear el título del catálogo
        self.catalog_title = tk.Label(self.frame_catalog, text="Teléfonos", foreground="#FFFFFF", font=("Arial", 16))
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#333333")

        # Crear el marco para los productos
        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#FFFFFF")

        # Inicialmente mostrar teléfonos
        self.mostrar_productos_categoria("celular")
    
    #oreo dato
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

        filas = (len(self.productos_filtrados) // 3) + (1 if len(self.productos_filtrados) % 3 != 0 else 0)  # Calcular filas necesarias

        for i in range(filas):  # Crear las filas necesarias
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#FFFFFF")
            
            for j in range(3):  # columnas
                img_index = (i * 3) + j
                if img_index < len(self.productos_filtrados):  # Asegurarse de que el índice no sobrepase los productos filtrados
                    self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                    self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                    self.crear_cuadro_producto(self.product_frame, self.productos_filtrados[img_index])

    def crear_cuadro_producto(self, product_frame, producto):
        """ Crea un cuadro individual para un producto. """
        self.rutaimagen = producto[5]  # Suponiendo que la ruta de la imagen está en la columna 5
        
        if not os.path.exists(self.rutaimagen):
            print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
            return
        
        try:
            imagen = Image.open(self.rutaimagen)
            imagen = imagen.resize((110, 110))      
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.imagenes_tk.append(imagen_tk)  # Guardar referencia para evitar que la imagen sea recolectada por el GC
            etiqueta_imagen = tk.Label(product_frame, image=imagen_tk, width=130, height=100)
            etiqueta_imagen.pack(pady=5)
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")
        
        # Información del producto
        info_label = tk.Label(product_frame, text=f"Nombre: {producto[1]}\nPrecio: {producto[2]}\nCantidad: {producto[4]}", justify=tk.LEFT)
        info_label.pack()

    def actualizar_catalogo(self,categoria):
        self.productos = self.objController.obtener_productos()
        """ Método para refrescar el catálogo de productos. """
        self.productos_filtrados = [p for p in self.productos if p[3] == categoria]
        # Limpiar el marco de productos antes de agregar los productos actualizados
        for widget in self.frame_products.winfo_children():
            widget.destroy()

        # Volver a crear los cuadros de productos actualizados
        self.imagenes_tk = []  # Limpiar la lista de imágenes

        # Obtener productos actualizados desde el controlador
        #self.productos = self.objController.obtener_productos()

        filas = (len(self.productos_filtrados) // 3) + (1 if len(self.productos_filtrados) % 3 != 0 else 0)  # Calcular filas necesarias

        for i in range(filas):  # Crear las filas necesarias
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#FFFFFF")
            
            for j in range(3):  # columnas
                img_index = (i * 3) + j
                if img_index < len(self.productos_filtrados):
                    self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                    self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                    self.crear_cuadro_producto(self.product_frame, self.productos_filtrados[img_index])

        print("Catálogo actualizado.")

    def actualizar_imagenes(self, productos):
        for img_index, etiqueta_imagen in enumerate(self.labels_imagenes):
            if img_index < len(productos):
                producto = productos[img_index]
                self.rutaimagen = producto[5]  # Suponiendo que la ruta de la imagen está en la columna 5
                categoria = producto[3]  # Suponiendo que la categoría está en la columna 6
                
                if not os.path.exists(self.rutaimagen):
                    print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
                    continue
                
                try:
                    imagen = Image.open(self.rutaimagen)
                    imagen = imagen.resize((100, 100))      
                    imagen_tk = ImageTk.PhotoImage(imagen)  # Crear una nueva referencia a la imagen
                    self.imagenes_tk[img_index] = imagen_tk  # Actualizar la referencia en la lista
                    
                    etiqueta_imagen.config(image=imagen_tk)
                    etiqueta_imagen.config(text=f"Categoría: {categoria}")  # Mostrar la categoría
                except Exception as e:
                    print(f"Error al abrir o procesar la imagen: {e}")

    def agregar_producto(self):
        self.ventanaAgregar=tk.Toplevel()
        self.ventanaAgregar.title("agregar producto")
        self.ventanaAgregar.geometry("500x500")
        self.contenedor2=tk.Frame(self.ventanaAgregar)
        self.contenedor2.pack()
        nombre=tk.StringVar()
        precio=tk.DoubleVar()
        categoria=tk.StringVar()
        cantidad=tk.IntVar()
        self.labelNombre=tk.Label(self.contenedor2, text="ingrese el nombre del producto")
        self.labelNombre.pack(padx=10,pady=10)
        self.entryNombre=tk.Entry(self.contenedor2,textvariable=nombre)
        self.entryNombre.pack(padx=10,pady=10)
        self.labelPrecio=tk.Label(self.contenedor2, text="ingrese el precio del producto")
        self.labelPrecio.pack(padx=10,pady=10)
        self.entryPrecio=tk.Entry(self.contenedor2, textvariable=precio)
        self.entryPrecio.pack(padx=10,pady=10)
        self.labeCategoria=tk.Label(self.contenedor2, text="ingrese la categoria")
        self.labeCategoria.pack(padx=10,pady=10)
        self.entryCategoria=tk.Entry(self.contenedor2, textvariable=categoria)
        self.entryCategoria.pack(padx=10,pady=10)
        self.labelCantidad=tk.Label(self.contenedor2, text="ingrese la cantidad del producto")
        self.labelCantidad.pack(padx=10,pady=10)
        self.entryCantidad=tk.Entry(self.contenedor2, textvariable=cantidad)
        self.entryCantidad.pack(padx=10,pady=10)
        self.boton=tk.Button(self.contenedor2, text="agregar",command=lambda: self.agregarProducto(nombre,precio,categoria,cantidad))
        self.boton.pack(padx=10,pady=10)
        #self.actualizar_catalogo()

    def agregarProducto(self,datoNombre,datoPrecio,datoCategoria,datoCantidad):
        self.ventanaAgregar.destroy()
        nombre = datoNombre.get()
        precio = datoPrecio.get()
        categoria = datoCategoria.get()
        cantidad = datoCantidad.get()

        if not nombre or not precio or not categoria or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios para agregar un producto")
            return

        try:
            self.objController.agregar_productos(nombre,precio,categoria,cantidad)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")

    def agregar_imagen_a_bd(self):
        self.agregarProducto2=tk.Toplevel()
        self.agregarProducto2.title("Agregando imagen")
        self.agregarProducto2.geometry("400x400")
        nombre=tk.StringVar()
        contenedor=tk.Frame(self.agregarProducto2)
        contenedor.pack()
        self.label=tk.Label(contenedor,text="ingrese el nombre del producto")
        self.label.pack(padx=10,pady=10)
        self.entry=tk.Entry(contenedor,textvariable=nombre)
        self.entry.pack(padx=10,pady=10)
        self.boton=tk.Button(contenedor,text="agregar imagen", command=lambda:self.montarImagen(nombre))
        self.boton.pack(padx=10,pady=10)

    def montarImagen(self,datoNombre):
        self.agregarProducto2.destroy()
        nombre=datoNombre.get()
        # Abre el diálogo para seleccionar una imagen
        ruta_imagen = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=(("Archivos de imagen", ".jpg;.jpeg;.png"), ("Todos los archivos", ".*"))
        )
        
        if not ruta_imagen:
            print("No se seleccionó ninguna imagen")
            return
        imagen=ruta_imagen
        self.objController.subirImagen(nombre,imagen)
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        
    def catalogoTelefono(self,productos):
        self.catalog_title.config(text="Telefono")
        self.actualizar_imagenes(productos)
        #self.actualizar_imagenes(self.imagenes4)

    def catalogoLaptop(self):
        self.catalog_title.config(text="Laptops")
        #self.actualizar_imagenes(self.imagenes)

    # Métodos de comando para los botones
    def guardarComando(self):
        self.ventanaModificar=tk.Toplevel()
        self.ventanaModificar.title("modificar producto")
        self.ventanaModificar.geometry("500x500")
        self.contenedor4=tk.Frame(self.ventanaModificar)
        self.contenedor4.pack(padx=10,pady=10)
        nombre=tk.StringVar()
        precioNuevo=tk.DoubleVar()
        categoriaNueva=tk.StringVar()
        cantidadNueva=tk.IntVar()
        self.labelNombre=tk.Label(self.contenedor4, text="ingrese el nombre del producto")
        self.labelNombre.pack(padx=10,pady=10)
        self.entryNombre=tk.Entry(self.contenedor4,textvariable=nombre)
        self.entryNombre.pack(padx=10,pady=10)
        self.labelPrecio=tk.Label(self.contenedor4, text="ingrese el nuevo precio del producto")
        self.labelPrecio.pack(padx=10,pady=10)
        self.entryPrecio=tk.Entry(self.contenedor4, textvariable=precioNuevo)
        self.entryPrecio.pack(padx=10,pady=10)
        self.labeCategoria=tk.Label(self.contenedor4, text="ingrese la nueva categoria")
        self.labeCategoria.pack(padx=10,pady=10)
        self.entryCategoria=tk.Entry(self.contenedor4, textvariable=categoriaNueva)
        self.entryCategoria.pack(padx=10,pady=10)
        self.labelCantidad=tk.Label(self.contenedor4, text="ingrese la nueva cantidad del producto")
        self.labelCantidad.pack(padx=10,pady=10)
        self.entryCantidad=tk.Entry(self.contenedor4, textvariable=cantidadNueva)
        self.entryCantidad.pack(padx=10,pady=10)
        self.boton=tk.Button(self.contenedor4, text="agregar",command=lambda: self.modificar_producto(nombre,precioNuevo,categoriaNueva,cantidadNueva))
        self.boton.pack(padx=10,pady=10)
        #self.actualizar_catalogo()

    def modificar_producto(self,datoNombre,datoPrecio,datoCategoria,datoCantidad):
        nombre = datoNombre.get()
        nuevo_precio = datoPrecio.get()
        nueva_categoria = datoCategoria.get()
        nueva_cantidad = datoCantidad.get()

        if not nombre:
            messagebox.showerror("Error", "El nombre del producto es obligatorio para modificarlo")
            return

        try:
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            producto = self.objController.obtener_producto_por_nombre(nombre)
            if producto:
                self.objController.modificar_producto(nombre, nuevo_precio, nueva_categoria, nueva_cantidad)
                self.agregar_imagen_a_bd()
                messagebox.showinfo("Éxito", "Producto modificado con éxito")
            else:
                messagebox.showerror("Error", "Producto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")

    def eliminar_command(self):
        self.ventanaEliminar=tk.Toplevel()
        self.ventanaEliminar.title("eliminar producto")
        self.ventanaEliminar.geometry("500x500")
        self.contenedor3=tk.Frame(self.ventanaEliminar)
        self.contenedor3.pack(padx=10,pady=10)
        nombreEliminar=tk.StringVar()
        self.labelEliminar=tk.Label(self.contenedor3,text="ingrese el nombre del producto a eliminar")
        self.labelEliminar.pack(padx=10,pady=10)
        self.entryEliminar=tk.Entry(self.contenedor3, textvariable=nombreEliminar)
        self.entryEliminar.pack(padx=10,pady=10)
        self.botonEliminar=tk.Button(self.contenedor3, text="eliminar",command=lambda:self.eliminar_producto(nombreEliminar))
        self.botonEliminar.pack(padx=10,pady=10)
        #self.actualizar_catalogo()

    def eliminar_producto(self,datoEliminar):
        nombre = datoEliminar.get()
        if not nombre:
            messagebox.showerror("Error", "El nombre del producto es obligatorio para eliminarlo")
            return

        producto = self.objController.obtener_producto_por_nombre(nombre)
        if producto:
            self.objController.eliminar_producto(nombre)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def CerrarSesion(self):
        self.mensajeCerrrarSesion=tk.Toplevel()
        self.mensajeCerrrarSesion.title("¿seguro?")
        self.mensajeCerrrarSesion.geometry("300x200")
        self.mensajeCerrrarSesion.config(bg="lightblue")
        self.respuesta=tk.StringVar()
        self.contenedorMensaje=tk.Frame(self.mensajeCerrrarSesion,bg="lightblue")
        self.contenedorMensaje.pack()
        self.labelMensaje=tk.Label(self.contenedorMensaje,text="¿Esta seguro que desea cerrar sesion?",font=("Arial", 12))
        self.labelMensaje.pack(padx=10,pady=10)
        self.botonSi=tk.Button(self.contenedorMensaje,text="SI",width=5,height=2,command=self.salirTodo,bg="red")
        self.botonSi.pack(padx=10,pady=10)
        self.botonNo=tk.Button(self.contenedorMensaje,text="NO",width=5,height=2,command=self.destruirMensaje)
        self.botonNo.pack(padx=10,pady=10)
        
    def destruirMensaje(self):
        self.mensajeCerrrarSesion.destroy()

    def salirTodo(self):
        self.mensajeCerrrarSesion.destroy()
        self.rootVendedor.destroy()
        self.objController.mostrarLogin()

    def Informes(self):
        self.objController.vistaInformes()

    def telefono(self):
        print("telefono")
        self.mostrar_productos_categoria("Teléfonos")
        self.actualizar_catalogo("Teléfonos")

    def laptop(self):
        print("laptop")
        self.mostrar_productos_categoria("Laptop")
        self.actualizar_catalogo("laptop")
