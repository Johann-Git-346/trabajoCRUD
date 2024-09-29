import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox

class Davista3:
    def __init__(self,objController):
        self.objController=objController
    
    def iniciarCliente(self):
        self.rootVendedor = tk.Tk()
        self.rootVendedor.title("CLIENTE")
        self.rootVendedor.geometry("800x600")

        self.rootVendedor.state('zoomed')

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

    def create_sidebar_frame(self):
        """ Crear el marco para la barra lateral izquierda y añadir botones. """
        self.frame_sidebar = tk.Frame(self.rootVendedor, relief=tk.RAISED, borderwidth=1)
        self.frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_sidebar.config(background="#D3D3D3")

        # Añadir botones de la barra lateral
        sidebar_buttons = ["Agregar", "Modificar", "Eliminar", "Comprar", "Cerrar sesion"]
        sidebar_commands = [ self.Agregar_Pedido, self.Modificar_Pedido, self.Eliminar_Pedido, self.Comprar_Pedido, self.CerrarSesion]

        for text, command in zip(sidebar_buttons, sidebar_commands):
            tk.Button(self.frame_sidebar, cursor="hand2",bg="#87CEEB",foreground="black",font=("Arial", 10,"bold"),text=text, command=command).pack(fill=tk.X, padx=10, pady=20)

        # Controles multimedia (espacios reservados)
        multimedia_frame = tk.Frame(self.frame_sidebar)
        multimedia_frame.pack(fill=tk.X, padx=10, pady=10)

    def create_catalog_frame(self):
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
        categories = ["Celular", "Laptops"]
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
        self.rutaimagen = producto[5]  
        
        if not os.path.exists(self.rutaimagen):
            print(f"Error: La ruta de la imagen no existe: {self.rutaimagen}")
            return
        
        try:
            imagen = Image.open(self.rutaimagen)
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
        info_label.config(bg="#B0E0E6",font=("Arial", 10,"bold"),foreground="#000000",)

    def actualizar_catalogo(self,categoria):
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

    def Agregar_Pedido(self):#cambiar la funcinalidad = comprar
        self.ventanaAgregar=tk.Toplevel()
        self.ventanaAgregar.title("agregar producto")
        self.ventanaAgregar.geometry("500x500")
        self.ventanaAgregar.config(bg="lightblue")
        self.contenedor2=tk.Frame(self.ventanaAgregar, bg="lightblue")
        self.contenedor2.pack()

    def catalogoTelefono(self):
        self.catalog_title.config(text="celulares")
        self.mostrar_productos_categoria("celular")
        self.actualizar_catalogo("celular")

    def catalogoLaptop(self):
        self.catalog_title.config(text="Laptops")
        self.mostrar_productos_categoria("laptop")
        self.actualizar_catalogo("laptop")

    def Modificar_Pedido(self):
        self.ventanaBuscarModificar=tk.Toplevel()
        self.ventanaBuscarModificar.title("buscar producto")
        self.ventanaBuscarModificar.geometry("400x200")
        self.ventanaBuscarModificar.config(bg="lightblue")
        self.contenedor7=tk.Frame(self.ventanaBuscarModificar,bg="lightblue")
        self.contenedor7.pack(padx=10,pady=10)
        

    def Comprar_Pedido(self):
        self.ventanaComprar=tk.Toplevel()
        self.ventanaComprar.title("Comprar producto")
        self.ventanaComprar.geometry("400x200")
        self.ventanaComprar.config(bg="lightblue")
        self.contenedor4=tk.Frame(self.ventanaComprar,bg="lightblue")
        self.contenedor4.pack(padx=10,pady=10)
        

    def Eliminar_Pedido(self):
        self.ventanaEliminar=tk.Toplevel()
        self.ventanaEliminar.title("eliminar producto")
        self.ventanaEliminar.geometry("400x200")
        self.ventanaEliminar.config(bg="lightblue")
        self.contenedor3=tk.Frame(self.ventanaEliminar,bg="lightblue")
        self.contenedor3.pack(padx=10,pady=10)
        nombreEliminar=tk.StringVar()
        self.labelEliminar=tk.Label(self.contenedor3,text="ingrese el nombre del producto a eliminar",bg="lightblue",font=("Arial", 12,"bold"))
        self.labelEliminar.pack(padx=10,pady=10)
        self.entryEliminar=tk.Entry(self.contenedor3, textvariable=nombreEliminar)
        self.entryEliminar.pack(padx=10,pady=10)
        self.botonEliminar=tk.Button(self.contenedor3, text="eliminar",cursor="hand2",command=lambda:self.Eliminar_Pedido(nombreEliminar),bg="lightgreen", font=("Arial", 12, "bold"))
        self.botonEliminar.pack(padx=10,pady=10)
        
    def Eliminar_Pedido(self,datoEliminar):
        self.ventanaEliminar.destroy()
        nombre = datoEliminar.get()
        if not nombre:
            messagebox.showerror("Error", "El nombre del producto es obligatorio para eliminarlo")
            return

        producto = self.objController.obtener_producto_por_nombre(nombre)
        if producto:
            self.objController.Eliminar_Pedido(nombre)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def CerrarSesion(self):
        self.mensajeCerrrarSesion=tk.Toplevel()
        self.mensajeCerrrarSesion.title("¿seguro?")
        self.mensajeCerrrarSesion.geometry("350x250")
        self.mensajeCerrrarSesion.config(bg="lightblue")
        self.respuesta=tk.StringVar()
        self.contenedorMensaje=tk.Frame(self.mensajeCerrrarSesion,bg="lightblue")
        self.contenedorMensaje.pack()
        self.labelMensaje=tk.Label(self.contenedorMensaje,text="¿Esta seguro que desea cerrar sesion?",font=("Arial", 12,"bold"),bg="lightblue")
        self.labelMensaje.pack(padx=10,pady=10)
        self.botonSi=tk.Button(self.contenedorMensaje,text="SI",command=self.salirTodo,bg="red",cursor="hand2", font=("Arial", 12, "bold"))
        self.botonSi.pack(padx=10,pady=10)
        self.botonNo=tk.Button(self.contenedorMensaje,text="NO",command=self.destruirMensaje,cursor="hand2", bg="lightgreen", font=("Arial", 12, "bold"))
        self.botonNo.pack(padx=10,pady=10)
        
    def destruirMensaje(self):
        self.mensajeCerrrarSesion.destroy()

    def salirTodo(self):
        self.mensajeCerrrarSesion.destroy()
        self.rootVendedor.destroy()
        self.objController.mostrarLogin()