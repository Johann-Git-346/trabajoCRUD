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
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#FFFFFF")

        # Añadir botones de la barra lateral
        sidebar_buttons = ["Agregar", "Modificar", "Eliminar", "Informe", "Cerrar Sesion"]
        sidebar_commands = [self.agregar, self.modificar, self.eliminar, self.informe, self.salir]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2",text=text,bg="#FFD700",foreground="#333333", command=command).pack(fill=tk.X, padx=5, pady=15)

        # Controles multimedia (espacios reservados)
        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=5, pady=5)

    def create_catalog_frame(self):
        """ Crear el marco para las categorías y el catálogo. """
        self.frame_catalog = tk.Frame(self.rootProductos)
        self.frame_catalog.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.frame_catalog.config(background="#FFFFFF")

        # Crear el marco de categorías
        self.frame_categories = tk.Frame(self.frame_catalog, relief=tk.RAISED,borderwidth=1)
        self.frame_categories.pack(side=tk.TOP, fill=tk.X)
        self.frame_categories.config(background="#FFFFFF")

        # Añadir botones de categorías
        categories = ["Telefonos", "Tablets", "Laptops", "Monitores", "Cámaras", "Audífonos", "Cargadores"]
        comandoCategoria=[self.telefono,self.tablet,self.laptop,self.monitor,self.camara,self.audifonos,self.cargador]
        for text, comandoCategoria in zip(categories,comandoCategoria):
            tk.Button(self.frame_categories,cursor="hand2", bg="#FFD700",foreground="#333333",text=text,command=comandoCategoria).pack(side=tk.LEFT, padx=50, pady=5)

        # Crear el título del catálogo
        self.catalog_title = tk.Label(self.frame_catalog, text="Telefonos", font=("Arial", 16),foreground="#FFFFFF")
        self.catalog_title.pack(side=tk.TOP, pady=10)
        self.catalog_title.config(background="#333333")

        # Crear el marco para los productos
        self.frame_products = tk.Frame(self.frame_catalog)
        self.frame_products.pack(fill=tk.BOTH, expand=True)
        self.frame_products.config(background="#FFFFFF")

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

        for i in range(2): # filas
            row = tk.Frame(self.frame_products)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
            row.config(background="#FFFFFF")
            for j in range(7):  # columnas
                self.product_frame = tk.Frame(row, width=100, height=100, relief=tk.RAISED, borderwidth=1)
                self.product_frame.pack(side=tk.LEFT, padx=15, pady=5)

                # Asignar una imagen diferente a cada producto
                img_index = (i * 7) + j  # Calcular el índice de la imagen
                if img_index < len(self.imagenes3):
                    self.rutaimagen = self.imagenes3[img_index]
                    
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
