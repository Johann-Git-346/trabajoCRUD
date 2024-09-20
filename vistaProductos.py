import tkinter as tk
from PIL import Image, ImageTk
import os

class Davista:
    def __init__(self,objController):
        self.objController=objController

    def iniciarProductos(self):
        self.rootProductos = tk.Tk()
        self.rootProductos.title("CLIENTE")
        self.rootProductos.geometry("800x600")

        self.create_top_frame()
        self.create_sidebar_frame()
        self.create_catalog_frame()
<<<<<<< HEAD

    def create_top_frame(self):
        self.baner = tk.Frame(self.root, borderwidth=1)
        self.baner.pack(side=tk.TOP)
        
        izespacio = tk.Frame(self.baner)
        izespacio.pack(side=tk.LEFT)
        
        nombre = tk.Label(self.baner, text="TecnoNube", font=("Arial", 26), anchor="center")
        nombre.pack(side=tk.LEFT)
        
        etiqueta = tk.Label(self.baner)
        etiqueta.pack(side=tk.LEFT)
        
        rutaimagen = 'imagenes/logoc.png'
        
        if not os.path.exists(rutaimagen):
            print(f"Error: La ruta de la imagen no existe: {rutaimagen}")
            return
        
        try:
            imagen = Image.open(rutaimagen)
            imagen = imagen.resize((100, 100))
            self.imagen_tk = ImageTk.PhotoImage(imagen)  # Mantén la referencia a la imagen
            
            etiqueta_imagen = tk.Label(self.baner, image=self.imagen_tk)
            etiqueta_imagen.pack(side=tk.RIGHT, pady=10)
        
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

    def create_menu_frame(self):
        self.frame_menu = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)

        menu_buttons = ["Inicio", "Productos", "Perfil", "Contacto"]
        commands = [self.home_command, self.products_command, self.about_command, self.contact_command]

        for text, command in zip(menu_buttons, commands):
            tk.Button(self.frame_menu, text=text, command=command).grid(row=0, column=menu_buttons.index(text), padx=10, pady=5)

        for i in range(len(menu_buttons)):
            self.frame_menu.grid_columnconfigure(i, weight=1)

    def create_sidebar_frame(self):
        self.frame_sidebar = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
