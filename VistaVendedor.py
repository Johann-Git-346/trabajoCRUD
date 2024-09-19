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
        self.create_menu_frame()
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

    def create_menu_frame(self):
        """ Crear el marco para el menú de navegación. """
        self.frame_menu = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)
        self.frame_menu.config(background="#FFFFFF")

        # Botones de navegación
        menu_buttons = ["Informes","Cerrar Sesion"]
        commands = [self.Informes, self.CerrarSesion]

        for text, command in zip(menu_buttons, commands):
            tk.Button(self.frame_menu, text=text,cursor="hand2",bg="#FFD700",foreground="black" ,command=command).grid(row=0, column=menu_buttons.index(text), padx=10, pady=5)

        # Configurar las columnas para que se expandan igualmente
        for i in range(len(menu_buttons)):
            self.frame_menu.grid_columnconfigure(i, weight=1)

    def create_sidebar_frame(self):
        """ Crear el marco para la barra lateral izquierda y añadir botones. """
        self.frame_sidebar = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#FFFFFF")

        # Añadir botones de la barra lateral
        sidebar_buttons = ["Agregar","Modificar", "Eliminar","Guardar"]
        sidebar_commands = [ self.agregar_imagen_a_bd,self.modificar_command, self.eliminar_command,self.guardarComando]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2",bg="#FFD700",foreground="black",text=text, command=command).pack(fill=tk.X, padx=10, pady=20)

        # Controles multimedia (espacios reservados)
        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=10, pady=10)

    def create_catalog_frame(self):
        """ Crear el marco para las categorías y el catálogo. """
        self.frame_catalog = tk.Frame(self.rootVendedor)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#FFFFFF")

        # Crear el marco de categorías
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#FFFFFF")

        # Añadir botones de categorías
        categories = ["Smartphones", "Tablets", "Laptops", "Monitores", "Cámaras", "Audífonos", "Cargadores"]
        comandoCategoria=[self.telefono,self.tablet,self.laptop,self.monitor,self.camara,self.audifonos,self.cargador]
        for text, comandoCategoria in zip(categories,comandoCategoria):
            tk.Button(self.frame_categories,cursor="hand2", bg="#333333",foreground="#FFFFFF",text=text,command=comandoCategoria).pack(side=tk.LEFT, padx=50, pady=5)

        # Crear el título del catálogo
        self.catalog_title = tk.Label(self.frame_catalog, text="Telefonos",foreground="#FFFFFF", font=("Arial", 16))
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#333333")



        # Crear el marco para los productos
        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#FFFFFF")

        self.imagenes_tk = []
        self.labels_imagenes = []

        productos = self.objController.obtener_productos()

        for i in range(2):  # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#FFFFFF")
            
            for j in range(3):  # columnas
                self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
                self.crear_cuadro_producto(row,productos,i,j)

    def crear_cuadro_producto(self, row, productos, i, j):
        self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
        self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)
        img_index = (i * 3) + j
        if img_index < len(productos):
            producto = productos[img_index]
            self.rutaimagen = producto[5]  # Suponiendo que la ruta de la imagen está en la columna 5
            if not os.path.exists(self.rutaimagen):
                print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
                return
            try:
                imagen = Image.open(self.rutaimagen)
                imagen = imagen.resize((110, 110))      
                imagen_tk = ImageTk.PhotoImage(imagen)
                self.imagenes_tk.append(imagen_tk)
                etiqueta_imagen = tk.Label(self.product_frame, image=imagen_tk, width=130, height=100)
                etiqueta_imagen.pack(pady=5)
                self.labels_imagenes.append(etiqueta_imagen)
            except Exception as e:
                print(f"Error al abrir o procesar la imagen: {e}")
        else:
            etiqueta_imagen = tk.Label(self.product_frame, text="No Image", width=10, height=5)
            etiqueta_imagen.pack(pady=5)

        if img_index < len(productos):
            producto = productos[img_index]
            info_label = tk.Label(self.product_frame, text=f"Nombre: {producto[1]}\nPrecio: {producto[2]}\nDescripción: {producto[3]}\nCantidad: {producto[4]}", justify=tk.LEFT)
            info_label.pack()


    def actualizar_imagenes(self, imagenes):
        for img_index, etiqueta_imagen in enumerate(self.labels_imagenes):
            if img_index < len(imagenes):
                self.rutaimagen = imagenes[img_index]
                
                if not os.path.exists(self.rutaimagen):
                    print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
                    continue
            
                try:
                    imagen = Image.open(self.rutaimagen)
                    imagen = imagen.resize((100, 100))      
                    imagen_tk = ImageTk.PhotoImage(imagen)  # Crear una nueva referencia a la imagen
                    self.imagenes_tk[img_index] = imagen_tk  # Actualizar la referencia en la lista
                    
                    etiqueta_imagen.config(image=imagen_tk)
                
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

    def agregarProducto(self,datoNombre,datoPrecio,datoCategoria,datoCantidad):
        nombre = datoNombre.get()
        precio = datoPrecio.get()
        categoria = datoCategoria.get()
        cantidad = datoCantidad.get()

        if not nombre or not precio or not categoria or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios para agregar un producto")
            return

        try:
            self.objController.agregar_productos(nombre,precio,categoria,cantidad)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.actualizar_lista_productos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el precio y la cantidad")

    def agregar_imagen_a_bd(self):
        self.agregarProducto2=tk.Toplevel()
        self.agregarProducto2.title("Agregando producto")
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
        
    def catalogoTelefono(self):
        self.catalog_title.config(text="Telefonos")
        #self.actualizar_imagenes(self.imagenes4)

    def catalogoTablet(self):
        self.catalog_title.config(text="Tablets")
    def catalogoLaptop(self):
        self.catalog_title.config(text="Laptops")
        #self.actualizar_imagenes(self.imagenes)

    def catalogoMonitor(self):
        self.catalog_title.config(text="Monitores")
    def catalogoCamara(self):
        self.catalog_title.config(text="Camaras")
    def catalogoAudifonos(self):
        self.catalog_title.config(text="Audifonos")
    def catalogoCargador(self):
        self.catalog_title.config(text="Cargadores")

    # Métodos de comando para los botones
    def guardarComando(self):
        print("guardar button clicked")

    def eliminar_command(self):
        print("eliminar button clicked")

    def modificar_command(self):
        print("agregar button clicked")

    def CerrarSesion(self):
        self.mensajeCerrrarSesion=tk.Toplevel()
        self.mensajeCerrrarSesion.title("¿seguro?")
        self.mensajeCerrrarSesion.geometry("300x200")
        self.mensajeCerrrarSesion.config(background="lightblue")
        self.respuesta=tk.StringVar()
        self.contenedorMensaje=tk.Frame(self.mensajeCerrrarSesion)
        self.contenedorMensaje.pack()
        self.labelMensaje=tk.Label(self.contenedorMensaje,text="¿Esta seguro que desea cerrar sesion?",font=("Arial", 12))
        self.labelMensaje.pack(padx=10,pady=10)
        self.botonSi=tk.Button(self.contenedorMensaje,text="SI",width=5,height=2,command=self.salirTodo)
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
        print("telfono")
        self.catalogoTelefono()

    def tablet(self):
        print("tablet")
        self.catalogoTablet()

    def laptop(self):
        print("laptop")
        self.catalogoLaptop()

    def monitor(self):
        print("monitor")
        self.catalogoMonitor()

    def camara(self):
        print("camara")
        self.catalogoCamara()

    def audifonos(self):
        print("audifonos")
        self.catalogoAudifonos()

    def cargador(self):
        print("cargador")
        self.catalogoCargador()