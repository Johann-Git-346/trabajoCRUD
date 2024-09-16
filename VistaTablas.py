import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class VistaTablas1:
    def __init__(self,objController):
        self.objController=objController

    def iniciarTablas(self):
        # Crear la ventana principal
        self.rootTablas = tk.Tk()
        self.rootTablas.title("TecnoNube")
        self.rootTablas.geometry("800x600")

        self.create_top_frame()
        self.create_menu_frame()
        """self.create_sidebar_frame()"""
        self.create_catalog_frame()
        self.crearMarcoInferior()

        self.rootTablas.mainloop()

    def create_top_frame(self):
        """ Crear el marco superior para el nombreTelefonos de la empresa y la imagen del logo. """
        self.frame_top = tk.Frame(self.rootTablas, relief=tk.RAISED,borderwidth=1)
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

        # Añadir un widget de Frame central vacío para centrar los otros widgets
        spacer_right = tk.Frame(self.frame_top)
        spacer_right.pack(side=tk.RIGHT, expand=True)

    def create_menu_frame(self):
        # Crear el marco para el menú de navegación
        frame_menu = tk.Frame(self.rootTablas, relief=tk.RAISED, borderwidth=0.5)
        frame_menu.pack(side=tk.TOP, fill=tk.X)
        frame_menu.config(background="#FFFFFF")

        # Botones de navegación
        menu_buttons = ["Inicio","Cerrar Sesion"]
        commands = [self.inicio,self.CerrarSesion]

        for text, command in zip(menu_buttons, commands):
            tk.Button(frame_menu, text=text,cursor="hand2",bg="#333333",foreground="#FFFFFF" ,command=command).grid(row=0, column=menu_buttons.index(text), padx=10, pady=5)

        # Configurar las columnas para que se expandan igualmente
        for i in range(len(menu_buttons)):
            frame_menu.grid_columnconfigure(i, weight=1)
    
    def create_catalog_frame(self):
        # Crear el marco para las categorías y el informe de productos
        frame_report = tk.Frame(self.rootTablas)
        frame_report.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        frame_report.config(background="#FFFFFF")

        # Crear el título del informe
        report_title = tk.Label(frame_report, text="Informe de Productos", font=("Arial", 16),foreground="#FFFFFF")
        report_title.pack(side=tk.TOP, pady=10)
        report_title.config(background="#333333")

        # Crear el marco para los informes de más vendidos y menos vendidos
        frame_products = tk.Frame(frame_report)
        frame_products.pack(fill=tk.BOTH, expand=True)

        # Tabla de Más Vendidos
        frame_mas_vendidos = tk.Frame(frame_products)
        frame_mas_vendidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        frame_mas_vendidos.config(background="#333333")

        mas_vendidos_title = tk.Label(frame_mas_vendidos, text="Más Vendidos", font=("Arial", 14),foreground="#FFFFFF")
        mas_vendidos_title.pack(side=tk.TOP, pady=5)
        mas_vendidos_title.config(background="#333333")

        mas_vendidos_tree = ttk.Treeview(frame_mas_vendidos, columns=("Producto", "Cantidad" ,"Categoria"), show="headings")
        mas_vendidos_tree.heading("Producto", text="Nombre Producto")
        mas_vendidos_tree.heading("Cantidad", text="Cantidad")
        mas_vendidos_tree.heading("Categoria", text="Categoria")
        mas_vendidos_tree.insert("", "end", values=("Producto 1", "10", "Categoria A"))
        mas_vendidos_tree.insert("", "end", values=("Producto 2", "20", "Categoria B"))
        mas_vendidos_tree.insert("", "end", values=("Producto 3", "30", "Categoria C"))
        mas_vendidos_tree.pack(fill=tk.BOTH, expand=True)

        # Tabla de Menos Vendidos
        frame_menos_vendidos = tk.Frame(frame_products)
        frame_menos_vendidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        frame_menos_vendidos.config(background="#333333")

        menos_vendidos_title = tk.Label(frame_menos_vendidos, text="Menos Vendidos", font=("Arial", 14),foreground="#FFFFFF")
        menos_vendidos_title.pack(side=tk.TOP, pady=5)
        menos_vendidos_title.config(background="#333333")

        menos_vendidos_tree = ttk.Treeview(frame_menos_vendidos, columns=("Producto", "Cantidad" ,"Categoria"), show="headings")
        menos_vendidos_tree.heading("Producto", text="Nombre Producto")
        menos_vendidos_tree.heading("Cantidad", text="Cantidad")
        menos_vendidos_tree.heading("Categoria", text="Categoria")
        menos_vendidos_tree.pack(fill=tk.BOTH, expand=True)

        # Botón para generar el informe
        generate_button = tk.Button(frame_report, text="Generar Informe",cursor="hand2",bg="#FFD700",foreground="black")
        generate_button.pack(side=tk.BOTTOM, pady=10)

    def crearMarcoInferior(self):
        # Crear el marco inferior para la barra de navegación
        frame_bottom = tk.Frame(self.rootTablas, relief=tk.RAISED, borderwidth=1)
        frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)


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
        self.rootTablas.destroy()
        self.objController.mostraLogin() 

    def inicio(self):
        self.rootTablas.destroy()