=======

        self.rootProductos.mainloop()
        

    def create_top_frame(self):
        """ Crear el marco superior para el nombreTelefonos de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.rootProductos, relief=tk.RAISED,borderwidth=1)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_top.config(background="#333333")

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_left = tk.Frame(self.frame_top)
        spacer_left.pack(side=tk.LEFT, expand=True)

        company_name = tk.Label(self.frame_top, text="TecnoNube", foreground="#FFFFFF",font=("Arial", 24), anchor="center")
        company_name.pack(side=tk.LEFT, padx=10, pady=10)
        company_name.config(background="#333333")


        logo = tk.Frame(self.frame_top)
        logo.pack(side=tk.RIGHT, padx=20, pady=20)

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_right = tk.Frame(self.frame_top)
        spacer_right.pack(side=tk.RIGHT, expand=True)

        etiqueta = tk.Label(logo)
        etiqueta.pack(side=tk.RIGHT)
        
        self.rutaimagen = 'imagenes/LOGO.jpg'
        
        if not os.path.exists(self.rutaimagen):
            print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
            return
        
        try:
            imagen = Image.open(self.rutaimagen)
            imagen = imagen.resize((155, 130))
            self.imagen_tk = ImageTk.PhotoImage(imagen)  # Mantén la referencia a la imagen
            
            etiqueta_imagen = tk.Label(logo, image=self.imagen_tk)
            etiqueta_imagen.pack()
        
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

    def create_sidebar_frame(self):
        """ Crear el marco para la barra lateral izquierda y añadir botones. """
        self.frame_sidebar = tk.Frame(self.rootProductos, relief=tk.RAISED,borderwidth=1)
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#FFFFFF")

<<<<<<< HEAD
        sidebar_buttons = ["Apps", "Juegos", "Peliculas", "Libros", "Noticias"]
        sidebar_commands = [self.apps_command, self.games_command, self.movies_command, self.books_command, self.newspapers_command]
=======
        # Añadir botones de la barra lateral
        sidebar_buttons = ["Agregar", "Modificar", "Eliminar", "Informe", "Cerrar Sesion"]
        sidebar_commands = [self.agregar, self.modificar, self.eliminar, self.informe, self.salir]
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2",text=text,bg="#FFD700",foreground="#333333", command=command).pack(fill=tk.X, padx=5, pady=15)

        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=5, pady=5)

    def create_catalog_frame(self):
<<<<<<< HEAD
        self.frame_catalog = tk.Frame(self.root)
=======
        """ Crear el marco para las categorías y el catálogo. """
        self.frame_catalog = tk.Frame(self.rootProductos)
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#FFFFFF")

<<<<<<< HEAD
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED, borderwidth=1)
=======
        # Crear el marco de categorías
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED,borderwidth=1)
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#FFFFFF")

<<<<<<< HEAD
        categories = ["Smartphones", "Tablets", "Laptops", "Monitores", "Cámaras", "Audífonos", "Cargadores"]
        for category in categories:
            tk.Button(self.frame_categories, text=category).pack(side=tk.LEFT, padx=10, pady=5)

        catalog_title = tk.Label(self.frame_catalog, text="Título del Catálogo", font=("Arial", 16))
        catalog_title.pack(side=tk.TOP, pady=10)
=======
        # Añadir botones de categorías
        categories = ["Telefonos", "Tablets", "Laptops", "Monitores", "Cámaras", "Audífonos", "Cargadores"]
        comandoCategoria=[self.telefono,self.tablet,self.laptop,self.monitor,self.camara,self.audifonos,self.cargador]
        for text, comandoCategoria in zip(categories,comandoCategoria):
            tk.Button(self.frame_categories,cursor="hand2", bg="#FFD700",foreground="#333333",text=text,command=comandoCategoria).pack(side=tk.LEFT, padx=50, pady=5)

        # Crear el título del catálogo
        self.catalog_title = tk.Label(self.frame_catalog, text="Telefonos", font=("Arial", 16),foreground="#FFFFFF")
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#333333")
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103

        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#FFFFFF")

<<<<<<< HEAD
        # Cargar una sola vez la imagen productoc.png
        product_image_path = 'imagenes/productoc.png'  # Ruta a la imagen que se utilizará para todos los productos
        
        print("Intentando cargar la imagen desde:", product_image_path)
        if not os.path.exists(product_image_path):
            print(f"Error: La ruta de la imagen no existe: {product_image_path}")
            return
        
        try:
            imagen = Image.open(product_image_path)
            print("Imagen cargada correctamente")
            imagen = imagen.resize((100, 100))  # Redimensiona la imagen si es necesario
            self.product_image = ImageTk.PhotoImage(imagen)  # Mantén la referencia a la imagen
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")
            self.product_image = None
=======
        self.crearmarcos()

    def crearmarcos(self):

        self.imagenes2=["imagenes/compu1.jpg","imagenes/compu2.jpg","imagenes/compu3.jpeg","imagenes/compu4.jpg","imagenes/compu5.jpeg","imagenes/compu6.png",
               "imagenes/compu7.jpeg","imagenes/compu8.jpg","imagenes/compu9.jpeg","imagenes/compu10.jpg","imagenes/compu11.jpg","imagenes/compu12.jpg",
               "imagenes/compu13.png","imagenes/compu14.png"]
        self.imagenes3=["imagenes/cel.jpg","imagenes/cel2.jpg","imagenes/cel3.jpg","imagenes/cel4.jpg","imagenes/cel5.jpg","imagenes/cel6.jpeg",
                       "imagenes/cel7.jpeg","imagenes/cel8.jpeg","imagenes/cel9.jpg","imagenes/cel10.jpg","imagenes/cel11.png","imagenes/cel12.jpg",
                       "imagenes/cel13.jpg","imagenes/cel14.jpg"]
        
        self.imagenes_tk = []
        self.labels_imagenes = []
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103

        for i in range(2): # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#FFFFFF")
            for j in range(7):  # columnas
                self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)

<<<<<<< HEAD
                if self.product_image is not None:
                    img_label = tk.Label(product_frame, image=self.product_image)
                else:
                    img_label = tk.Label(product_frame, text="Sin Imagen", bg="lightgray", width=10, height=5)
=======
                # Asignar una imagen diferente a cada producto
                img_index = (i * 7) + j  # Calcular el índice de la imagen
                if img_index < len(self.imagenes3):
                    self.rutaimagen = self.imagenes3[img_index]
                    
                    if not os.path.exists(self.rutaimagen):
                        print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
                        continue
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103
                
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

<<<<<<< HEAD
                info_label = tk.Label(product_frame, text=f"Producto {(i * 7) + j + 1}\nCategoría\nPrecio", justify=tk.LEFT)
                info_label.pack()

    def home_command(self):
        print("Home button clicked")
=======
                info_label = tk.Label(self.product_frame, text=f"Producto {img_index + 1}\nCategoría\nPrecio", justify=tk.LEFT)
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
                    imagen = imagen.resize((110, 110))      
                    imagen_tk = ImageTk.PhotoImage(imagen)  # Crear una nueva referencia a la imagen
                    self.imagenes_tk[img_index] = imagen_tk  # Actualizar la referencia en la lista
                    
                    etiqueta_imagen.config(image=imagen_tk)
                
                except Exception as e:
                    print(f"Error al abrir o procesar la imagen: {e}")
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103

    def catalogoTablet(self):
        self.catalog_title.config(text="Tablets")

    def catalogoLaptop(self):
        self.catalog_title.config(text="Laptops")
        self.actualizar_imagenes(self.imagenes2)

    def catalogoTelefono(self):
        self.catalog_title.config(text="Telefonos")
        self.actualizar_imagenes(self.imagenes3)

    def catalogoMonitor(self):
        self.catalog_title.config(text="Monitores")
    def catalogoCamara(self):
        self.catalog_title.config(text="Camaras")
    def catalogoAudifonos(self):
        self.catalog_title.config(text="Audifonos")
    def catalogoCargador(self):
        self.catalog_title.config(text="Cargadores")

    def salir(self):
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
        self.rootProductos.destroy()
        self.objController.mostrarLogin()   

    def agregar(self):
        print("agregar button clicked")

    def modificar(self):
        print("modificar button clicked")

<<<<<<< HEAD
# Crear la ventana principal
root = tk.Tk()
app = Davista(root)
root.mainloop()
=======
    def eliminar(self):
        print("eliminar button clicked")


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
>>>>>>> 0b2dfe525694170464f984a889026f185bc62103
