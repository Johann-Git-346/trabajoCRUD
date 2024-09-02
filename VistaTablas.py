import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class VistaTablas1:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("TecnoNube")
        self.root.geometry("800x600")

        self.create_top_frame()
        self.create_menu_frame()
        self.create_catalog_frame()
        self.crearMarcoInferior()

        self.root.mainloop()

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
        # Crear el marco para el menú de navegación
        frame_menu = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        frame_menu.pack(side=tk.TOP, fill=tk.X)

        # Botones de navegación
        menu_buttons = ["Inicio", "Productos", "Servicios", "Contacto", "Perfil"]
        for i, button in enumerate(menu_buttons):
            btn = tk.Button(frame_menu, text=button)
            btn.pack(side=tk.LEFT, padx=120, pady=5)
            
            # Añadir espaciador entre los botones
            if i < len(menu_buttons) - 1:
                spacer = tk.Frame(frame_menu, width=20)
                spacer.pack(side=tk.LEFT)
    
    def create_catalog_frame(self):
        # Crear el marco para las categorías y el informe de productos
        frame_report = tk.Frame(self.root)
        frame_report.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Crear el marco de categorías
        frame_categories = tk.Frame(frame_report, relief=tk.RAISED, borderwidth=1)
        frame_categories.pack(side=tk.TOP, fill=tk.X)

        # Añadir botones de categorías
        categories = ["Smartphones", "Tablets", "Laptops", "Monitores", "Cámaras", "Audífonos", "Cargadores"]
        for category in categories:
            btn = tk.Button(frame_categories, text=category)
            btn.pack(side=tk.LEFT, padx=10, pady=5)

        # Crear el título del informe
        report_title = tk.Label(frame_report, text="Informe de Productos", font=("Arial", 16))
        report_title.pack(side=tk.TOP, pady=10)

        # Crear el marco para los informes de más vendidos y menos vendidos
        frame_products = tk.Frame(frame_report)
        frame_products.pack(fill=tk.BOTH, expand=True)

        # Tabla de Más Vendidos
        frame_mas_vendidos = tk.Frame(frame_products)
        frame_mas_vendidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        mas_vendidos_title = tk.Label(frame_mas_vendidos, text="Más Vendidos", font=("Arial", 14))
        mas_vendidos_title.pack(side=tk.TOP, pady=5)

        mas_vendidos_tree = ttk.Treeview(frame_mas_vendidos, columns=("Producto", "Cantidad"), show="headings")
        mas_vendidos_tree.heading("Producto", text="Nombre Producto")
        mas_vendidos_tree.heading("Cantidad", text="Cantidad")
        mas_vendidos_tree.pack(fill=tk.BOTH, expand=True)

        # Tabla de Menos Vendidos
        frame_menos_vendidos = tk.Frame(frame_products)
        frame_menos_vendidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        menos_vendidos_title = tk.Label(frame_menos_vendidos, text="Menos Vendidos", font=("Arial", 14))
        menos_vendidos_title.pack(side=tk.TOP, pady=5)

        menos_vendidos_tree = ttk.Treeview(frame_menos_vendidos, columns=("Producto", "Cantidad"), show="headings")
        menos_vendidos_tree.heading("Producto", text="Nombre Producto")
        menos_vendidos_tree.heading("Cantidad", text="Cantidad")
        menos_vendidos_tree.pack(fill=tk.BOTH, expand=True)

        # Botón para generar el informe
        generate_button = tk.Button(frame_report, text="Generar Informe")
        generate_button.pack(side=tk.BOTTOM, pady=10)

    def crearMarcoInferior(self):
        # Crear el marco inferior para la barra de navegación
        frame_bottom = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)

x = VistaTablas1()
