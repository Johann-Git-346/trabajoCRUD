import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

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
        self.imagenes=[]
        #"imagenes/compu1.jpg","imagenes/compu2.jpg","imagenes/compu3.jpeg","imagenes/compu4.jpg","imagenes/compu5.jpeg","imagenes/compu6.png",
        #       "imagenes/compu7.jpeg","imagenes/compu8.jpg","imagenes/compu9.jpeg","imagenes/compu10.jpg","imagenes/compu11.jpg","imagenes/compu12.jpg",
        #       "imagenes/compu13.png","imagenes/compu14.png"
        self.imagenes4=[]
        #"imagenes/cel.jpg","imagenes/cel2.jpg","imagenes/cel3.jpg","imagenes/cel4.jpg","imagenes/cel5.jpg","imagenes/cel6.jpeg",
        #               "imagenes/cel7.jpeg","imagenes/cel8.jpeg","imagenes/cel9.jpg","imagenes/cel10.jpg","imagenes/cel11.png","imagenes/cel12.jpg",
        #               "imagenes/cel13.jpg","imagenes/cel14.jpg"
        self.imagenes_tk = []
        self.labels_imagenes = []

        for i in range(2):
             # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#FFFFFF")
            for j in range(7):  # columnas
                self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)

                # Asignar una imagen diferente a cada producto
                img_index = (i * 7) + j  # Calcular el índice de la imagen
                if img_index < len(self.imagenes4):
                    self.rutaimagen = self.imagenes4[img_index]
                    
                    if not os.path.exists(self.rutaimagen):
                        print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
                        continue
                
                    try:
                        imagen = Image.open(self.rutaimagen)
                        imagen = imagen.resize((110, 110))      
                        imagen_tk = ImageTk.PhotoImage(imagen)  # Crear una nueva referencia a la imagen
                        self.imagenes_tk.append(imagen_tk)  # Guardar la referencia en la lista
                        
                        etiqueta_imagen = tk.Label(self.product_frame, image=imagen_tk, width=130, height=100)
                        etiqueta_imagen.pack(pady=5)
                        self.labels_imagenes.append(etiqueta_imagen)
                    
                    except Exception as e:
                        print(f"Error al abrir o procesar la imagen: {e}")
                else:
                    etiqueta_imagen = tk.Label(self.product_frame, text="No Image", width=10, height=5)
                    etiqueta_imagen.pack(pady=5)
                info_label = tk.Label(self.product_frame, text=f"Producto {img_index + 1}\nCategoría\nPrecio", justify=tk.LEFT)
                info_label.pack()
        #productos = self.controller.obtener_productos()
        #for producto in productos:
        #    self.product_listbox.insert(tk.END, f"Nombre: {producto[1]}, Precio: {producto[2]}, Descripcion:{producto[3]}, Cantidad: {producto[4]}")


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


    def agregar_imagen_a_bd(self):
        self.agregarProducto=tk.Toplevel()
        self.agregarProducto.title("Agregando producto")
        self.agregarProducto.geometry("400x400")
        contenedor=tk.Frame(self.agregarProducto)
        contenedor.pack()
        self.label=tk.Label(contenedor,text="ingrese el nombre del producto")
        self.label.pack(padx=10,pady=10)
        self.entry=tk.Entry(contenedor,textvariable=self.label)
        self.entry.pack(padx=10,pady=10)
        self.boton=tk.Button(contenedor,text="agregar imagen", command=lambda:self.montarImagen(self.label))
        self.boton.pack(padx=10,pady=10)

    def montarImagen(self,datoNombre):
        dato=[datoNombre]
        # Abre el diálogo para seleccionar una imagen
        ruta_imagen = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=(("Archivos de imagen", ".jpg;.jpeg;.png"), ("Todos los archivos", ".*"))
        )
        
        if not ruta_imagen:
            print("No se seleccionó ninguna imagen")
            return
        
        # Abrir y convertir la imagen en formato binario
        try:
            with open(ruta_imagen, 'rb') as file:
                imagen_binaria = file.read()
        except Exception as e:
            print(f"Error al leer la imagen: {e}")
            return
        self.objController.subirImagen(dato,imagen_binaria)
        #try:
        #    conexion = mysql.connector.connect(
        #        host="localhost",
        #        user="root",
        #        password="",
        #        database="Usuarios",
        #    )
        #    cursor = conexion.cursor()
        #    
        #    # Inserta la imagen en la base de datos
        #    sql = "INSERT INTO imagen (nombre, imagenes) VALUES (%s, %s)"
        #    valores = ("Producto desde Tkinter", imagen_binaria)
        #    cursor.execute(sql, valores)
        #    conexion.commit()
        #    print("Imagen guardada exitosamente en la base de datos")
        #
        #except mysql.connector.Error as error:
        #    print(f"Error al guardar en la base de datos: {error}")
        #
        #finally:
        #    cursor.close()
        
    def catalogoTelefono(self):
        self.catalog_title.config(text="Telefonos")
        self.actualizar_imagenes(self.imagenes4)

    def catalogoTablet(self):
        self.catalog_title.config(text="Tablets")
    def catalogoLaptop(self):
        self.catalog_title.config(text="Laptops")
        self.actualizar_imagenes(self.imagenes)

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